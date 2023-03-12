from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        declares = ctx.visitDeclare()
        decls = [self.visitDeclare(x) for x in declares]
        return Program(reduce(lambda x, y: x.extend(y) if isinstance(y, list) else x.append(y), decls, []))
    
    def visitDeclare(self, ctx:MT22Parser.DeclareContext):
        return self.visitChildren(ctx)

    def visitVar_declare(self, ctx:MT22Parser.Var_declareContext):
        return 