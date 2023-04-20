from StaticError import *
from Utils import Utils
from Visitor import *
from AST import *
from functools import reduce

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class ExpUtils:
    def infer(env, name, typ):
        for symbol_list in env:
            for symbol in symbol_list:
                if symbol.name == name:
                    symbol.typ = typ
        return typ
    
    def flatter(scope):
        return list(reduce(lambda x,y: x+y, scope,[]))
    
    @staticmethod
    def isNaN(expType):
        return type(expType) not in [IntegerType, FloatType, AutoType]
    
    @staticmethod
    def isStmt(expType):
        return type(expType) in [AssignStmt, BlockStmt, IfStmt, ForStmt, WhileStmt, DoWhileStmt, BreakStmt, ContinueStmt, ReturnStmt, CallStmt]
    
    @staticmethod
    def isOpForNumber(op):
        return op in ['+', '-', '*', '/', '%', '!=', '==', '>', '<', '>=', '<=']

    @staticmethod
    def isOpForInt(op):
        return op in ['%', '!=', '==']

    # @staticmethod
    # def isOpForFloat(op):
    #     return op in ['+', '-', '*', '/', '>', '<', '>=', '<=']

    @staticmethod
    def mergeNumType(ltype, rtype):
        return FloatType() if FloatType in [type(x) for x in [ltype, rtype]] else IntegerType()

class Symbol:
    def __init__(self, name, type, inherit=None, kind=Function(), isGlobal=False):
        self.name = name
        self.type = type
        self.inherit = inherit
        self.kind = kind
        self.isGlobal = isGlobal

    def getKind(self):
        return self.kind if type(self.type) is MType else Identifier()

    def toTuple(self):
        return (self.name, type(self.getKind()))
    
    def toString(self):
        tmp = str(self.name)+str(self.kind)
        return tmp

    def toParam(self):
        self.kind = Parameter()
        return self
    
    def toVar(self):
        self.kind = Variable()
        return self
    
    def toGlobal(self):
        self.isGlobal = True
        return self
    
    @staticmethod
    def cmp(symbol):
        return symbol.name

    @staticmethod
    def fromVarDecl(decl):
        if type(decl.typ) is AutoType and decl.init is None:
            raise Invalid(Variable(), decl.name)
        return Symbol(decl.name, decl.typ, kind=Variable())
    
    @staticmethod
    def fromFuncDecl(decl):
        paramsType = [x.typ for x in decl.params]
        return Symbol(decl.name, MType(paramsType, decl.return_type), kind=Function())
    
    @staticmethod
    def fromDecl(decl):
        return Symbol.fromVarDecl(decl) if type(decl) is VarDecl else Symbol.fromFuncDecl(decl)

class Scope:
    @staticmethod
    def isExisted(symbol_list, symbol):
        return len([x for x in symbol_list if x.name == symbol.name]) > 0
    
    @staticmethod
    def merge(curScope, nextScope):
        return reduce(lambda lst, sym: lst if Scope.isExisted(lst, sym) else lst + [sym], curScope, nextScope)

class Checker:
    utils = Utils()

    @staticmethod
    def checkRedeclared(curScope, symbol):
        # print(curScope)
        if len(curScope[0]) != 0:
            f = Checker.utils.lookup(symbol.name, curScope[0], Symbol.cmp)
            if f is not None:
                raise Redeclared(symbol.kind, symbol.name)
            # newScope.append(symbol)
        curScope[0] = [symbol] + curScope[0]
        return curScope
    
    @staticmethod
    def checkUndeclared(visibleScope, name, kind):
        scope = list(reduce(lambda x,y: x+y, visibleScope,[]))
        # print(scope, name)
        res = Checker.utils.lookup((name, type(kind)), scope, lambda x: x.toTuple())
        if res is None:
            raise Undeclared(kind, name)
        return res
    
    # @staticmethod
    # def matchArrayType(a, b):
    #     return a.low

    @staticmethod
    def matchType(patternType, paramType):
        if ArrayType in [type(x) for x in [patternType, paramType]]:
            if type(patternType) != type(paramType): return False
            return Checker.matchArrayType(patternType, paramType)

        if AutoType in [type(patternType), type(paramType)]: return True
        if type(patternType) == type(paramType): return True
        if type(patternType) is FloatType and type(paramType) is IntegerType: return True
        return False

    @staticmethod
    def checkParamType(pattern, param):
        if len(pattern) != len(param): return False
        return all([Checker.matchType(x, y) for x, y in zip(pattern, param)])
    
    @staticmethod
    def handleReturnStmt(stmts):
        for i in range(0, len(stmts)-1):
            if Checker.isStopTypeStatement(stmts[i][1]):
                return None
        return None if stmts == [] else stmts[-1][1]

    @staticmethod
    def isReturnTypeFunction(rettype):
        return type(rettype) in [IntegerType, FloatType, BooleanType, StringType, ArrayType]

    def isReturnTypeCall(rettype):
        return type(rettype) is VoidType

    @staticmethod
    def isReturnType(rettype):
        return Checker.isReturnTypeFunction(rettype) or type(rettype) in [BreakStmt, ContinueStmt]

    @staticmethod
    def isStopTypeStatement(rettype):
        return Checker.isReturnType(rettype) or type(rettype) in [BreakStmt, ContinueStmt]

class StaticChecker(Visitor):
    global_env = [
        Symbol('readInteger', MType([], IntegerType())),
        Symbol('printInteger', MType([Symbol('',IntegerType(),kind=Parameter())], VoidType())),
        Symbol('readFloat', MType([], FloatType())),
        Symbol('writeFloat', MType([Symbol('',FloatType(),kind=Parameter())], VoidType())),
        Symbol('readBoolean', MType([], BooleanType())),
        Symbol('printBoolean', MType([Symbol('',BooleanType(),kind=Parameter())], VoidType())),
        Symbol('readString', MType([], StringType())),
        Symbol('printString', MType([Symbol('',StringType(),kind=Parameter())], VoidType())),
        # Symbol('super', MType([IntegerType()], VoidType())),
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visitProgram(self.ast, StaticChecker.global_env)

    def visitProgram(self, ast: Program, param): 
        funcdecls = [Symbol.fromDecl(x) for x in ast.decls if type(x) is FuncDecl]
        # symbols = [Symbol.fromDecl(x) for x in ast.decl]
        # entryPoint = Symbol('main', MType([], VoidType()), kind=Function())
        # res = Checker.utils.lookup(entryPoint.toTuple, funcdecls, lambda x: x.toTuple())
        # if len(funcdecls) == 0 or res is None: raise NoEntryPoint()
        entryPoint = Symbol('main', MType([], VoidType()), kind=Function())
        func_list = param + [entryPoint] + funcdecls
        env = [[]]
        for decl in ast.decls:
            env = self.visit(decl, (env, func_list))
        res = Checker.utils.lookup(entryPoint.toString(), funcdecls, lambda x: x.toString())
        if res is None: raise NoEntryPoint()
        return []

    def visitVarDecl(self, ast: VarDecl, param): 
        env = param[0]
        if ast.init is None:    
            if type(ast.typ) is AutoType:
                raise Invalid(Variable(), ast.name)
        else: 
            typ = self.visit(ast.init, param)
            if type(ast.typ) is AutoType:
                ast.typ = self.visit(ast.init, param)
            elif type(ast.typ) is not type(typ):
                raise TypeMismatchInVarDecl(ast)
        return Checker.checkRedeclared(env, Symbol(ast.name, ast.typ, kind=Variable()))
        
    
    #inherit processing
    def visitFuncDecl(self, ast: FuncDecl, param): 
        env, func_list = param
        params_list = [self.visit(x, env).toParam() for x in ast.params]
        env = [params_list] + env
        inherit_list = []
        if ast.inherit:
            inherit = Checker.checkUndeclared(env+[func_list], ast.inherit, Function())
            if len(inherit.type.partype) != 0 and (type(ast.body.body[0]) is not CallStmt or not ast.body.body[0].name in ['super', 'preventDefault']):
                raise InvalidStatementInFunction(ast.name)
            #take inherited params from parent function
            for symbol in inherit.type.partype:
                if symbol.inherit:
                    inherit_list += symbol
            self.handleSuper(ast.body.body[0], inherit_list, (env, func_list))
        env[0] = inherit_list + env[0]
        for i in range(1 if ast.inherit else 0, len(ast.body.body)):
            if ExpUtils.isStmt(ast.body.body[i]):
                self.visit(ast.body.body[i], (env, func_list, ast.return_type, False)) #pass another param in visit
            else:
                env = self.visit(ast.body.body[i], (env, func_list))
        return [[Symbol(ast.name, MType(params_list, ast.return_type))]] + param[0]

    def visitParamDecl(self, ast: ParamDecl, param): 
        return Symbol(ast.name, ast.typ, inherit=True) if ast.inherit else Symbol(ast.name, ast.typ)

    #Statementssw
    def visitAssignStmt(self, ast, param): 
        scope, func_list, rettype, inloop = param
        ltype = self.visit(ast.lhs, (scope, func_list))
        rtype = self.visit(ast.rhs, (scope, func_list))
        if type(ltype) in [VoidType, ArrayType] or not Checker.matchType(ltype, rtype):
            raise TypeMismatchInStatement(ast)
        if type(ltype) is AutoType:
            ExpUtils.infer(scope, ast.lhs.name, rtype)
            return
        if type(rtype) is AutoType:
            ExpUtils.infer(scope, ast.rhs.name, ltype)
            return
        return

    def visitBlockStmt(self, ast, param): 
        scope, func_list, rettype, inloop = param
        env = [[]] + scope
        self.checkScope(env)
        for x in ast.body:
            if ExpUtils.isStmt(x):
                self.visit(x, (env, func_list, rettype, inloop)) #pass another param in visit
            else:
                env = self.visit(x, (env, func_list))

    
    def visitIfStmt(self, ast, param): 
        scope, func_list, rettype, inloop = param
        condtype = self.visit(ast.cond, (scope, func_list))
        if type(condtype) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.tstmt, param)
        if ast.fstmt: 
            self.visit(ast.fstmt, param) 
        return

    def visitForStmt(self, ast, param): 
        scope, func_list, rettype, inloop = param
        initype = self.visit(ast.init.lhs, (scope, func_list))
        self.visit(ast.init, param)
        condtype = self.visit(ast.cond, (scope, func_list))
        uptype = self.visit(ast.upd, (scope, func_list))
        if False in [x is IntegerType for x in [type(initype), type(uptype)]] or type(condtype) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, (scope, func_list, rettype, True))
        return
        
    def visitWhileStmt(self, ast, param): 
        scope, func_list, rettype, inloop = param
        condtype = self.visit(ast.cond, (scope, func_list))
        if type(condtype) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, (scope, func_list, rettype, True))
        return 
    
    def visitDoWhileStmt(self, ast, param): 
        scope, func_list, rettype, inloop = param
        self.visit(ast.stmt, (scope, func_list, rettype, True))
        condtype = self.visit(ast.cond, (scope, func_list))
        if type(condtype) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        return

    def visitBreakStmt(self, ast, param): 
        if not param[3]:
            raise MustInLoop(ast)
        return
    
    def visitContinueStmt(self, ast, param): 
        if not param[3]:
            raise MustInLoop(ast)
        return 
    
    def visitReturnStmt(self, ast, param): 
        scope, func_list, rettype, inloop = param
        if not ast.expr and type(rettype) is not VoidType:
            raise TypeMismatchInStatement(ast)
        ret = self.visit(ast.expr, (scope, func_list))
        if type(ret) is not type(rettype):
            raise TypeMismatchInStatement(ast)
        return 
    
    def visitCallStmt(self, ast, param): 
        scope, func_list, rettype, inloop = param
        symbol = Checker.checkUndeclared(scope+[func_list], ast.name, Function())
        if len(ast.args) != len(symbol.type.partype):
            raise TypeMismatchInStatement(ast)
        for i in range(len(ast.args)):
            para = self.visit(ast.args[i], (scope, func_list))
            if type(para) is not type(symbol.type.partype[i].type):
                raise TypeMismatchInStatement(ast)
        # return
        # symbol = self.handleCall(ast, scope+[func_list], Function(), 'CallStmt')
        # if type(symbol.type.rettype) is VoidType:
        #     raise TypeMismatchInExpression(ast)
        return symbol.type.rettype
    

    # Expressions
    def visitBinExpr(self, ast: BinExpr, param): 
        scope, func_list = param
        ltype = self.visit(ast.left, param)
        rtype = self.visit(ast.right, param)
        op = ast.op
        if ExpUtils.isOpForNumber(op):
            if ExpUtils.isNaN(ltype) or ExpUtils.isNaN(rtype):
                raise TypeMismatchInExpression(ast)
            if ExpUtils.isOpForInt(op):
                if FloatType in [type(ltype), type(rtype)]:
                    raise TypeMismatchInExpression(ast)
                if type(ltype) is AutoType:
                    ExpUtils.infer(scope, ast.left.name, IntegerType())
                if type(rtype) is AutoType:
                    ExpUtils.infer(scope, ast.right.name, IntegerType())
                if op == '%': 
                    return IntegerType()
                return BooleanType()
            if type(ltype) is AutoType():
                ltype = ExpUtils.infer(scope, ast.left.name, rtype)
            if type(rtype) is AutoType():
                rtype = ExpUtils.infer(scope, ast.right.name, ltype)
            if op in ['+','-','*']: 
                return ExpUtils.mergeNumType(ltype, rtype)
            if op == '/': return FloatType()
            return BooleanType()
        if op == '::':
            if type(ltype) is AutoType():
                ltype = ExpUtils.infer(scope, ast.left.name, StringType())
            if type(rtype) is AutoType():
                rtype = ExpUtils.infer(scope, ast.right.name, StringType())
            if False in [type(x) is StringType for x in [ltype, rtype]]:
                raise TypeMismatchInExpression(ast)
            return StringType()
        if type(ltype) is AutoType():
                ltype = ExpUtils.infer(scope, ast.left.name, BooleanType())
        if type(rtype) is AutoType():
            rtype = ExpUtils.infer(scope, ast.right.name, BooleanType())
        if False in [type(x) is BooleanType for x in [ltype, rtype]]:
            raise TypeMismatchInExpression(ast)
        return BooleanType()
    
    def visitUnExpr(self, ast: UnExpr, param): 
        scope, func_list = param
        otype = self.visit(ast.val, param)
        op = ast.op
        if op == '-':
            if ExpUtils.isNaN(otype): 
                raise TypeMismatchInExpression(ast)
        elif op == '!':
            if not type(otype) in [BooleanType, AutoType]:
                raise TypeMismatchInExpression(ast)
            if type(otype) is AutoType:
                otype = ExpUtils.infer(scope, ast.val.name, BooleanType())
        else:
            if type(otype) is not ArrayType:
                raise TypeMismatchInExpression(ast)
        return otype
        
    def visitId(self, ast: Id, param): 
        symbol = Checker.checkUndeclared(param[0], ast.name, Identifier())
        return symbol.type
    
    def visitArrayCell(self, ast: ArrayCell, param): 
        arrtype = self.visit(Id(ast.name), param)
        exp_list = [self.visit(x, param) for x in ast.cell]
        if False in [type(x) is IntegerType for x in exp_list]:
            raise TypeMismatchInExpression(ast)
        return arrtype.typ

    def visitFuncCall(self, ast: FuncCall, param): 
        scope, func_list = param
        symbol = self.handleCall(ast, scope+[func_list], Function(), 'FuncCall')
        if type(symbol.type.rettype) is VoidType:
            raise TypeMismatchInExpression(ast)
        return symbol.type.rettype

    def handleCall(self, ast, scope, kind, typ):
        symbol = Checker.checkUndeclared(scope, ast.name, kind)
        params = [self.visit(x, scope) for x in ast.cell]
        if not Checker.checkParamType(symbol.type.partype, params):
            raise TypeMismatchInExpression(ast) if typ == 'FuncCall' else TypeMismatchInStatement(ast)
        return symbol

    # param is list of inherited params from parent func
    def handleSuper(self, ast, param, params):
        if len(ast.agrs) > len(param):
            raise TypeMismatchInExpression(ast.agrs[len(param)])
        if len(ast.agrs) < len(param):
            raise TypeMismatchInExpression()
        for i in range(len(ast.args)):
            symbol = self.visit(ast.args[i], params)
            if type(symbol) is not type(param[i].type):
                raise TypeMismatchInExpression(ast.args[i])
            
    def checkScope(self, env):
        for symbol_list in env:
            for symbol in symbol_list:
                print(symbol.name)
            
    # Visit literal => return corresponding type
    def visitIntegerLit(self, ast, param): 
        return IntegerType()
    
    def visitFloatLit(self, ast, param): 
        return FloatType()
    
    def visitBooleanLit(self, ast, param): 
        return BooleanType()
    
    def visitStringLit(self, ast, param): 
        return StringType()
        
    def visitArrayLit(self, ast, param):
        exp_list = [self.visit(x, param) for x in ast.explist]
        for i in range(len(exp_list)-1):
            if type(exp_list[i]) is not type(exp_list[i+1]):
                raise IllegalArrayLiteral(ast)
        return ArrayType([len(ast.explist)], type(exp_list[0]))
            
