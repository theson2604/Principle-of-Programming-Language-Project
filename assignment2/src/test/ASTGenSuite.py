import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        print(expect)
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_5_var_decl(self):
        """ Test Var Declare """
        input = r"""
a, B, c: array [5,1000] of boolean ;
"""
        expect = """Program([
	VarDecl(a, ArrayType([5, 1000], BooleanType))
	VarDecl(B, ArrayType([5, 1000], BooleanType))
	VarDecl(c, ArrayType([5, 1000], BooleanType))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
        

    def test_6(self):
        input = r"""main: function integer() {
                    for (i=1, m<10, i+1) {
                        for (j = m+1, j < 100, j*3) {
                            s: integer = j + 1;
                            if(s==1) return 3;
                        }
                    }
                    return a*2;
                   }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(m), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(m), IntegerLit(1))), BinExpr(<, Id(j), IntegerLit(100)), BinExpr(*, Id(j), IntegerLit(3)), BlockStmt([VarDecl(s, IntegerType, BinExpr(+, Id(j), IntegerLit(1))), IfStmt(BinExpr(==, Id(s), IntegerLit(1)), ReturnStmt(IntegerLit(3)))]))])), ReturnStmt(BinExpr(*, Id(a), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,306))
        
    def test_7(self):
        input = r"""main: function integer() {
                    while(1) continue;
                   }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([WhileStmt(IntegerLit(1), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input,expect,307))

    def test_8(self):
        input = r"""test: function boolean() {
a: array[23,5,3] of integer;
while(true) break;
}"""
        expect = """Program([
	FuncDecl(test, BooleanType, [], None, BlockStmt([VarDecl(a, ArrayType([23, 5, 3], IntegerType)), WhileStmt(BooleanLit(True), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input,expect,308))

    def test_9(self):
        input = r"""test: function boolean(a: array[3] of integer) {
foo(3,a+1,a!=1,a[1]);
return true;
}"""
        expect = """Program([
	FuncDecl(test, BooleanType, [Param(a, ArrayType([3], IntegerType))], None, BlockStmt([CallStmt(foo, IntegerLit(3), BinExpr(+, Id(a), IntegerLit(1)), BinExpr(!=, Id(a), IntegerLit(1)), ArrayCell(a, [IntegerLit(1)])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input,expect,309))

    def test_10(self):
        input = r"""test: function boolean(a: array[3] of float) {
foo(3,a+1,a!=1,a[1],foo(a[3],true,a!=a));
return false;
}"""
        expect = """Program([
	FuncDecl(test, BooleanType, [Param(a, ArrayType([3], FloatType))], None, BlockStmt([CallStmt(foo, IntegerLit(3), BinExpr(+, Id(a), IntegerLit(1)), BinExpr(!=, Id(a), IntegerLit(1)), ArrayCell(a, [IntegerLit(1)]), FuncCall(foo, [ArrayCell(a, [IntegerLit(3)]), BooleanLit(True), BinExpr(!=, Id(a), Id(a))])), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input,expect,310))

    def test_12(self):
        input = r"""test: function boolean(a: array[3] of float) {
foo(foo(foo(foo(foo(1,3333,foo(a[3],a[0],3)))),222,a[1]),a[1]+foo(1,2,3));
return false;
}"""
        expect = """Program([
	FuncDecl(test, BooleanType, [Param(a, ArrayType([3], FloatType))], None, BlockStmt([CallStmt(foo, FuncCall(foo, [FuncCall(foo, [FuncCall(foo, [FuncCall(foo, [IntegerLit(1), IntegerLit(3333), FuncCall(foo, [ArrayCell(a, [IntegerLit(3)]), ArrayCell(a, [IntegerLit(0)]), IntegerLit(3)])])])]), IntegerLit(222), ArrayCell(a, [IntegerLit(1)])]), BinExpr(+, ArrayCell(a, [IntegerLit(1)]), FuncCall(foo, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input,expect,312))

    def test_13(self):
        input = r"""test: function boolean(a: array[3] of string) {
if (a[1] == "hello world") break;
else return a[1];
return "return";
}"""
        expect = """Program([
	FuncDecl(test, BooleanType, [Param(a, ArrayType([3], StringType))], None, BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1)]), StringLit(hello world)), BreakStmt(), ReturnStmt(ArrayCell(a, [IntegerLit(1)]))), ReturnStmt(StringLit(return))]))
])"""
        self.assertTrue(TestAST.test(input,expect,313))

    def test_14(self):
        input = r"""test: function boolean(a: array[3] of string) {
if (a[1] == "hello world") 
if (a[0] == "hello worlds")
else return a[1]
else return a[0]
return "return";
}"""
        expect = """Program([
	FuncDecl(test, BooleanType, [Param(a, ArrayType([3], StringType))], None, BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1)]), StringLit(hello world)), IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(0)]), StringLit(hello worlds)), ReturnStmt(ArrayCell(a, [IntegerLit(1)]))), ReturnStmt(ArrayCell(a, [IntegerLit(0)]))), ReturnStmt(StringLit(return))]))
])"""
        self.assertTrue(TestAST.test(input,expect,314))

    def test_15(self):
        input = r"""
        i: integer = 3;
        func: function string(){
            var: string = "test"
            return var;
        }
        test: function void(){
            a: string;
            print("hello wrodl");
            while(true) a = func()
        }

}"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(3))
	FuncDecl(func, StringType, [], None, BlockStmt([VarDecl(var, StringType, StringLit(test)), ReturnStmt(Id(var))]))
	FuncDecl(test, VoidType, [], None, BlockStmt([VarDecl(a, StringType), CallStmt(print, StringLit(hello wrodl)), WhileStmt(BooleanLit(True), AssignStmt(Id(a), FuncCall(func, [])))]))
])"""
        self.assertTrue(TestAST.test(input,expect,315))