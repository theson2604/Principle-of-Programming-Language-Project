from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        # print([self.visit(ctx.getChild(i)) for i in range(ctx.getChildCount())])
        return Program(reduce(lambda x,y: x + (y if isinstance(y, list) else [y]), [self.visit(ctx.getChild(i)) for i in range(ctx.getChildCount()-1)], []))
    
    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_else_stmt.
    def visitIf_else_stmt(self, ctx:MT22Parser.If_else_stmtContext):
        return IfStmt(self.visit(ctx.expr()), self.visit(ctx.statement(0)), self.visit(ctx.statement(1)) if ctx.ELSE() else None)


    # Visit a parse tree produced by MT22Parser#other_stmt.
    def visitOther_stmt(self, ctx:MT22Parser.Other_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stat.
    def visitBlock_stat(self, ctx:MT22Parser.Block_statContext):
        return BlockStmt(self.visit(ctx.list_element()))


    # Visit a parse tree produced by MT22Parser#list_element.
    def visitList_element(self, ctx:MT22Parser.List_elementContext):
        if not ctx.getChildCount(): return []
        return reduce(lambda x,y: x + (y if isinstance(y, list) else [y]), [self.visit(ctx.getChild(i)) for i in range(ctx.getChildCount())], [])


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        call_func = self.visit(ctx.function_call())
        return CallStmt(call_func.name, call_func.args)


    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.block_stat()))


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.statement()))


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return ForStmt(self.visit(ctx.assign_ops()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.statement()))


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visit(ctx.assign_ops())


    # Visit a parse tree produced by MT22Parser#assign_ops.
    def visitAssign_ops(self, ctx:MT22Parser.Assign_opsContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr()))


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.array_access())


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return BreakStmt()


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return ContinueStmt()


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return ReturnStmt(self.visit(ctx.expr()) if ctx.expr() else None)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relational_expr(0))
        left = self.visit(ctx.relational_expr(0))
        right = self.visit(ctx.relational_expr(1))
        return BinExpr(ctx.CONCAT().getText(), left, right)


    # Visit a parse tree produced by MT22Parser#relational_expr.
    def visitRelational_expr(self, ctx:MT22Parser.Relational_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logical_expr(0))
        left = self.visit(ctx.logical_expr(0))
        right = self.visit(ctx.logical_expr(1))
        if ctx.EQ():
            return BinExpr(ctx.EQ().getText(), left, right)
        elif ctx.NEQ():
            return BinExpr(ctx.NEQ().getText(), left, right)
        elif ctx.LESS():
            return BinExpr(ctx.LESS().getText(), left, right)
        elif ctx.LE():
            return BinExpr(ctx.LE().getText(), left, right)
        elif ctx.GREATER():
            return BinExpr(ctx.GREATER().getText(), left, right)
        else:
            return BinExpr(ctx.GE().getText(), left, right)


    # Visit a parse tree produced by MT22Parser#logical_expr.
    def visitLogical_expr(self, ctx:MT22Parser.Logical_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.adding_expr())
        left = self.visit(ctx.logical_expr())
        right = self.visit(ctx.adding_expr())
        if ctx.AND():
            return BinExpr(ctx.AND().getText(), left, right)
        else:
            return BinExpr(ctx.OR().getText(), left, right)


    # Visit a parse tree produced by MT22Parser#adding_expr.
    def visitAdding_expr(self, ctx:MT22Parser.Adding_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multiplying_expr())
        left = self.visit(ctx.adding_expr())
        right = self.visit(ctx.multiplying_expr())
        if ctx.PLUS():
            return BinExpr(ctx.PLUS().getText(), left, right)
        else:
            return BinExpr(ctx.MINUS().getText(), left, right)


    # Visit a parse tree produced by MT22Parser#multiplying_expr.
    def visitMultiplying_expr(self, ctx:MT22Parser.Multiplying_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unary_logical_expr())
        left = self.visit(ctx.multiplying_expr())
        right = self.visit(ctx.unary_logical_expr())
        if ctx.MULT():
            return BinExpr(ctx.MULT().getText(), left, right)
        elif ctx.DIV():
            return BinExpr(ctx.DIV().getText(), left, right)
        else:
            return BinExpr(ctx.MOD().getText(), left, right)

    # Visit a parse tree produced by MT22Parser#unary_logical_expr.
    def visitUnary_logical_expr(self, ctx:MT22Parser.Unary_logical_exprContext):
        return UnExpr(ctx.NOT().getText(),self.visit(ctx.unary_logical_expr())) if ctx.NOT() else self.visit(ctx.unary_sign_expr())


    # Visit a parse tree produced by MT22Parser#unary_sign_expr.
    def visitUnary_sign_expr(self, ctx:MT22Parser.Unary_sign_exprContext):
        return UnExpr(ctx.MINUS().getText(),self.visit(ctx.unary_sign_expr())) if ctx.MINUS() else self.visit(ctx.parent_expr())


    # Visit a parse tree produced by MT22Parser#parent_expr.
    def visitParent_expr(self, ctx:MT22Parser.Parent_exprContext):
        return self.visit(ctx.expr()) if ctx.expr() else self.visit(ctx.operand())


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return Id(ctx.ID().getText()) if ctx.ID() else self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_operator.
    def visitIndex_operator(self, ctx:MT22Parser.Index_operatorContext):
        return self.visit(ctx.list_expr())


    # Visit a parse tree produced by MT22Parser#function_call.
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        return FuncCall(ctx.ID().getText(), self.visit(ctx.list_expr()) if ctx.list_expr() else [])


    # Visit a parse tree produced by MT22Parser#array_access.
    def visitArray_access(self, ctx:MT22Parser.Array_accessContext):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.index_operator()))


    # Visit a parse tree produced by MT22Parser#list_expr.
    def visitList_expr(self, ctx:MT22Parser.List_exprContext):
        return [self.visit(ctx.expr())] + self.visit(ctx.next_expr())


    # Visit a parse tree produced by MT22Parser#next_expr.
    def visitNext_expr(self, ctx:MT22Parser.Next_exprContext):
        return [self.visit(ctx.expr())] + self.visit(ctx.next_expr()) if ctx.expr() else []


    # Visit a parse tree produced by MT22Parser#function_declaration.
    def visitFunction_declaration(self, ctx:MT22Parser.Function_declarationContext):
        return FuncDecl(ctx.ID(0).getText(), self.visit(ctx.return_type()), self.visit(ctx.list_parameter()), ctx.ID(1).getText() if ctx.INHERIT() else None, self.visit(ctx.block_stat()))


    # Visit a parse tree produced by MT22Parser#list_parameter.
    def visitList_parameter(self, ctx:MT22Parser.List_parameterContext):
        return [self.visit(ctx.parameter())] + self.visit(ctx.next_parameter()) if ctx.parameter() else []


    # Visit a parse tree produced by MT22Parser#next_parameter.
    def visitNext_parameter(self, ctx:MT22Parser.Next_parameterContext):
        return [self.visit(ctx.parameter())] + self.visit(ctx.next_parameter()) if ctx.parameter() else []


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return ParamDecl(ctx.ID().getText(), self.visit(ctx.var_type()), ctx.OUT() is not None, ctx.INHERIT() is not None)


    # Visit a parse tree produced by MT22Parser#variable_decl.
    def visitVariable_decl(self, ctx:MT22Parser.Variable_declContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#full_variable.
    def visitFull_variable(self, ctx:MT22Parser.Full_variableContext):
        get_next = self.visit(ctx.next_variable())
        idList =  [ctx.ID().getText()] + get_next[0]
        expList = [self.visit(ctx.expr())] + get_next[1]
        expList = expList[::-1]
        var_type = get_next[2]
        # print(idList)
        # print(expList)
        # print(var_type)
        return list(map(lambda x, y: VarDecl(x, var_type, y), idList, expList))


    # Visit a parse tree produced by MT22Parser#next_variable.
    def visitNext_variable(self, ctx:MT22Parser.Next_variableContext):
        if ctx.var_type():
            return [[],[],self.visit(ctx.var_type())]
        get_next = self.visit(ctx.next_variable())
        idList =  [ctx.ID().getText()] + get_next[0]
        expList = [self.visit(ctx.expr())] + get_next[1]
        var_type = get_next[2]
        return [idList, expList, var_type]


    # Visit a parse tree produced by MT22Parser#variable.
    def visitVariable(self, ctx:MT22Parser.VariableContext):
        var_type = self.visit(ctx.var_type())
        id_list = self.visit(ctx.idList())
        
        return list(map(lambda x: VarDecl(x, var_type), id_list))


    # Visit a parse tree produced by MT22Parser#idList.
    def visitIdList(self, ctx:MT22Parser.IdListContext):
        return [ctx.ID().getText()] + self.visit(ctx.next_id())


    # Visit a parse tree produced by MT22Parser#next_id.
    def visitNext_id(self, ctx:MT22Parser.Next_idContext):
        return [ctx.ID().getText()] + self.visit(ctx.next_id()) if ctx.ID() else []


    # Visit a parse tree produced by MT22Parser#var_type.
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_type.
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_type.
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        return IntegerType() if ctx.INTEGER() else FloatType() if ctx.FLOAT() else BooleanType() if ctx.BOOL() else StringType()

    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return ArrayType(self.visit(ctx.list_integer()), self.visit(ctx.atomic_type()))


    # Visit a parse tree produced by MT22Parser#list_integer.
    def visitList_integer(self, ctx:MT22Parser.List_integerContext):
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.next_integerlit())


    # Visit a parse tree produced by MT22Parser#next_integerlit.
    def visitNext_integerlit(self, ctx:MT22Parser.Next_integerlitContext):
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.next_integerlit()) if ctx.INTLIT() else []


    # Visit a parse tree produced by MT22Parser#void_type.
    def visitVoid_type(self, ctx:MT22Parser.Void_typeContext):
        return VoidType()


    # Visit a parse tree produced by MT22Parser#auto_type.
    def visitAuto_type(self, ctx:MT22Parser.Auto_typeContext):
        return AutoType()


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        
        if ctx.FLOATLIT():
            return FloatLit(float("0"+ctx.FLOATLIT().getText()))
        
        if ctx.boollit():
            return self.visit(ctx.boollit())
        
        if ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        
        if ctx.arraylit():
            return self.visit(ctx.arraylit())


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.array_elements()))


    # Visit a parse tree produced by MT22Parser#array_elements.
    def visitArray_elements(self, ctx:MT22Parser.Array_elementsContext):
        return [self.visit(ctx.element())] + self.visit(ctx.next_elements()) if ctx.element() else []


    # Visit a parse tree produced by MT22Parser#next_elements.
    def visitNext_elements(self, ctx:MT22Parser.Next_elementsContext):
        return [self.visit(ctx.element())] + self.visit(ctx.next_elements()) if ctx.element() else []


    # Visit a parse tree produced by MT22Parser#element.
    def visitElement(self, ctx:MT22Parser.ElementContext):
        return self.visit(ctx.expr()) if ctx.expr() else self.visit(ctx.arraylit())


    # Visit a parse tree produced by MT22Parser#boollit.
    def visitBoollit(self, ctx:MT22Parser.BoollitContext):
        return BooleanLit(ctx.getChild(0).getText()=="true")
