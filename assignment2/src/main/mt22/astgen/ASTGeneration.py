from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
# from functools import reduce

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        declares = ctx.declare()
        declare_list = []
        for x in declares:
            declare = self.visit(x)
            if isinstance(declare, list):
                declare_list.extend(declare if declare else [])
            else: declare_list.append(declare)
        return Program(declare_list)
    
    def visitDeclare(self, ctx:MT22Parser.DeclareContext):
        return self.visitChildren(ctx)

    def visitVar_declare(self, ctx:MT22Parser.Var_declareContext):
        if ctx.COLON():
            id_list = self.visit(ctx.id_list())
            var_type = self.visit(ctx.types())
            return [VarDecl(x, var_type) for x in id_list]
        
        id_list = [ctx.ID().getText()]
        exp_list = [self.visit(ctx.exp())]
        mixed_list = self.visit(ctx.nextID())
        # var_type 
        for i in range(len(mixed_list)):
            if i == (len(mixed_list)-1):
                var_type = mixed_list[i]
            else:
                id_list = id_list + [mixed_list[i][0]]
                exp_list = [mixed_list[i][1]] + exp_list
        return [VarDecl(id_list[i], var_type, exp_list[i]) for i in range(len(id_list))]
        
    def visitNextID(self, ctx:MT22Parser.NextIDContext):
        if ctx.COLON():
            return [self.visit(ctx.types())]
        return [[ctx.ID().getText(), self.visit(ctx.exp())]] + self.visit(ctx.nextID())
    
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.id_list2())
        
    def visitId_list2(self, ctx:MT22Parser.Id_list2Context):
        if ctx.getChildCount() == 0:
            return []
        return [ctx.ID().getText()] + self.visit(ctx.id_list2())
    
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        return IntegerType() if ctx.INTEGER() else FloatType() if ctx.FLOAT() else BooleanType() if ctx.BOOLEAN() else StringType()
    
    # in process
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return ArrayType(self.visit(ctx.index_int()), self.visit(ctx.atomic_type()))
    
    def visitFunc_declare(self, ctx:MT22Parser.Func_declareContext):
        [_id, return_type, params] = self.visit(ctx.func_proto())
        if ctx.INHERIT():
            return FuncDecl(_id, return_type, params, ctx.ID().getText(), self.visit(ctx.func_body()))
        return FuncDecl(_id, return_type, params, ctx.INHERIT(), self.visit(ctx.func_body()))

    def visitFunc_proto(self, ctx:MT22Parser.Func_protoContext):
        return [ctx.ID().getText(), self.visit(ctx.return_type()), self.visit(ctx.params_list())] 

    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return IntegerType() if ctx.INTEGER() else FloatType() if ctx.FLOAT() else BooleanType() if ctx.BOOLEAN() else StringType() if ctx.STRING() else AutoType() if ctx.AUTO() else VoidType() if ctx.VOID() else self.visit(ctx.array_type())
    
    def visitFunc_body(self, ctx:MT22Parser.Func_bodyContext):
        return self.visit(ctx.block_stmt())
    
    def visitParam_declare(self, ctx:MT22Parser.Param_declareContext):
        if ctx.OUT(): out = True
        else: out = False
        if ctx.INHERIT(): inherit = True
        else: inherit = False
        return ParamDecl(ctx.ID().getText(), self.visit(ctx.types()), out, inherit)
                         
    def visitParams_list(self, ctx:MT22Parser.Params_listContext):
        return self.visit(ctx.params())

    def visitParams(self, ctx:MT22Parser.ParamsContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.param_declare())] + self.visit(ctx.params2())

    def visitParams2(self, ctx:MT22Parser.Params2Context):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.param_declare())] + self.visit(ctx.params2()) 

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
            return self.visit(ctx.exp1(0))
        return BinExpr(ctx.DC().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
    
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2(0))
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
        return UnExpr("!", self.visit(ctx.exp5()))

    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        return UnExpr("-", self.visit(ctx.exp6()))
    
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
        return self.visitChildren(ctx)
    
    # def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
    #     assign_lhs = ctx.assign_lhs()
    #     lhs_list = []
    #     exp = self.visit(ctx.exp())
    #     for x in assign_lhs:
    #         lhs_list = lhs_list + [self.visit(x)]
    #     return AssignStmt(lhs_list, exp)
    
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        lhs_list = self.visit(ctx.lhs_list())
        if len(lhs_list) == 1:
            lhs = lhs_list[0]
        else: lhs = lhs_list
        return AssignStmt(lhs, self.visit(ctx.exp()))

    def visitAssign_lhs(self, ctx:MT22Parser.Assign_lhsContext):
        return self.visit(ctx.scalar_var())
    
    def visitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        return Id(ctx.ID().getText()), self.visit(ctx.index())
    
    def visitLhs_list(self, ctx:MT22Parser.Lhs_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.assign_lhs())]
        return [self.visit(ctx.assign_lhs())] + self.visit(ctx.lhs_list2())

    def visitLhs_list2(self, ctx:MT22Parser.Lhs_list2Context):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.assign_lhs())] + self.visit(ctx.lhs_list2())

    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        if ctx.ELSE():
            return IfStmt(self.visit(ctx.exp_bool()), self.visit(ctx.stmt(0)), self.visit(ctx.stmt(1)))
        return IfStmt(self.visit(ctx.exp_bool()), self.visit(ctx.stmt(0)))
    
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return ForStmt(AssignStmt(self.visit(ctx.scalar_var()), self.visit(ctx.exp())), self.visit(ctx.exp_bool()), self.visit(ctx.exp_int()), self.visit(ctx.for_body()))
    
    def visitFor_body(self, ctx:MT22Parser.For_bodyContext):
        return self.visitChildren(ctx)
    
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return WhileStmt(self.visit(ctx.exp_bool()), self.visit(ctx.while_body()))
    
    def visitWhile_body(self, ctx:MT22Parser.While_bodyContext):
        return self.visitChildren(ctx)
    
    def visitDowhile_stmt(self, ctx:MT22Parser.Dowhile_stmtContext):
        return DoWhileStmt(self.visit(ctx.exp_bool()), self.visit(ctx.while_body()))
    
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return BreakStmt()
    
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return ContinueStmt()
    
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return ReturnStmt() if ctx.getChildCount() != 3 else ReturnStmt(self.visit(ctx.exp())) if ctx.exp() else ReturnStmt(self.visit(ctx.fun_call()))
                                                                                                                           
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return CallStmt(ctx.ID().getText(), self.visit(ctx.call_body()))
    
    def visitCall_body(self, ctx:MT22Parser.Call_bodyContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.exp())] + self.visit(ctx.call_body2())
    
    def visitCall_body2(self, ctx:MT22Parser.Call_body2Context):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.exp())] + self.visit(ctx.call_body2())
    
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return BlockStmt(self.visit(ctx.block_body()))
    
    def visitBlock_body(self, ctx:MT22Parser.Block_bodyContext):
        if ctx.getChildCount() == 0: return []
        return [self.visit(ctx.block_element())] + self.visit(ctx.block_body2())
    
    def visitBlock_body2(self, ctx:MT22Parser.Block_bodyContext):
        if ctx.getChildCount() == 0: return []
        return [self.visit(ctx.block_element())] + self.visit(ctx.block_body2())
    
    def visitBlock_element(self, ctx:MT22Parser.Block_elementContext):
        return self.visitChildren(ctx)
    
    def visitIndex_int(self, ctx:MT22Parser.Index_intContext):
        return self.visit(ctx.list_int())

    def visitList_int(self, ctx:MT22Parser.List_intContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INT_LIT().getText())]
        return [int(ctx.INT_LIT().getText())] + self.visit(ctx.list_int2())
    
    def visitList_int2(self, ctx:MT22Parser.List_int2Context):
        if ctx.getChildCount() == 0:
            return []
        return [int(ctx.INT_LIT().getText())] + self.visit(ctx.list_int2())

    def visitIndex(self, ctx:MT22Parser.IndexContext):
        return self.visit(ctx.list_exp_int())
    
    def visitList_exp_int(self, ctx:MT22Parser.List_exp_intContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.exp_int())]
        return [self.visit(ctx.exp_int())] + self.visit(ctx.list_exp_int2())
    
    def visitList_exp_int2(self, ctx:MT22Parser.List_exp_int2Context):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.exp_int())] + self.visit(ctx.list_exp_int2())
    
    def visitLiterals(self, ctx:MT22Parser.LiteralsContext):
        if ctx.array_lit():
            return self.visit(ctx.array_lit())
        if ctx.INT_LIT():
            return IntegerLit(int(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT():
            float_string = ctx.FLOAT_LIT().getText()
            return FloatLit(float(float_string if (float_string[1]!='e' and float_string[1]!='E') else '0'+float_string))
        if ctx.STRING_LIT():
            return StringLit(ctx.STRING_LIT().getText())
        return BooleanLit(ctx.BOOL_LIT().getText() == "true")
    
    def visitArray_lit(self, ctx:MT22Parser.Array_litContext):
        return self.visit(ctx.exp_list())
    
    def visitExp_list(self, ctx:MT22Parser.Exp_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.exp())] + self.visit(ctx.exp_list2())
    
    def visitExp_list2(self, ctx:MT22Parser.Exp_list2Context):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.exp())] + self.visit(ctx.exp_list2())