from functools import reduce

def flat(param):
    flat = 123

# def visitArrayLit(self, ast, param):
#         exp_list = [self.visit(x, param) for x in ast.explist]
#         for i in range(len(exp_list)-1):
#             if type(exp_list[i]) is not type(exp_list[i+1]):
#                 raise IllegalArrayLiteral(ast)
#         typ = exp_list[0]
#         dimen = [0] if type(typ) in [IntegerType, StringType, FloatType, BooleanType] else exp_list[0].dimensions + [0]
#         while not type(typ) in [IntegerType, StringType, FloatType, BooleanType]:
#             typ = typ.typ
#         return ArrayType(dimen, typ)


print(flat([3,3,3,3]))