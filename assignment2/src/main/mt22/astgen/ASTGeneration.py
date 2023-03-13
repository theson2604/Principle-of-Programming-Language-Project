from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        declares = ctx.declare()
        decls = [self.visit(x) for x in declares]
        return Program(reduce(lambda x, y: x.extend(y) if isinstance(y, list) else x.append(y), decls, []))
    
    def visitDeclare(self, ctx:MT22Parser.DeclareContext):
        return self.visitChildren(ctx)

    def visitVar_declare(self, ctx:MT22Parser.Var_declareContext):
        if ctx.COLON():
            id_list = self.visit(ctx.id_list())
            var_type = self.visit(ctx.types())
            return [VarDecl(x, var_type) for x in id_list]
        
        id_list = [Id(ctx.ID().getText())]
        exp_list = [self.visit(ctx.exp())]
        mixed_list = self.visit(ctx.nextID())
        var_type
        for i in range(len(mixed_list)):
            if i == (len(mixed_list)-1):
                var_type = mixed_list[i]
            else:
                id_list = id_list + mixed_list[i][0]
                exp_list = mixed_list[i][1] + exp_list
        return [VarDecl(id_list[i], var_type, exp_list[i]) for i in range(len(id_list))]
        
    def visitNextID(self, ctx:MT22Parser.NextIDContext):
        if ctx.COLON():
            return [self.visit(ctx.types())]
        return [Id(ctx.ID().getText()), self.visit(ctx.exp())] + self.visit(ctx.nextID())
    
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.id_list2())
        
    def visitId_list2(self, ctx:MT22Parser.Id_list2Context):
        if ctx.getChildCount() == 0:
            return []
        return [Id(ctx.ID().getText())] + self.visit(ctx.id_list2())
    
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        return IntegerType() if ctx.INTEGER() else FloatType() if ctx.FLOAT() else BooleanType() if ctx.BOOLEAN() else StringType()
    
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return ArrayType(self.visit(ctx.index()), self.visit(ctx.atomic_type()))
    
    def visitFunc_declare(self, ctx:MT22Parser.Func_declareContext):
        [_id, return_type, params] = self.visit(ctx.func_proto())
        if ctx.INHERIT():
            return FuncDecl(_id, return_type, params, Id(ctx.ID().getText()), self.visit(ctx.func_body()))
        return FuncDecl(_id, return_type, params, self.visit(ctx.func_body()))

    def visitFunc_proto(self, ctx:MT22Parser.Func_protoContext):
        return [Id(ctx.ID().getText()), self.visit(ctx.return_type()), self.visit(ctx.params_list())] 

    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return IntegerType() if ctx.INTEGER() else FloatType() if ctx.FLOAT() else BooleanType() if ctx.BOOLEAN() else StringType() if ctx.STRING() else AutoType() if ctx.AUTO() else VoidType() if ctx.VOID() else self.visit(ctx.array_type())
    
    def visitFunc_body(self, ctx:MT22Parser.Func_bodyContext):
        return self.visit(ctx.block_stmt())
    
    def visitParam_declare(self, ctx:MT22Parser.Param_declareContext):
        # return [ParamDecl(Id(ctx.ID().getText()), self.visit(ctx.types()), ctx.OUT()?, ctx.INHERIT()?)]
        return
                         
    def visitParams_list(self, ctx:MT22Parser.Params_listContext):
        return self.visit(ctx.params())

    def visitParams(self, ctx:MT22Parser.ParamsContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.param_declare()) + self.visit(ctx.params2)

    def visitParams2(self, ctx:MT22Parser.Params2Context):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.param_declare()) + self.visit(ctx.params2()) 

    def visitTypes(self, ctx:MT22Parser.TypesContext):
        return IntegerType() if ctx.INTEGER() else FloatType() if ctx.FLOAT() else BooleanType() if ctx.BOOLEAN() else StringType() if ctx.STRING() else AutoType() if ctx.AUTO() else self.visit(ctx.array_type())
    
    def visitExp_bool(self, ctx:MT22Parser.Exp_boolContext):
        return self.visitChildren(ctx)

    def visitExp_int(self, ctx:MT22Parser.Exp_intContext):
        return self.visitChildren(ctx)
    
    def visitExp_float(self, ctx:MT22Parser.Exp_floatContext):
        return self.visitChildren(ctx)
    
    def visitExp_string(self, ctx:MT22Parser.Exp_stringContext):
        return self.visitChildren(ctx)
    
    def visitExp(self, ctx:MT22Parser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1())
        return BinExpr(ctx.DC().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
    
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2())
        op = "==" if ctx.EQ() else "!=" if ctx.NEQ() else ">" if ctx.GT() else "<" if ctx.LT() else ">=" if ctx.GTE() else "<="
        return BinExpr(op, self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
    
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        op = "&&" if ctx.AND() else "||"
        return BinExpr(op, self.visit(ctx.exp2()), self.visit(ctx.exp3()))
    
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        op = "+" if ctx.ADD() else "-"
        return BinExpr(op, self.visit(ctx.exp3()), self.visit(ctx.exp4()))
    
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        op = "*" if ctx.MUL() else "/" if ctx.DIV() else "%"
        return BinExpr(op, self.visit(ctx.exp4()), self.visit(ctx.exp5()))
    
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        return BinExpr("!", self.visit(ctx.exp5()))

    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        return BinExpr("-", self.visit(ctx.exp6()))
    
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operands())
        _id = self.visit(ctx.exp7())
        return ArrayCell(_id, self.visit(ctx.index()))
    
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        return self.visit(ctx.literals()) if ctx.literals() else Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.func_call()) if ctx.func_call() else self.visit(ctx.exp())
    
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        return FuncCall(Id(ctx.ID().getText()), self.visit(ctx.call_body()))

    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChidlren(ctx)