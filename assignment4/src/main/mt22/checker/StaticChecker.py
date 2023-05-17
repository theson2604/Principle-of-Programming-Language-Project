from abc import ABC
from Visitor import Visitor
from StaticError import *
from AST import *
from functools import reduce
import copy

class SuperType(Type):
    def __init__(self, exprs: List[Expr]):
        self.list_exprs = exprs
    
DEFAULT_FUNCTIONS = [
    {
        "name": "readInteger",
        "param_type": [],
        "return_type": IntegerType(),
    },
    {
        "name": "printInteger",
        "param_type": [IntegerType()],
        "return_type": VoidType(),
    },
    {
        "name": "readFloat",
        "param_type": [],
        "return_type": FloatType(),
    },
    {
        "name": "writeFloat",
        "param_type": [FloatType()],
        "return_type": VoidType(),
    },
    {
        "name": "printBoolean",
        "param_type": [BooleanType()],
        "return_type": VoidType(),
    },
    {
        "name": "readString",
        "param_type": [VoidType()],
        "return_type": StringType(),
    },
    {
        "name": "printString",
        "param_type": [StringType()],
        "return_type": VoidType(),
    },
    {
        "name": "super",
        "param_type": [SuperType([])],
        "return_type": VoidType(),
    },
    {
        "name": "preventDefault",
        "param_type": [],
        "return_type": VoidType(),
    },
]

class StackSymbolTable:
    def __init__(self):
        self.scope = [Scope()]
        self.list_function_prototypes = []
        self.in_loop = False
        self.func_decl = None
        self.inherit_func = None
        self.func_return = False
        self.firstStmt = True
        self.inStmt = False
        self.storeArrayLit = None
        self.inFuncCall = False
    
    def initializeAScope(self):
        self.scope = [Scope()] + self.scope
        return self
    
    def pushFunction(self, funcdecl:FuncDecl):
        self.list_function_prototypes = [funcdecl]+self.list_function_prototypes
        return self
    
    def pushFunctions(self, funcdecl:List[FuncDecl]):
        self.list_function_prototypes = funcdecl[::-1]+self.list_function_prototypes
        return self
                
    def pushRecord(self, decl):
        if type(decl) is list:
            self.scope[0].pushRecords(decl)
        else: self.scope[0].pushRecord(decl)
        return self
    
    def popAScope(self):
        self.scope = self.scope[1:]
        return self
    
   
    
    def checkUndeclaredFunc(self, func_name: str):
        for func in self.list_function_prototypes:
            if func.name == func_name:
                return func
        raise Undeclared(Function(), func_name)
    
    def checkUndeclaredID(self, decl_name):
        for scope in self.scope:
            getDecls = list(filter(lambda x : type(x) in [VarDecl,ParamDecl], scope.existName(decl_name)))
            if getDecls:
                return getDecls[0]
        raise Undeclared(Identifier(), decl_name)
    
    def checkExistWithFilter(self, name:str, decl_type):
        for idx,scope in enumerate(self.scope):
            getDecls = list(filter(lambda x : type(x) is decl_type, scope.existName(name)))
            if getDecls:
                return getDecls[0]
        return None
    
    def getByName(self, name:str):
        for scope in self.scope:
            getDecls = scope.existName(name)
            if getDecls:
                return getDecls[0]
        return None
      
    @staticmethod
    def checkANameInList(param: ParamDecl, param_decl:List[ParamDecl]):
        for eachParam in param_decl:
            if eachParam.name == param.name:
                raise Redeclared(Parameter(), param.name)
        return [param] + param_decl
    
    def checkInvalidParameter(self, param_decl: List[ParamDecl]):
        paramList = []
        for param in param_decl:
            if self.scope[0].checkRedeclared(param, True):
                raise Invalid(Parameter(), param.name)
            paramList = self.checkANameInList(param, paramList)
        self.pushRecord(paramList)
    
    def checkInvalidVariable(self, decl: VarDecl):
       
        if type(decl.typ) is AutoType and decl.init is None:
            raise Invalid(Variable(), decl.name)
        return self
    
    def checkVarAndInitType(self, var_decl: VarDecl, expType: Type):
        if type(var_decl.typ) is AutoType:
            var_decl.typ = expType
            return True
        elif type(var_decl.typ) is ArrayType and type(expType) is ArrayType:
            if not StackSymbolTable.compare2ArrayType(var_decl.typ, expType):
                if var_decl.typ.dimensions == expType.dimensions and type(var_decl.typ.typ) is FloatType and type(expType.typ) is IntegerType:
                    return True
                return False
            return True
        elif type(var_decl.typ) is not type(expType):
            if not (type(var_decl.typ) is FloatType and type(expType) is IntegerType):
                if type(expType) is AutoType:
                    if type(var_decl.init) is FuncCall:
                        func = self.checkUndeclaredFunc(var_decl.init.name)
                        func.return_type = var_decl.typ
                    elif type(var_decl.init) is ParamDecl:
                
                        param = self.checkUndeclaredID(var_decl.init.name)
                        param.typ = var_decl.typ
                    elif type(var_decl.init) is BinExpr:
                        if type(var_decl.typ) in [IntegerType, FloatType] and var_decl.init.op not in ["+","-","*","/","%"]:
                            return False
                        elif type(var_decl.typ) in [BooleanType] and var_decl.init.op not in [">",">=","<","<=","==","!=","&&", "||"]:
                            return False
                        elif type(var_decl.typ) in [StringType] and var_decl.init.op not in ["::"]:
                            return False
                    elif type(var_decl.init) is UnExpr:
                        if type(var_decl.typ) in [IntegerType, FloatType] and var_decl.init.op not in ["-"]:
                            return False
                        elif type(var_decl.typ) in [BooleanType] and var_decl.init.op not in ["!"]:
                            return False
                    return True
                return False
            else:
                return True
        else:
            return True
                
    
    def compareParamType(self, params, args, visitor, superFunc=False):
        if len(params) != len(args): return False
        for i in range(len(params)):
            typeExps = visitor.visit(args[i], self)
            if type(params[i].typ) is AutoType:
                params[i].typ = typeExps
            elif type(typeExps) is AutoType:
                if type(args[i]) is FuncCall:
                    func = self.checkUndeclaredFunc(args[i].name)
                    func.return_type = params[i].typ
                else:
            
            
                    autoParam = self.checkUndeclaredID(args[i].name)
                    autoParam.typ = params[i].typ
            else:
                if type(params[i].typ) is not type(typeExps) and not (type(params[i].typ) is FloatType and type(typeExps) is IntegerType):
                    if superFunc:
                        raise TypeMismatchInExpression(args[i])
                    return False
                
        return True           
    
    @staticmethod
    def compare2ArrayType(arr1, arr2):
        return arr1.dimensions == arr2.dimensions and type(arr1.typ) is type(arr2.typ)
    
class Scope:
    def __init__(self):
        self.list_record = []
    
    def pushRecord(self, record: Decl):
        self.checkRedeclared(record)
        # record = copy.deepcopy(record)
        self.list_record = [record] + self.list_record
        return self
    
    def pushRecords(self, records: List[Decl]):
        for record in records:
            self.checkRedeclared(record)
            # record = copy.deepcopy(record)
            self.list_record = [record] + self.list_record
        
        return self
    
    def existName(self, name: str):
        return list(filter(lambda x : x.name == name, self.list_record))

    def checkRedeclared(self, decl: Decl, out=False):
        if self.existName(decl.name):
            kind = Variable()
            if type(decl) is ParamDecl:
                kind = Parameter()
            
            if type(decl) is FuncDecl:
                kind = Function()
            if out:
                return True
            raise Redeclared(kind, decl.name)
        if out: return False
    
    def checkInvalidVariable(self, decl: VarDecl):
        if decl.typ is AutoType and decl.init == None:
            raise Invalid(Variable(), decl.name)
        return self
    
    
class StaticChecker(Visitor):
    
    def __init__(self, ast):
        self.ast = ast
        self.symbolTable = StackSymbolTable()
        default_functions = list(map(lambda x: FuncDecl(name=x["name"],return_type=x["return_type"],params=[ParamDecl("",param) for param in x["param_type"]],inherit=None,body=[]), DEFAULT_FUNCTIONS))
        self.symbolTable.pushFunctions(default_functions)
        
    def check(self):
        return self.visit(self.ast, self.symbolTable)
    
    def visitProgram(self, ast, param):
        param.pushFunctions(list(filter(lambda x: type(x) is FuncDecl,ast.decls)))
        reduce(lambda x, y: self.visit(y,x), ast.decls, param)
        check_main = param.checkExistWithFilter('main', FuncDecl)
        if not check_main or check_main.params or type(check_main.return_type) is not VoidType:
            raise NoEntryPoint()
        return []  

    def visitFuncDecl(self, ast, param):
        if not param.inFuncCall:
            param.pushRecord(ast)
        # param = param.initializeAScope()
        
        param.func_decl = ast
        if ast.inherit:
            param.inherit_func = param.checkUndeclaredFunc(ast.inherit)
            # param.pushRecord(list(filter(lambda x: x.inherit,param.inherit_func.params)))
        # param = param.pushRecord(ast.param)
        param.firstStmt = False
        param.func_return = False
        stmts = self.visit(ast.body, param)
        
        param.func_decl = None
        param.inherit_func = None
        
        # param = param.popAScope()
        
        return param
    
    def visitParamDecl(self, ast, param): pass
        
    
    def visitVarDecl(self, ast, param):
        param = param.pushRecord(ast).checkInvalidVariable(ast)
        if ast.init:
            expType = self.visit(ast.init, param)
    
            if not param.checkVarAndInitType(ast, expType):
                raise TypeMismatchInVarDecl(ast)
                
        return param

    def visitCallStmt(self, ast, param):
        # func = param.checkUndeclaredFunc(ast.name)
        func = param.getByName(ast.name)
        if func is None:
            func = param.checkUndeclaredFunc(ast.name)
        else:
            if type(func) is not FuncDecl:
                raise TypeMismatchInStatement(ast)
        # if len(ast.args) != len(func.params):
        #     raise TypeMismatchInExpression(ast)
        # typeExps = list(reduce(lambda x, y: x+[self.visit(y, param)],ast.args, []))
        flag = param.compareParamType(func.params, ast.args, self)
        if not flag:
            raise TypeMismatchInStatement(ast)
        
        # return func.return_type
        
        return param
        
    def visitReturnStmt(self, ast, param):
        if param.func_return:
            return param
        exprType = VoidType()
        if ast.expr:
            exprType = self.visit(ast.expr, param)
        if type(param.func_decl.return_type) is AutoType:
            param.func_decl.return_type = exprType
        else:
            if type(param.func_decl.return_type) is not type(exprType):
                if not (type(param.func_decl.return_type) is FloatType and type(exprType) is IntegerType):
                    raise TypeMismatchInStatement(ast)
        if not param.inStmt:
            param.func_return = True
        return param
    
    def visitContinueStmt(self, ast, param):
        if not param.in_loop:
            raise MustInLoop(ast)
        return param
    
    def visitBreakStmt(self, ast, param):
        if not param.in_loop:
            raise MustInLoop(ast)
        return param
        
    def visitDoWhileStmt(self, ast, param):
        expType = self.visit(ast.cond, param)
        if type(expType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        closeLoopState = param.in_loop
        closeStmtState = param.inStmt
        param.in_loop = True
        param.inStmt = True
        self.visit(ast.stmt, param)
        param.in_loop = closeLoopState
        param.inStmt = closeStmtState
        return param
        
    def visitWhileStmt(self, ast, param):
        expType = self.visit(ast.cond, param)
        if type(expType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        closeLoopState = param.in_loop
        closeStmtState = param.inStmt
        param.in_loop = True
        param.inStmt = True
        self.visit(ast.stmt, param)
        param.in_loop = closeLoopState
        param.inStmt = closeStmtState
        return param
    
    def visitForStmt(self, ast, param):
        initType = self.visit(ast.init.lhs, param)
        if type(initType) is AutoType:
            getLHS = param.checkUndeclaredID(ast.init.lhs.name)
            getLHS.typ = IntegerType()
        elif type(initType) is not IntegerType: raise TypeMismatchInStatement(ast)
        
        self.visit(ast.init, param)
        # initRhsType = self.visit(ast.init.rhs, param)
        # if type(initRhsType) is AutoType:
        #     if type(ast.init.rhs) is Id:
        #         par = param.checkUndeclaredID(ast.init.rhs.name)
        #         par.typ = IntegerType()
            
        #     elif type(ast.init.rhs) is FuncCall:
        #         func = param.checkUndeclaredFunc(ast.init.rhs.name)
        #         func.return_type = IntegerType()
        # elif type(initRhsType) is not IntegerType: raise TypeMismatchInStatement(ast)
        
        expType = self.visit(ast.cond, param)
        if type(expType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        updType = self.visit(ast.upd, param)
        if type(updType) is not IntegerType: raise TypeMismatchInStatement(ast)
        closeLoopState = param.in_loop
        closeStmtState = param.inStmt
        param.in_loop = True
        param.inStmt = True
        self.visit(ast.stmt, param)
        param.in_loop = closeLoopState
        param.inStmt = closeStmtState
        return param
    
    def visitIfStmt(self, ast, param):
        condType = self.visit(ast.cond, param)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        closeLoopState = param.in_loop
        closeStmtState = param.inStmt
        param.in_loop = True
        param.inStmt = True
        self.visit(ast.tstmt, param)
        if ast.fstmt:
            self.visit(ast.fstmt, param)
        param.in_loop = closeLoopState
        param.inStmt = closeStmtState
        return param
        
        
    def visitBlockStmt(self, ast, param):
        param = param.initializeAScope()
        stmts = ast.body
        if not param.firstStmt:  
            # Hamdle First statement  
            if param.inherit_func:
                
                # Implicit Super hanlde
                if not len(stmts) or type(stmts[0]) is not CallStmt or stmts[0].name not in ["super", "preventDefault"]:
                    if len(param.inherit_func.params) > 0:
                        raise InvalidStatementInFunction(param.func_decl.name)
                    param.pushRecord(list(filter(lambda x: x.inherit, param.inherit_func.params)))   
                # Super handle
                elif stmts[0].name == "super":
                    firstStmt = stmts[0]
                    if len(firstStmt.args) > len(param.inherit_func.params):
                        raise TypeMismatchInExpression(firstStmt.args[len(param.inherit_func.params)])
                    elif len(firstStmt.args) < len(param.inherit_func.params):
                        raise TypeMismatchInExpression()
                    else:
                        param.compareParamType(param.inherit_func.params, firstStmt.args, self, True)
                    param.pushRecord(list(filter(lambda x: x.inherit, param.inherit_func.params)))   
                    stmts = stmts[1:]
                # preventDeafult handle
                else:
                    if len(stmts[0].args) > 0:
                        raise TypeMismatchInExpression(stmts[0].args[0])
                    stmts = stmts[1:]              
                
            # Handle parameter
            param.checkInvalidParameter(param.func_decl.params)
                
            param.firstStmt = True
            
       
        
        param = reduce(lambda x, y: self.visit(y, x), stmts, param)
        
        param = param.popAScope()
        
        return param
        
    def visitAssignStmt(self, ast, param):
        lhs = self.visit(ast.lhs, param)
        if type(lhs) in [VoidType, ArrayType]:
            raise TypeMismatchInStatement(ast)
        rhs = self.visit(ast.rhs, param)
        
        if type(lhs) is AutoType and type(rhs) is AutoType:
            pass
        elif type(lhs) is AutoType:
            getE = param.checkUndeclaredID(ast.lhs.name)
            if  type(getE) is ParamDecl:
                getE.typ = rhs
                
        elif type(rhs) is AutoType:
            if  type(ast.rhs) is Id:
                getE = param.checkUndeclaredID(ast.rhs.name)
                getE.typ = lhs
            elif type(ast.rhs) is FuncCall:
                func = param.checkUndeclaredFunc(ast.rhs.name)
                func.return_type = lhs
            elif type(ast.rhs) is BinExpr:
                if type(lhs) in [IntegerType, FloatType] and ast.rhs.op not in ["+","-","*","/","%"]:
                    raise TypeMismatchInStatement(ast)
                elif type(lhs) in [BooleanType] and ast.rhs.op not in [">",">=","<","<=","==","!=","&&", "||"]:
                    raise TypeMismatchInStatement(ast)
                elif type(lhs) in [StringType] and ast.rhs.op not in ["::"]:
                    raise TypeMismatchInStatement(ast)
            elif type(ast.rhs) is UnExpr:
                if type(lhs) in [IntegerType, FloatType] and ast.rhs.op not in ["-"]:
                    raise TypeMismatchInStatement(ast)
                elif type(lhs) in [BooleanType] and ast.rhs.op not in ["!"]:
                    raise TypeMismatchInStatement(ast)
                
        else:
            if type(lhs) is not type(rhs):
                if not(type(lhs) is FloatType and type(rhs) is IntegerType):
                    raise TypeMismatchInStatement(ast)
        return param
    


    def visitFuncCall(self, ast, param):
        func = param.getByName(ast.name)
        if func is None:
            func = param.checkUndeclaredFunc(ast.name)
        else:
            if type(func) is not FuncDecl:
                raise TypeMismatchInExpression(ast)
        # if len(ast.args) != len(func.params):
        #     raise TypeMismatchInExpression(ast)
        # typeExps = list(reduce(lambda x, y: x+[self.visit(y, param)],ast.args, []))
        
        flag = param.compareParamType(func.params, ast.args, self)
        
        if not flag:
            raise TypeMismatchInExpression(ast)
        if type(func.return_type) is AutoType:
            func_decl = param.func_decl
            inherit_func = param.inherit_func
            in_loop = param.in_loop
            func_return = param.func_return
            firstStmt = param.firstStmt
            inStmt = param.inStmt
            inFuncCall = param.inFuncCall
            param.inherit_func = None
            param.func_decl = None
            param.in_loop = False
            param.func_return = False
            param.firstStmt = True
            param.inStmt = False
            param.inFuncCall = True
            self.visit(func, param)
            param.func_decl = func_decl
            param.inherit_func = inherit_func
            param.func_decl = func_decl
            param.in_loop = in_loop
            param.func_return = func_return
            param.firstStmt = firstStmt
            param.inStmt = inStmt
            param.inFuncCall = inFuncCall
        if type(func.return_type) is VoidType:
            raise TypeMismatchInExpression(ast)
        return func.return_type
        
        
    def visitArrayLit(self, ast, param):
        keepOldArrayLit = param.storeArrayLit
        if not param.storeArrayLit:
            param.storeArrayLit = ast
        typeExps = list(reduce(lambda x, y: x+[self.visit(y, param)],ast.explist,[]))
        firstExpType = typeExps[0]
        if type(firstExpType) is ArrayType:
            for typeExp in typeExps:
                if not param.compare2ArrayType(firstExpType, typeExp):
                    raise IllegalArrayLiteral(param.storeArrayLit)
            param.storeArrayLit = keepOldArrayLit
            return ArrayType([len(typeExps)]+firstExpType.dimensions, firstExpType.typ)
        else:
            for typeExp in typeExps:
                if type(typeExp) is not type(firstExpType):
                    raise IllegalArrayLiteral(param.storeArrayLit)
            param.storeArrayLit = keepOldArrayLit
            return ArrayType([len(typeExps)], typeExp)
    
    def visitBooleanLit(self, ast, param):
        return BooleanType()
    
    def visitStringLit(self, ast, param):
        return StringType()
    
    def visitFloatLit(self, ast, param):
        return FloatType()
    
    def visitIntegerLit(self, ast, param):
        return IntegerType()
    
    def visitArrayCell(self, ast, param):
        arr = param.checkUndeclaredID(ast.name)
        if type(arr.typ)is not ArrayType:
            raise TypeMismatchInExpression(ast)
            
        if len(ast.cell) > len(arr.typ.dimensions):
            raise TypeMismatchInExpression(ast)
        
        # first_int = self.visit(ast.cell[0], param)
        # check_list_int = map(lambda x,y : type(self.visit(y, param)) is IntegerType), ast.cell)
        
        # if not check_list_int:
        #     raise TypeMismatchInExpression(ast)
        for idx in ast.cell:
            expType = self.visit(idx, param)
            if type(expType) is AutoType:
                if  type(idx) is Id:
                    getE = param.checkUndeclaredID(idx.name)
                    getE.typ = IntegerType()
                elif type(idx) is FuncCall:
                    func = param.checkUndeclaredFunc(idx.name)
                    func.return_type = IntegerType()
            elif type(expType) is not IntegerType:
                raise TypeMismatchInExpression(idx)
        
        
        
        remainder = len(ast.cell)
        return ArrayType(arr.typ.dimensions[remainder:],arr.typ.typ) if remainder < len(arr.typ.dimensions) else arr.typ.typ
        
        
        
    def visitId(self, ast, param):

        decl = param.checkUndeclaredID(ast.name)
        
        return decl.typ
        
    def visitUnExpr(self, ast, param):
        e = self.visit(ast.val, param)
        
        if ast.op == "-":
            if type(e) is AutoType:
                pass
            elif type(e) not in [FloatType, IntegerType]:
                raise TypeMismatchInExpression(ast) 

            return e
            
        
        if ast.op == "!":
            if type(e) is AutoType:
                pass
            elif type(e) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            
            return e 
       
        
    def visitBinExpr(self, ast, param):
        e1 = self.visit(ast.left,param)
        e2 = self.visit(ast.right,param)
        
        if type(e1) is AutoType and type(e2) is AutoType:
                return AutoType()
        elif type(e1) is AutoType:
            e1 = e2
            if  type(ast.left) is Id:
                # Sure, ParamDecl
                getE1 = param.checkUndeclaredID(ast.left.name)
                getE1.typ = e2
                
            else:
                # Sure FuncDecl
                func = param.checkUndeclaredFunc(ast.left.name)
                func.return_type = e2
        elif type(e2) is AutoType:
            e2 = e1
            if  type(ast.right) is Id:
                getE2 = param.checkUndeclaredID(ast.right.name)
                getE2.typ = e1
            else:
                func = param.checkUndeclaredFunc(ast.right.name)
                func.return_type = e1
        
        
        
        if ast.op in ["+","-","*","/"]:
            
                
            if type(e1) not in [IntegerType, FloatType] or type(e2) not in [IntegerType, FloatType]:
                raise TypeMismatchInExpression(ast)
            
            if type(e1) is FloatType or type(e2) is FloatType:
                return FloatType()
            return IntegerType()
        
        elif ast.op == "%":
            if type(e1) is not IntegerType or type(e2) is not IntegerType:
                raise TypeMismatchInExpression(ast)
            return IntegerType()
        
        elif ast.op in [">",">=","<","<=","==","!="]:
            
            if ast.op in ["==", "!="]:
                if type(e1) not in [IntegerType, BooleanType] or type(e2) not in [IntegerType, BooleanType]:
                    raise TypeMismatchInExpression(ast)
                
            if ast.op in [">",">=","<","<="]:
                if type(e1) not in [IntegerType, FloatType] or type(e2) not in [IntegerType, FloatType]:
                    raise TypeMismatchInExpression(ast)
                
            return BooleanType()
        
        
        elif ast.op in ["&&", "||"]:
            if type(e1) is not BooleanType or type(e2) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            
            return BooleanType()
        
        else:
            if type(e1) is not StringType or type(e2) is not StringType:
                raise TypeMismatchInExpression(ast)
            
            return StringType()
        


    def visitVoidType(self, ast, param): return self
    def visitAutoType(self, ast, param): return self
    def visitArrayType(self, ast, param): return self
    def visitStringType(self, ast, param): return self
    def visitBooleanType(self, ast, param): return self
    def visitFloatType(self, ast, param): return self
    def visitIntegerType(self, ast, param): return self
