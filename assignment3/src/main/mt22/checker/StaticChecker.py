from StaticError import *
from Utils import Utils
from Visitor import *
from AST import *


class StaticChecker(Visitor):
    pass

    

    # Visit literal => return corresponding type
    def visitIntLit(self, ctx, o):
        return IntegerType()
    
    def visitFloatLit(self, ctx, o):
        return FloatType()
    
    def visitBoolLit(self, ctx, o):
        return BooleanType()
    
    def visitStringLit(self, ctx, o):
        return StringType()
        