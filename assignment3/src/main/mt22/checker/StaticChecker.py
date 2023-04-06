from StaticError import *
from Utils import Utils
from Visitor import *
from AST import *
from functools import reduce

class FuncType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class ExpUtils:
    @staticmethod
    def isNaN(expType):
        return type(expType) not in [IntegerType, FloatType]
    
    @staticmethod
    def isOpForInt(op):
        return op in ['+', '-', '*', '/', '%', '!=', '==', '>', '<', '>=', '<=']

    @staticmethod
    def isOpForFloat(op):
        return op in ['+', '-', '*', '/', '!=', '==', '>', '<', '>=', '<=']

    @staticmethod
    def mergeNumType(ltype, rtype):
        return FloatType() if FloatType in [type(x) for x in [ltype, rtype]] else IntegerType()

class Symbol:
    def __init__(self, name, type, value=None, kind=Function(), isGlobal=False):
        self.name = name
        self.type = type
        self.value = value
        self.kind = kind
        self.isGlobal = isGlobal

    def getKind(self):
        return self.kind if type(self.type) is FuncType else Identifier()

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
        return Symbol(decl.name, FuncType(paramsType, decl.return_type), kind=Function())
    
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
    #     Symbol('readInteger', FuncType([], IntegerType())),
    #     Symbol('printInteger', FuncType([IntegerType()], VoidType())),
    #     Symbol('readFloat', FuncType([], FloatType())),
    #     Symbol('writeFloat', FuncType([FloatType()], VoidType())),
    #     Symbol('readBoolean', FuncType([], BooleanType())),
    #     Symbol('printBoolean', FuncType([BooleanType()], VoidType())),
    #     Symbol('readString', FuncType([], StringType())),
    #     Symbol('printString', FuncType([StringType()], VoidType())),
    #     # Symbol('super', FuncType([IntegerType()], VoidType())),
    # ]]

    def visitProgram(self, ast, param): 
        env = [[
            Symbol('readInteger', FuncType([], IntegerType())),
            Symbol('printInteger', FuncType([IntegerType()], VoidType())),
            Symbol('readFloat', FuncType([], FloatType())),
            Symbol('writeFloat', FuncType([FloatType()], VoidType())),
            Symbol('readBoolean', FuncType([], BooleanType())),
            Symbol('printBoolean', FuncType([BooleanType()], VoidType())),
            Symbol('readString', FuncType([], StringType())),
            Symbol('printString', FuncType([StringType()], VoidType())),
            # Symbol('super', FuncType([IntegerType()], VoidType())),
        ]]
        for decl in ast.decls:
            env = self.visit(decl, env)

    def visitVarDecl(self, ast, param): 
        return Checker.checkRedeclared(param, [Symbol.fromVarDecl(ast)])
    
    def visitFuncDecl(self, ast, param): 
        return 

    def visitParamDecl(self, ast, param): 
        return 

    # Visit literal => return corresponding type
    def visitIntegerLit(self, ast, param): 
        return IntegerType()
    
    def visitFloatLit(self, ast, param): 
        return FloatType()
    
    def visitBooleanLit(self, ast, param): 
        return BooleanType()
    
    def visitStringLit(self, ast, param): 
        return StringType()
        