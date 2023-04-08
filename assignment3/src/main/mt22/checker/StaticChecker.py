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
    
    @staticmethod
    def isNaN(expType):
        return type(expType) not in [IntegerType, FloatType, AutoType]
    
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
    def checkRedeclared(curScope, symbol_list):
        newScope = curScope.copy()
        for x in symbol_list:
            f = Checker.utils.lookup(x.name, newScope, Symbol.cmp)
            if f is not None:
                raise Redeclared(x.kind, x.name)
            newScope.append(x)
        return newScope
    
    @staticmethod
    def checkUndeclared(visibleScope, name, kind, notGlobal=False):
        scope = visibleScope if not notGlobal else [x for x in visibleScope if not x.isGlobal]
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
            # if Checker.isStopTypeStatement()
            pass

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
    # global_env = [[
    #     Symbol('readInteger', MType([], IntegerType())),
    #     Symbol('printInteger', MType([IntegerType()], VoidType())),
    #     Symbol('readFloat', MType([], FloatType())),
    #     Symbol('writeFloat', MType([FloatType()], VoidType())),
    #     Symbol('readBoolean', MType([], BooleanType())),
    #     Symbol('printBoolean', MType([BooleanType()], VoidType())),
    #     Symbol('readString', MType([], StringType())),
    #     Symbol('printString', MType([StringType()], VoidType())),
    #     # Symbol('super', MType([IntegerType()], VoidType())),
    # ]]

    def visitProgram(self, ast, param): 
        env = [[
            Symbol('readInteger', MType([], IntegerType())),
            Symbol('printInteger', MType([IntegerType()], VoidType())),
            Symbol('readFloat', MType([], FloatType())),
            Symbol('writeFloat', MType([FloatType()], VoidType())),
            Symbol('readBoolean', MType([], BooleanType())),
            Symbol('printBoolean', MType([BooleanType()], VoidType())),
            Symbol('readString', MType([], StringType())),
            Symbol('printString', MType([StringType()], VoidType())),
            # Symbol('super', MType([IntegerType()], VoidType())),
        ]]
        for decl in ast.decls:
            env = self.visit(decl, env)

    def visitVarDecl(self, ast, param): 
        if type(ast.typ) is AutoType:
            if ast.init is None:
                raise Invalid(Variable(), ast.name)
            ast.typ = self.visit(ast.init, param)
        return Checker.checkRedeclared(param, [Symbol(ast.name, ast.typ, kind=Variable())])
    
    #missing inherit
    def visitFuncDecl(self, ast, param): 
        params_list = [self.visit(x, scope).toParam() for x in ast.params]
        env = [[params_list]] + param
        for x in self.visit(ast.body, env):
            env = self.visit(x, env)
        return [[Symbol(ast.name, MType(params_list, ast.return_type))]] + param

    def visitParamDecl(self, ast, param): 
        return Symbol(ast.name, ast.typ, inherit=True) if ast.inherit else Symbol(ast.name, ast.typ)

    #missing autotype
    def visitBinExpr(self, ast, param): 
        ltype = self.visit(ast.left, param)
        rtype = self.visit(ast.right, param)
        op = ast.op
        if ExpUtils.isOpForNumber(op):
            if ExpUtils.isNaN(ltype) or ExpUtils.isNaN(rtype):
                raise TypeMismatchInExpression(ast)
            if op in ExpUtils.isOpForInt:
                if FloatType in [type(ltype), type(rtype)]:
                    raise TypeMismatchInExpression(ast)
                if type(ltype) is AutoType:
                    ExpUtils.infer(param, ast.left.name, IntegerType())
                if type(rtype) is AutoType:
                    ExpUtils.infer(param, ast.right.name, IntegerType())
                if op == '%': 
                    return IntegerType()
                return BooleanType()
            if op in ['+','-','*']: 
                # if type(ltype) is
                return ExpUtils.mergeNumType(ltype, rtype)
            if op == '/': return FloatType()
            return BooleanType()
        if op == '::':
            if False in [type(x) is StringType for x in [ltype, rtype]]:
                raise TypeMismatchInExpression(ast)
            return StringType()
        if False in [type(x) is BooleanType for x in [ltype, rtype]]:
            raise TypeMismatchInExpression(ast)
        return BooleanType()
    
    def visitUnExpr(self, ast, param): 
        otype = self.visit(ast.val, param)
        op = ast.op
        

    # Visit literal => return corresponding type
    def visitIntegerLit(self, ast, param): 
        return IntegerType()
    
    def visitFloatLit(self, ast, param): 
        return FloatType()
    
    def visitBooleanLit(self, ast, param): 
        return BooleanType()
    
    def visitStringLit(self, ast, param): 
        return StringType()
        