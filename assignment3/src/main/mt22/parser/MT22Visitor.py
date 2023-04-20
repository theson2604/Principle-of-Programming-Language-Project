# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declare.
    def visitDeclare(self, ctx:MT22Parser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_declare.
    def visitVar_declare(self, ctx:MT22Parser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#nextID.
    def visitNextID(self, ctx:MT22Parser.NextIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_list.
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_list2.
    def visitId_list2(self, ctx:MT22Parser.Id_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_type.
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_declare.
    def visitFunc_declare(self, ctx:MT22Parser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_proto.
    def visitFunc_proto(self, ctx:MT22Parser.Func_protoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_type.
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_body.
    def visitFunc_body(self, ctx:MT22Parser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_declare.
    def visitParam_declare(self, ctx:MT22Parser.Param_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#params_list.
    def visitParams_list(self, ctx:MT22Parser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#params.
    def visitParams(self, ctx:MT22Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#params2.
    def visitParams2(self, ctx:MT22Parser.Params2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#types.
    def visitTypes(self, ctx:MT22Parser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_bool.
    def visitExp_bool(self, ctx:MT22Parser.Exp_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_int.
    def visitExp_int(self, ctx:MT22Parser.Exp_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_float.
    def visitExp_float(self, ctx:MT22Parser.Exp_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_string.
    def visitExp_string(self, ctx:MT22Parser.Exp_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp.
    def visitExp(self, ctx:MT22Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp2.
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp3.
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp4.
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp5.
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp6.
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operands.
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_call.
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_lhs.
    def visitAssign_lhs(self, ctx:MT22Parser.Assign_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar_var.
    def visitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs_list.
    def visitLhs_list(self, ctx:MT22Parser.Lhs_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs_list2.
    def visitLhs_list2(self, ctx:MT22Parser.Lhs_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_body.
    def visitFor_body(self, ctx:MT22Parser.For_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_body.
    def visitWhile_body(self, ctx:MT22Parser.While_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhile_stmt.
    def visitDowhile_stmt(self, ctx:MT22Parser.Dowhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_body.
    def visitCall_body(self, ctx:MT22Parser.Call_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_body2.
    def visitCall_body2(self, ctx:MT22Parser.Call_body2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_body.
    def visitBlock_body(self, ctx:MT22Parser.Block_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_body2.
    def visitBlock_body2(self, ctx:MT22Parser.Block_body2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_element.
    def visitBlock_element(self, ctx:MT22Parser.Block_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_int.
    def visitIndex_int(self, ctx:MT22Parser.Index_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_int.
    def visitList_int(self, ctx:MT22Parser.List_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_int2.
    def visitList_int2(self, ctx:MT22Parser.List_int2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index.
    def visitIndex(self, ctx:MT22Parser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_exp_int.
    def visitList_exp_int(self, ctx:MT22Parser.List_exp_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_exp_int2.
    def visitList_exp_int2(self, ctx:MT22Parser.List_exp_int2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literals.
    def visitLiterals(self, ctx:MT22Parser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_lit.
    def visitArray_lit(self, ctx:MT22Parser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list.
    def visitExp_list(self, ctx:MT22Parser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list2.
    def visitExp_list2(self, ctx:MT22Parser.Exp_list2Context):
        return self.visitChildren(ctx)



del MT22Parser