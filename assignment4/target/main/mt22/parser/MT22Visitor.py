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


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_else_stmt.
    def visitIf_else_stmt(self, ctx:MT22Parser.If_else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#other_stmt.
    def visitOther_stmt(self, ctx:MT22Parser.Other_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stat.
    def visitBlock_stat(self, ctx:MT22Parser.Block_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_element.
    def visitList_element(self, ctx:MT22Parser.List_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_ops.
    def visitAssign_ops(self, ctx:MT22Parser.Assign_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
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


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_expr.
    def visitRelational_expr(self, ctx:MT22Parser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_expr.
    def visitLogical_expr(self, ctx:MT22Parser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#adding_expr.
    def visitAdding_expr(self, ctx:MT22Parser.Adding_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplying_expr.
    def visitMultiplying_expr(self, ctx:MT22Parser.Multiplying_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unary_logical_expr.
    def visitUnary_logical_expr(self, ctx:MT22Parser.Unary_logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unary_sign_expr.
    def visitUnary_sign_expr(self, ctx:MT22Parser.Unary_sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parent_expr.
    def visitParent_expr(self, ctx:MT22Parser.Parent_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_operator.
    def visitIndex_operator(self, ctx:MT22Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_call.
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_access.
    def visitArray_access(self, ctx:MT22Parser.Array_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_expr.
    def visitList_expr(self, ctx:MT22Parser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#next_expr.
    def visitNext_expr(self, ctx:MT22Parser.Next_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_declaration.
    def visitFunction_declaration(self, ctx:MT22Parser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_parameter.
    def visitList_parameter(self, ctx:MT22Parser.List_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#next_parameter.
    def visitNext_parameter(self, ctx:MT22Parser.Next_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variable_decl.
    def visitVariable_decl(self, ctx:MT22Parser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#full_variable.
    def visitFull_variable(self, ctx:MT22Parser.Full_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#next_variable.
    def visitNext_variable(self, ctx:MT22Parser.Next_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variable.
    def visitVariable(self, ctx:MT22Parser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idList.
    def visitIdList(self, ctx:MT22Parser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#next_id.
    def visitNext_id(self, ctx:MT22Parser.Next_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_type.
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_type.
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_type.
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_integer.
    def visitList_integer(self, ctx:MT22Parser.List_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#next_integerlit.
    def visitNext_integerlit(self, ctx:MT22Parser.Next_integerlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#void_type.
    def visitVoid_type(self, ctx:MT22Parser.Void_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#auto_type.
    def visitAuto_type(self, ctx:MT22Parser.Auto_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_elements.
    def visitArray_elements(self, ctx:MT22Parser.Array_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#next_elements.
    def visitNext_elements(self, ctx:MT22Parser.Next_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#element.
    def visitElement(self, ctx:MT22Parser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boollit.
    def visitBoollit(self, ctx:MT22Parser.BoollitContext):
        return self.visitChildren(ctx)



del MT22Parser