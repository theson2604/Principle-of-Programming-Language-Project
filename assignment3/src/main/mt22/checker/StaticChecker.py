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
                    if type(symbol.kind) is Function:
                        symbol.type.rettype = typ
                    else:    
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

    @staticmethod
    def mergeNumType(ltype, rtype):
        return FloatType() if FloatType in [type(x) for x in [ltype, rtype]] else IntegerType()

class Symbol:
    def __init__(self, name, type, inherit=None, kind=Function(), body=None):
        self.name = name
        self.type = type
        self.inherit = inherit
        self.kind = kind
        self.body = body

    def getKind(self):
        return self.kind if type(self.type) is MType else Identifier()

    def toTuple(self):
        return (self.name, type(self.getKind()))
    
    def toString(self):
        tmp = str(self.name)+str(self.type.rettype)+str(self.kind) if type(self.type) is MType else str(self.name)+str(self.kind)
        return tmp

    def toParam(self):
        self.kind = Parameter()
        return self
    
    def toVar(self):
        self.kind = Variable()
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
        paramsType = [Symbol(x.name, x.typ, inherit=True, kind=Parameter()) if x.inherit else Symbol(x.name, x.typ, kind=Parameter()) for x in decl.params]
        return Symbol(decl.name, MType(paramsType, decl.return_type), kind=Function(), body=decl.body)
    
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
        if len(curScope[0]) != 0:
            f = Checker.utils.lookup(symbol.name, curScope[0], Symbol.cmp)
            if f is not None:
                raise Redeclared(symbol.kind, symbol.name)
        curScope[0] += [symbol]
        return curScope
    
    @staticmethod
    def checkUndeclared(visibleScope, name, kind):
        scope = list(reduce(lambda x,y: x+y if type(y) is list else x, visibleScope,[]))
        if scope == []: scope = visibleScope
        res = Checker.utils.lookup(name, scope, lambda x: x.name if type(x) is Symbol else x)
        # if res is None or (type(res.kind) is Variable and type(kind) is not Identifier):
        if res is None or (type(kind) is Identifier and type(res.kind) is Function):
            raise Undeclared(kind, name)
        return res
    
    @staticmethod
    def matchType(patternType, paramType):
        if ArrayType in [type(x) for x in [patternType, paramType]]:
            if type(patternType) != type(paramType): return False
            return Checker.matchArrayType(patternType, paramType)

        if AutoType in [type(patternType), type(paramType)]: return True
        if type(patternType) is type(paramType): return True
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
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visitProgram(self.ast, StaticChecker.global_env)

    def visitProgram(self, ast: Program, param): 
        funcdecls = [Symbol.fromDecl(x) for x in ast.decls if type(x) is FuncDecl]
        entryPoint = Symbol('main', MType([], VoidType()), kind=Function())
        func_list = param + [entryPoint] + funcdecls
        env = [[]]
        for decl in ast.decls:
            env = self.visit(decl, (env, func_list))
        res = Checker.utils.lookup(entryPoint.toString(), funcdecls, lambda x: x.toString())
        if res is None: raise NoEntryPoint()
        return []

    def visitVarDecl(self, ast: VarDecl, param): 
        env, func_list = param
        new_env = Checker.checkRedeclared(env, Symbol(ast.name, ast.typ, kind=Variable()))
        if ast.init is None:    
            if type(ast.typ) is AutoType:
                raise Invalid(Variable(), ast.name)
        else: 
            typ = self.visit(ast.init, param)
            if type(ast.typ) is AutoType:
                new_env[0][len(new_env[0])-1].type = typ
            elif type(typ) is AutoType:
                if type(ast.init) is FuncCall:
                    ExpUtils.infer(env+[func_list], ast.init.name, ast.typ)
            elif type(ast.typ) is FloatType and type(typ) is IntegerType:
                pass
            elif type(ast.typ) is not type(typ):
                raise TypeMismatchInVarDecl(ast)
        return new_env
        
    
    def visitFuncDecl(self, ast: FuncDecl, param): 
        env, func_list = param
        if type(ast.return_type) is AutoType:
            for symbol in func_list:
                if symbol.name == ast.name:
                    ast.return_type = symbol.type.rettype
        inherit_list = []
        if ast.inherit:
            inherit = Checker.checkUndeclared(env+[func_list], ast.inherit, Function())
            #take inherited params from parent function
            for symbol in inherit.type.partype:
                if symbol.inherit:
                    inherit_list += [symbol]
            if len(ast.body.body) != 0 and type(ast.body.body[0]) is CallStmt and ast.body.body[0].name == 'preventDefault':
                inherit_list = []
        params_list = []
        for x in ast.params:
            params_list = self.visit(x, (params_list, inherit_list))
        env = [params_list] + env
        start = 0
        if ast.inherit:
            if len(inherit.type.partype) != 0:
                if len(ast.body.body) == 0 or type(ast.body.body[0]) is not CallStmt or not ast.body.body[0].name in ['super', 'preventDefault']:
                    raise InvalidStatementInFunction(ast.name)
                start = 1
                inherit_list = [] if not self.handleSuper(ast.body.body[0], inherit.type.partype, (env, func_list)) else inherit_list
            else:
                if len(ast.body.body) == 0 or type(ast.body.body[0]) is not CallStmt or not ast.body.body[0].name in ['super', 'preventDefault']:
                    pass
                else: 
                    start = 1
                    inherit_list = [] if not self.handleSuper(ast.body.body[0], inherit.type.partype, (env, func_list)) else inherit_list
        env[0] = inherit_list + env[0] 
        for i in range(start, len(ast.body.body)):
            if ExpUtils.isStmt(ast.body.body[i]):
                self.visit(ast.body.body[i], (env, func_list, ast.return_type, False, ast.name)) #pass another param in visit
            else:
                env = self.visit(ast.body.body[i], (env, func_list))
        if type(ast.return_type) is AutoType:
            for symbol in func_list:
                if symbol.name == ast.name:
                    ast.return_type = symbol.type.rettype
        return Checker.checkRedeclared(param[0], Symbol(ast.name, MType(params_list, ast.return_type)))

    def visitParamDecl(self, ast: ParamDecl, param):
        params_list, inherit_list = param
        symbol = Symbol(ast.name, ast.typ, inherit=True, kind=Parameter()) if ast.inherit else Symbol(ast.name, ast.typ, kind=Parameter())
        if len(inherit_list) != 0:
            f = Checker.utils.lookup(symbol.name, inherit_list, Symbol.cmp)
            if f is not None:
                raise Invalid(symbol.kind, symbol.name)
        params_list = Checker.checkRedeclared([params_list], symbol)
        return params_list[0]

    #Statements
    def visitAssignStmt(self, ast, param): 
        scope, func_list, rettype, inloop, func_name = param
        ltype = self.visit(ast.lhs, (scope, func_list))
        rtype = self.visit(ast.rhs, (scope, func_list))
        if type(ltype) in [VoidType, ArrayType] or not Checker.matchType(ltype, rtype):
            raise TypeMismatchInStatement(ast)
        if type(ltype) is AutoType:
            ExpUtils.infer(scope, ast.lhs.name, rtype)
            return
        if type(rtype) is AutoType:
            ExpUtils.infer(scope+[func_list], ast.rhs.name, ltype)
            return
        return

    def visitBlockStmt(self, ast, param): 
        scope, func_list, rettype, inloop, func_name = param
        env = [[]] + scope
        for x in ast.body:
            if ExpUtils.isStmt(x):
                self.visit(x, (env, func_list, rettype, inloop, func_name)) #pass another param in visit
            else:
                env = self.visit(x, (env, func_list))

    
    def visitIfStmt(self, ast, param): 
        scope, func_list, rettype, inloop, func_name = param
        condtype = self.visit(ast.cond, (scope, func_list))
        if type(condtype) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.tstmt, param)
        if ast.fstmt: 
            self.visit(ast.fstmt, param) 
        return

    def visitForStmt(self, ast, param): 
        scope, func_list, rettype, inloop, func_name = param
        initype = self.visit(ast.init.lhs, (scope, func_list))
        if not type(initype) in [IntegerType, AutoType]:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.init, param)
        condtype = self.visit(ast.cond, (scope, func_list))
        uptype = self.visit(ast.upd, (scope, func_list))
        if type(uptype) is not IntegerType or type(condtype) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, (scope, func_list, rettype, True, func_name))
        return
        
    def visitWhileStmt(self, ast, param): 
        scope, func_list, rettype, inloop, func_name = param
        condtype = self.visit(ast.cond, (scope, func_list))
        if type(condtype) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, (scope, func_list, rettype, True, func_name))
        return 
    
    def visitDoWhileStmt(self, ast, param): 
        scope, func_list, rettype, inloop, func_name = param
        self.visit(ast.stmt, (scope, func_list, rettype, True, func_name))
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
        scope, func_list, rettype, inloop, func_name = param
        if not ast.expr and not type(rettype) in [VoidType, AutoType]:
            raise TypeMismatchInStatement(ast)
        ret = self.visit(ast.expr, (scope, func_list))
        if type(rettype) is AutoType: 
            ExpUtils.infer(scope+[func_list], func_name, ret)
        elif type(ret) is not type(rettype):
            raise TypeMismatchInStatement(ast)
        return 
    
    def visitCallStmt(self, ast, param): 
        scope, func_list, rettype, inloop, func_name = param
        symbol = Checker.checkUndeclared(scope+[func_list], ast.name, Function())
        if type(symbol.kind) is not Function:
            raise TypeMismatchInStatement(ast)
        if len(ast.args) != len(symbol.type.partype):
            raise TypeMismatchInStatement(ast)
        for i in range(len(ast.args)):
            para = self.visit(ast.args[i], (scope, func_list))
            if not Checker.matchType(symbol.type.partype[i].type, para):
                raise TypeMismatchInStatement(ast)
            if type(symbol.type.partype[i].type) is AutoType:
                ExpUtils.infer([symbol.type.partype], symbol.type.partype[i].name, para)
            if type(para) is AutoType:
                ExpUtils.infer(scope+[func_list], ast.args[i].name, symbol.type.partype[i].type)
        return symbol.type.rettype
    

    # Expressions
    def visitBinExpr(self, ast: BinExpr, param): 
        scope, func_list = param
        ltype = self.visit(ast.left, param)
        rtype = self.visit(ast.right, param)
        op = ast.op
        if ExpUtils.isOpForNumber(op):
            if ExpUtils.isNaN(ltype) or ExpUtils.isNaN(rtype):
                if op in ['==', '!=']:
                    if type(ltype) is not BooleanType and type(rtype) is not BooleanType:
                        raise TypeMismatchInExpression(ast)
                    if type(ltype) is BooleanType:
                        if type(rtype) is AutoType:
                            return ExpUtils.infer(scope, ast.right.name, BooleanType())
                        if type(rtype) in [BooleanType, IntegerType]: 
                            return BooleanType()
                    if type(ltype) is AutoType:
                        return ExpUtils.infer(scope, ast.left.name, BooleanType())
                    if type(ltype) is IntegerType:
                        return BooleanType()
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
        scope, func_list = param
        arrtype = self.visit(Id(ast.name), param)
        exp_list = [self.visit(x, param) for x in ast.cell]
        if len(arrtype.dimensions) != len(exp_list):
            raise TypeMismatchInExpression(ast)
        for i in range(len(exp_list)):
            if type(exp_list[i]) is AutoType:
                ExpUtils.infer(scope+[func_list], ast.cell[i].name, IntegerType())
            elif  type(exp_list[i]) is not IntegerType:
                raise TypeMismatchInExpression(ast)
        return arrtype.typ

    def visitFuncCall(self, ast: FuncCall, param): 
        scope, func_list = param
        symbol = self.handleCall(ast, (scope,func_list), Function(), 'FuncCall')
        if type(symbol.type.rettype) is VoidType:
            raise TypeMismatchInExpression(ast)
        return symbol.type.rettype

    def handleCall(self, ast, scope, kind, typ):
        env, func_list = scope
        symbol = Checker.checkUndeclared(env+[func_list], ast.name, kind)
        if type(symbol.kind) is not Function:
            raise TypeMismatchInExpression(ast)
        params = [self.visit(x, (env, func_list)) for x in ast.args]
        args = [x.type for x in symbol.type.partype]
        if not Checker.checkParamType(args, params):
            raise TypeMismatchInExpression(ast) if typ == 'FuncCall' else TypeMismatchInStatement(ast)
        return symbol

    # param is list of params from parent func
    def handleSuper(self, ast, param, params):
        if ast.name == 'preventDefault':
            if len(ast.args) > 0:
                raise TypeMismatchInExpression(ast.args[0])
            return 
        if len(ast.args) > len(param):
            raise TypeMismatchInExpression(ast.args[len(param)])
        if len(ast.args) < len(param):
            raise TypeMismatchInExpression()
        for i in range(len(ast.args)):
            symbol = self.visit(ast.args[i], params)
            if AutoType in [type(symbol), type(param[i].type)]:
                continue
            if type(symbol) is not type(param[i].type):
                raise TypeMismatchInExpression(ast.args[i])
        return 1
            
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
        try:
            exp_list = [self.visit(x, param) for x in ast.explist]
        except IllegalArrayLiteral:
            raise IllegalArrayLiteral(ast)
        for i in range(len(exp_list)-1):
            if type(exp_list[i]) is not type(exp_list[i+1]):
                raise IllegalArrayLiteral(ast)
        typ = exp_list[0]
        dimen = [0] if type(typ) in [IntegerType, StringType, FloatType, BooleanType] else exp_list[0].dimensions + [0]
        while not type(typ) in [IntegerType, StringType, FloatType, BooleanType]:
            typ = typ.typ
        return ArrayType(dimen, typ)
            
