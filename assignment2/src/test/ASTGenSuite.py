import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
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
        

    def test_6_var_decl(self):
        """ Test Var Declare """
        input = """
a, B, c: integer;
x, Y, Z: boolean ;
g: array [2,3] of float={{2,1,6},{4,2,1}};
"""
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(B, IntegerType)
	VarDecl(c, IntegerType)
	VarDecl(x, BooleanType)
	VarDecl(Y, BooleanType)
	VarDecl(Z, BooleanType)
	VarDecl(g, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(1), IntegerLit(6)]), ArrayLit([IntegerLit(4), IntegerLit(2), IntegerLit(1)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
        

    def test_7_func_decl(self):
        """ Test Procedure Function Declare """
        input = """
foo: function integer () {
    a: float;
    return 2;
}
"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([VarDecl(a, FloatType), ReturnStmt(IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
        

    def test_8_func_decl(self):
        """ Test Procedure Function Declare """
        input = r"""
foo: function void (x: integer){
    a, b, c: float = 3.2,4.1,6.;
    a = b + c;
    return;
}
"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(x, IntegerType)], None, BlockStmt([VarDecl(a, FloatType, FloatLit(3.2)), VarDecl(b, FloatType, FloatLit(4.1)), VarDecl(c, FloatType, FloatLit(6.0)), AssignStmt(Id(a), BinExpr(+, Id(b), Id(c))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
        

    def test_9_func_decl(self):
        """ Test Procedure Function Declare """
        input = r"""
foo: function void (x: integer, z: float, g:boolean, h: string) {
    a, b, c: float;
    p: boolean;
    q: string;
    i, j: integer;
}
"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(x, IntegerType), Param(z, FloatType), Param(g, BooleanType), Param(h, StringType)], None, BlockStmt([VarDecl(a, FloatType), VarDecl(b, FloatType), VarDecl(c, FloatType), VarDecl(p, BooleanType), VarDecl(q, StringType), VarDecl(i, IntegerType), VarDecl(j, IntegerType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))
        

    def test_10_func_decl(self):
        """ Test Procedure Function Declare """
        input = r"""
foo: function auto (
    x: integer,
    y: boolean, z: float,
    g: string, h: string,
    arr: array[2, 3] of float
)
{ 
    a, b, c: float;
    p: boolean;
    q: string;
    i, j: integer;
    ab, kc, dd: array[1,2] of integer = {{2,1}}, {{4,4}}, {{2,3}};
}
"""
        expect = """Program([
	FuncDecl(foo, AutoType, [Param(x, IntegerType), Param(y, BooleanType), Param(z, FloatType), Param(g, StringType), Param(h, StringType), Param(arr, ArrayType([2, 3], FloatType))], None, BlockStmt([VarDecl(a, FloatType), VarDecl(b, FloatType), VarDecl(c, FloatType), VarDecl(p, BooleanType), VarDecl(q, StringType), VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(ab, ArrayType([1, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(1)])])), VarDecl(kc, ArrayType([1, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(4), IntegerLit(4)])])), VarDecl(dd, ArrayType([1, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(3)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
        

    def test_11_assign(self):
        """ Test Assign Statment """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    a = 3;    
}

"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
        

    def test_12_assign(self):
        """ Test Assign Statment """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    c : integer = 3;
    a = 5;    
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([VarDecl(c, IntegerType, IntegerLit(3)), AssignStmt(Id(a), IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
        

    def test_13_assign(self):
        """ Test Assign Statment """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float,
c: integer 
) {
    a = foo(3);    
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType), Param(c, IntegerType)], None, BlockStmt([AssignStmt(Id(a), FuncCall(foo, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))
        

    def test_14_assign(self):
        """ Test Assign Statment """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : array [3,2] of boolean) {
    a = b[foo(2,4),b[1,get((a+foo(2)),a)]];
    return b;
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, ArrayType([3, 2], BooleanType))], None, BlockStmt([AssignStmt(Id(a), ArrayCell(b, [FuncCall(foo, [IntegerLit(2), IntegerLit(4)]), ArrayCell(b, [IntegerLit(1), FuncCall(get, [BinExpr(+, Id(a), FuncCall(foo, [IntegerLit(2)])), Id(a)])])])), ReturnStmt(Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))
        

    def test_15_assign(self):
        """ Test Assign Statment """
        input = r"""
main: function array [3,2] of boolean (
a : array [3] of integer,
b : array [3] of float) {
    c: array [3] of boolean = {true, false, true};
    c[3+a] = a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
}

"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, ArrayType([3], IntegerType)), Param(b, ArrayType([3], FloatType))], None, BlockStmt([VarDecl(c, ArrayType([3], BooleanType), ArrayLit([BooleanLit(True), BooleanLit(False), BooleanLit(True)])), AssignStmt(ArrayCell(c, [BinExpr(+, IntegerLit(3), Id(a))]), BinExpr(+, ArrayCell(a, [ArrayCell(b, [BinExpr(-, BinExpr(+, Id(f), ArrayCell(y, [IntegerLit(2)])), BinExpr(*, ArrayCell(h, [ArrayCell(t, [BinExpr(+, IntegerLit(5), Id(j))])]), IntegerLit(4)))])]), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
        

    def test_16_assoc(self):
        """ Test Associative """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    a = b + 2 + n + 5 - g - 9;
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(-, BinExpr(+, BinExpr(+, BinExpr(+, Id(b), IntegerLit(2)), Id(n)), IntegerLit(5)), Id(g)), IntegerLit(9)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
        

    def test_17_assoc(self):
        """ Test Associative """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    a = 3;    
    a = b + 2 + n || 4 + 5 - g && 2 - 9;
}

"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(3)), AssignStmt(Id(a), BinExpr(&&, BinExpr(||, BinExpr(+, BinExpr(+, Id(b), IntegerLit(2)), Id(n)), BinExpr(-, BinExpr(+, IntegerLit(4), IntegerLit(5)), Id(g))), BinExpr(-, IntegerLit(2), IntegerLit(9))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
        

    def test_18_assoc(self):
        """ Test Associative """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    a = 3;    
    a = b / 2 * n / 4 / 5 % g && 2 * 9 / 4 % 2;
}

"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(3)), AssignStmt(Id(a), BinExpr(&&, BinExpr(%, BinExpr(/, BinExpr(/, BinExpr(*, BinExpr(/, Id(b), IntegerLit(2)), Id(n)), IntegerLit(4)), IntegerLit(5)), Id(g)), BinExpr(%, BinExpr(/, BinExpr(*, IntegerLit(2), IntegerLit(9)), IntegerLit(4)), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
        

    def test_19_precedence(self):
        """ Test Precedence """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    a = 3;    
    a = -5 - 6 + !5 - 9 - ! -(3 + ! -5);
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(3)), AssignStmt(Id(a), BinExpr(-, BinExpr(-, BinExpr(+, BinExpr(-, UnExpr(-, IntegerLit(5)), IntegerLit(6)), UnExpr(!, IntegerLit(5))), IntegerLit(9)), UnExpr(!, UnExpr(-, BinExpr(+, IntegerLit(3), UnExpr(!, UnExpr(-, IntegerLit(5))))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))
        

    def test_20_precedence(self):
        """ Test Precedence """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    a = 3;    
    a = ! - F * G / 5 + (I - !L && N + Y || Q *  !-P) && 6 * 5 + O / !(5 % T) ;
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(3)), AssignStmt(Id(a), BinExpr(&&, BinExpr(+, BinExpr(/, BinExpr(*, UnExpr(!, UnExpr(-, Id(F))), Id(G)), IntegerLit(5)), BinExpr(||, BinExpr(&&, BinExpr(-, Id(I), UnExpr(!, Id(L))), BinExpr(+, Id(N), Id(Y))), BinExpr(*, Id(Q), UnExpr(!, UnExpr(-, Id(P)))))), BinExpr(+, BinExpr(*, IntegerLit(6), IntegerLit(5)), BinExpr(/, Id(O), UnExpr(!, BinExpr(%, IntegerLit(5), Id(T)))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
        

    def test_21_assoc(self):
        """ Test Associative """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    a = b + 3;    
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(b), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
        

    def test_22_assoc(self):
        """ Test Associative """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    a = 3;    
    a = (((5 > 6) <(6 == 5)) >= (4 + 5 > 1)) <= 1 ;
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(3)), AssignStmt(Id(a), BinExpr(<=, BinExpr(>=, BinExpr(<, BinExpr(>, IntegerLit(5), IntegerLit(6)), BinExpr(==, IntegerLit(6), IntegerLit(5))), BinExpr(>, BinExpr(+, IntegerLit(4), IntegerLit(5)), IntegerLit(1))), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
        

    def test_23_assoc(self):
        """ Test Associative """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    a = true && !3 || ----b;    
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BinExpr(&&, BooleanLit(True), UnExpr(!, IntegerLit(3))), UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, Id(b)))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
        

    def test_24_assoc(self):
        """ Test Associative """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    a = true && false || 1 > 2 + (1 && 2);
    a = 3;    
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(>, BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(False)), IntegerLit(1)), BinExpr(+, IntegerLit(2), BinExpr(&&, IntegerLit(1), IntegerLit(2))))), AssignStmt(Id(a), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
        

    def test_25_keyword(self):
        """ Test True False Keywords """
        input = r"""
main: function void (
a : integer,
b : float) {
    a = true && false || 1 > 2 *(1 && 2);
    a = 3;
    return;
}

"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(>, BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(False)), IntegerLit(1)), BinExpr(*, IntegerLit(2), BinExpr(&&, IntegerLit(1), IntegerLit(2))))), AssignStmt(Id(a), IntegerLit(3)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))
        

    def test_26_if(self):
        """ Test If Statement """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    a = true && false || 1 > 2 +(1 && 2);
    if (a == 2) ok();
    a = 3;    
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(>, BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(False)), IntegerLit(1)), BinExpr(+, IntegerLit(2), BinExpr(&&, IntegerLit(1), IntegerLit(2))))), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), CallStmt(ok, )), AssignStmt(Id(a), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
        

    def test_27_if(self):
        """ Test If Statement """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    if ((a == 1 || b) != 2 && !c)
        ok();
    a = 3;    
}

"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(!=, BinExpr(==, Id(a), BinExpr(||, IntegerLit(1), Id(b))), BinExpr(&&, IntegerLit(2), UnExpr(!, Id(c)))), CallStmt(ok, )), AssignStmt(Id(a), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
        

    def test_28_if(self):
        """ Test If Statement """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) {
    if (a == 1) {
        b : integer;
        a = 5;
        
    }
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([VarDecl(b, IntegerType), AssignStmt(Id(a), IntegerLit(5))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
        

    def test_29_if(self):
        """ Test If Statement """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) { 
    if (a == 1)
        a = 5;
    b = c + e * 2;
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(5))), AssignStmt(Id(b), BinExpr(+, Id(c), BinExpr(*, Id(e), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
        

    def test_30_if(self):
        """ Test If Statement """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) { 
    if (a == 1) 
        if (b==2)
            a = a + 1;
        else a = a -2;
    else 
    c = 3;
    b = c + e * 2;
}

"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), IfStmt(BinExpr(==, Id(b), IntegerLit(2)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(2)))), AssignStmt(Id(c), IntegerLit(3))), AssignStmt(Id(b), BinExpr(+, Id(c), BinExpr(*, Id(e), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
        

    def test_31_if(self):
        """ Test If Statement """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) { 
    if (a != 1)
        if (b > 3)
            c = 5;
    else
        e = 0;
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(!=, Id(a), IntegerLit(1)), IfStmt(BinExpr(>, Id(b), IntegerLit(3)), AssignStmt(Id(c), IntegerLit(5)), AssignStmt(Id(e), IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))
        

    def test_32_if(self):
        """ Test If Statement """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) { 
    if (a == 1) {
        if (b > 3)  c = 5;
        else d = 1;
        if (e < 4) ok();
    }
    else {
        if (h > 5) nty(); else lyo();
        g = 5;
    }
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, Id(b), IntegerLit(3)), AssignStmt(Id(c), IntegerLit(5)), AssignStmt(Id(d), IntegerLit(1))), IfStmt(BinExpr(<, Id(e), IntegerLit(4)), CallStmt(ok, ))]), BlockStmt([IfStmt(BinExpr(>, Id(h), IntegerLit(5)), CallStmt(nty, ), CallStmt(lyo, )), AssignStmt(Id(g), IntegerLit(5))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))
        

    def test_33_while(self):
        """ Test While Statment """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) { 
    while (i < 1) i = i+1;
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
        

    def test_34_while(self):
        """ Test While Statement """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) { 
    while (i < 1){
        i = i+1;
        if (i >= 1) i = i - 1;
    }
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), IfStmt(BinExpr(>=, Id(i), IntegerLit(1)), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
        

    def test_35_for(self):
        """ Test For Statment """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) { 
    for (i = 1, i< 10, i+1) {
        for (j = i, j >= 1, j-1)
            if ((i + j) % 2 == 1) break;
    }
    
}
"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), Id(i)), BinExpr(>=, Id(j), IntegerLit(1)), BinExpr(-, Id(j), IntegerLit(1)), IfStmt(BinExpr(==, BinExpr(%, BinExpr(+, Id(i), Id(j)), IntegerLit(2)), IntegerLit(1)), BreakStmt()))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
             

    def test_36_call(self):
        """ Test Call Statment """
        input = r"""
main: function array [3,2] of boolean (
a : integer,
b : float) { 
    foo();
    bar(1);
    nty(1, 2, 3);
    pty(hyy, dyf(), ily(123, 456, fay), jtq(gyh())) ;  
}

"""
        expect = """Program([
	FuncDecl(main, ArrayType([3, 2], BooleanType), [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([CallStmt(foo, ), CallStmt(bar, IntegerLit(1)), CallStmt(nty, IntegerLit(1), IntegerLit(2), IntegerLit(3)), CallStmt(pty, Id(hyy), FuncCall(dyf, []), FuncCall(ily, [IntegerLit(123), IntegerLit(456), Id(fay)]), FuncCall(jtq, [FuncCall(gyh, [])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
        

    def test_37_complex(self):
        """ Test Complex Code """
        input = r"""
a, b, c: float;
x, y, z: boolean;
g, h, y: integer;

nty: function float() 
{
    x, y, z: integer;
    readString();
    // This is readString()

    fs = readFloat();
    
    {
        for (i = 4, i > -6, i -1) h = 6;
        if (i > 6) return 0;
    }

    return 1;
}

q, w : integer;

hgt: function boolean() {
    a: string;
    /*
        =======================================
        Comment here
        =======================================
    */
}
"""
        expect = """Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
	VarDecl(x, BooleanType)
	VarDecl(y, BooleanType)
	VarDecl(z, BooleanType)
	VarDecl(g, IntegerType)
	VarDecl(h, IntegerType)
	VarDecl(y, IntegerType)
	FuncDecl(nty, FloatType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(z, IntegerType), CallStmt(readString, ), AssignStmt(Id(fs), FuncCall(readFloat, [])), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(4)), BinExpr(>, Id(i), UnExpr(-, IntegerLit(6))), BinExpr(-, Id(i), IntegerLit(1)), AssignStmt(Id(h), IntegerLit(6))), IfStmt(BinExpr(>, Id(i), IntegerLit(6)), ReturnStmt(IntegerLit(0)))]), ReturnStmt(IntegerLit(1))]))
	VarDecl(q, IntegerType)
	VarDecl(w, IntegerType)
	FuncDecl(hgt, BooleanType, [], None, BlockStmt([VarDecl(a, StringType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
        

    def test_38_complex(self):
        """ Test Success Code Statment """
        input = r"""
foo: function void ()
{
    a: float;
    for (i[2] = 1, i[2] <= 10, i[2] + 1) 
        for (j = i, j >= 1, j - 1)
            if ((i + j) % 2 == 1) break;
    
}
"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([VarDecl(a, FloatType), ForStmt(AssignStmt(ArrayCell(i, [IntegerLit(2)]), IntegerLit(1)), BinExpr(<=, ArrayCell(i, [IntegerLit(2)]), IntegerLit(10)), BinExpr(+, ArrayCell(i, [IntegerLit(2)]), IntegerLit(1)), ForStmt(AssignStmt(Id(j), Id(i)), BinExpr(>=, Id(j), IntegerLit(1)), BinExpr(-, Id(j), IntegerLit(1)), IfStmt(BinExpr(==, BinExpr(%, BinExpr(+, Id(i), Id(j)), IntegerLit(2)), IntegerLit(1)), BreakStmt())))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
        

    def test_39_err_delc(self):
        """ Test Missing ; """
        input = r"""
a: integer;
b: float;
c, b, m: string="hello", "hi", "32,12";
"""
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(b, FloatType)
	VarDecl(c, StringType, StringLit(hello))
	VarDecl(b, StringType, StringLit(hi))
	VarDecl(m, StringType, StringLit(32,12))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
        

    def test_40_err_delc(self):
        """ Test Missing ; """
        input = r"""
a: integer;"""
        expect = """Program([
	VarDecl(a, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
        

    def test_41_err_delc(self):
        """ Test Error : """
        input = r"""
main: function string() {
    a = " hello";
    b = "world";
    c = (a::" ")::b;
    return c;
}
"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), StringLit( hello)), AssignStmt(Id(b), StringLit(world)), AssignStmt(Id(c), BinExpr(::, BinExpr(::, Id(a), StringLit( )), Id(b))), ReturnStmt(Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))
        

    def test_42_err_delc(self):
        """ Test Error Type """
        input = r"""
a: float;
"""
        expect = """Program([
	VarDecl(a, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 342))
        

    def test_nested_whilestmts(self):
        input = r"""
            foo: function void()
            {
                while (1 < 2) { 
                    while (true)
                        something();
                        /*This is a comment*/
                }
            }
            """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, IntegerLit(1), IntegerLit(2)), BlockStmt([WhileStmt(BooleanLit(True), CallStmt(something, ))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,343))

    def test_nested_whilestmts_2(self):
        input = r"""
            foo: function integer(a:float)
            {
                while(1 < 2) while (.e2) {
                    while (true) nothing();
                }
            }
            """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, FloatType)], None, BlockStmt([WhileStmt(BinExpr(<, IntegerLit(1), IntegerLit(2)), WhileStmt(FloatLit(0.0), BlockStmt([WhileStmt(BooleanLit(True), CallStmt(nothing, ))])))]))
])"""
        self.assertTrue(TestAST.test(input,expect,344))

    def test_forstmt_downto(self):
        input = r"""
            main: function void ()
            {
                for (i = 100, i >= 1, i/2)
                {
                    {Dosomething(a,b);}
                }
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(100)), BinExpr(>=, Id(i), IntegerLit(1)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([BlockStmt([CallStmt(Dosomething, Id(a), Id(b))])]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,345))

    def test_forstmt_to(self):
        input = r"""
            foo: function void()
            {
                for (x = a[0], x<a[2], x+1)
                {
                    PrintLn("Hello");
                }
            }
            """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), ArrayCell(a, [IntegerLit(0)])), BinExpr(<, Id(x), ArrayCell(a, [IntegerLit(2)])), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([CallStmt(PrintLn, StringLit(Hello))]))]))
])""" 
        self.assertTrue(TestAST.test(input,expect,346))

    def test_forstmt_to_47(self):
        input = r"""
            foo: function void()
            {
                for (x = - 1,  x != b[2], x * 3) {
                    PrintLn("Hello");
                }
            }
            """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), UnExpr(-, IntegerLit(1))), BinExpr(!=, Id(x), ArrayCell(b, [IntegerLit(2)])), BinExpr(*, Id(x), IntegerLit(3)), BlockStmt([CallStmt(PrintLn, StringLit(Hello))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,347))

    def test_nested_forstmts_48(self):
        input = r"""
            foo: function void()
            {
                for (x = -2,  x < b[2], x -3)
                    for (y = -.3e-5, y < x, y*1.5)
                    {
                        a();
                        b();
                    }
            }
            """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), UnExpr(-, IntegerLit(2))), BinExpr(<, Id(x), ArrayCell(b, [IntegerLit(2)])), BinExpr(-, Id(x), IntegerLit(3)), ForStmt(AssignStmt(Id(y), UnExpr(-, FloatLit(3e-06))), BinExpr(<, Id(y), Id(x)), BinExpr(*, Id(y), FloatLit(1.5)), BlockStmt([CallStmt(a, ), CallStmt(b, )])))]))
])"""
        self.assertTrue(TestAST.test(input,expect,348))

    def test_nested_forstmts_349(self):
        input = r"""
            foo: function void()
            {
                for (x = -2,  x < b[2], x -3)
                {
                    for (y = -.e-5, y < x, y*1.5)
                    {
                        a();
                        b();
                        for (_ = 1.0, _ == 2.0, (a*b))
                            x = !attr[true];
                    }
                }
            }
            """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), UnExpr(-, IntegerLit(2))), BinExpr(<, Id(x), ArrayCell(b, [IntegerLit(2)])), BinExpr(-, Id(x), IntegerLit(3)), BlockStmt([ForStmt(AssignStmt(Id(y), UnExpr(-, FloatLit(0.0))), BinExpr(<, Id(y), Id(x)), BinExpr(*, Id(y), FloatLit(1.5)), BlockStmt([CallStmt(a, ), CallStmt(b, ), ForStmt(AssignStmt(Id(_), FloatLit(1.0)), BinExpr(==, Id(_), FloatLit(2.0)), BinExpr(*, Id(a), Id(b)), AssignStmt(Id(x), UnExpr(!, ArrayCell(attr, [BooleanLit(True)]))))]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,349))


    def test_50_ifelse_none(self):
        input = r"""
foo: function void(){

    if (true) {} else ok();
}
"""
        expect ="""Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([]), CallStmt(ok, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_51_ifelse_none(self):
        input = r"""
foo: function void() {
    if (true){
    } else {}
}

"""
        expect ="""Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_52_assign_1lhs(self):
        input = r"""
foo: function void() {
    a = 1;    
}
"""
        expect ="""Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_53_nassign_1lhs(self):
        input = r"""
main: function void() { 
    a = 1;
    b = True;
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(b), Id(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_54_assign_nlhs(self):
        input = r"""
main: function void() {   
    b = "ahihi! hic hic";
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(b), StringLit(ahihi! hic hic))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_55_assign_lsh_arr(self):
        input = r"""
main: function void() {   
    a[5] = "ahihi! hic hic";
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(5)]), StringLit(ahihi! hic hic))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_56_assign_lhs_arr_call(self):
        input = r"""
main: function void() {
    foo[5] = 3;    
}

"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(foo, [IntegerLit(5)]), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_57_assign_complex(self):
        input = r"""
main: function void() {
    a = b[4] ;
    b[4] = foo[5] ;
    foo[5] = p;
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayCell(b, [IntegerLit(4)])), AssignStmt(ArrayCell(b, [IntegerLit(4)]), ArrayCell(foo, [IntegerLit(5)])), AssignStmt(ArrayCell(foo, [IntegerLit(5)]), Id(p))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_58_assign_complex(self):
        input = r"""
main: function void() {  
    a[1+2] = foo(bar(), "hi", 3.4, -6.5);
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2))]), FuncCall(foo, [FuncCall(bar, []), StringLit(hi), FloatLit(3.4), UnExpr(-, FloatLit(6.5))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_59_assign_complex(self):
        input = r"""
main: function void() {   
    a[1+2] = foo(bar(), .3e2, 3.4, -6.5);
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2))]), FuncCall(foo, [FuncCall(bar, []), FloatLit(30.0), FloatLit(3.4), UnExpr(-, FloatLit(6.5))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_60_assign_complex(self):
        input = r"""
main: function void() {  
    a = -1.2+4.6*6%7+m-f*k>4+2*5-6/abc- - -4 || 3 && true;
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(>, BinExpr(-, BinExpr(+, BinExpr(+, UnExpr(-, FloatLit(1.2)), BinExpr(%, BinExpr(*, FloatLit(4.6), IntegerLit(6)), IntegerLit(7))), Id(m)), BinExpr(*, Id(f), Id(k))), BinExpr(&&, BinExpr(||, BinExpr(-, BinExpr(-, BinExpr(+, IntegerLit(4), BinExpr(*, IntegerLit(2), IntegerLit(5))), BinExpr(/, IntegerLit(6), Id(abc))), UnExpr(-, UnExpr(-, IntegerLit(4)))), IntegerLit(3)), BooleanLit(True))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_61_assign_complex(self):
        input = r"""
main: function void() {
    a = false;
    g = -1.2+4.6*6 / 7+m-f*k>4+2*5-6 % abc - - - 4 || 3 && khj || true; 
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BooleanLit(False)), AssignStmt(Id(g), BinExpr(>, BinExpr(-, BinExpr(+, BinExpr(+, UnExpr(-, FloatLit(1.2)), BinExpr(/, BinExpr(*, FloatLit(4.6), IntegerLit(6)), IntegerLit(7))), Id(m)), BinExpr(*, Id(f), Id(k))), BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(-, BinExpr(-, BinExpr(+, IntegerLit(4), BinExpr(*, IntegerLit(2), IntegerLit(5))), BinExpr(%, IntegerLit(6), Id(abc))), UnExpr(-, UnExpr(-, IntegerLit(4)))), IntegerLit(3)), Id(khj)), BooleanLit(True))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_62_forto(self):
        input = r"""
main: function void() {
    for (i = 1, i < 11, i+1) hic();
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(11)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(hic, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_63_fordownto(self):
        input = r"""
main: function void() {
    for (i = 10, i >= 1, i-1) hic();
    
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(10)), BinExpr(>=, Id(i), IntegerLit(1)), BinExpr(-, Id(i), IntegerLit(1)), CallStmt(hic, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_64_for_exp(self):
        input = r"""
main: function void() {
    for (i = a+2*c, i < h(f+r*2), i*2) hic();    
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(+, Id(a), BinExpr(*, IntegerLit(2), Id(c)))), BinExpr(<, Id(i), FuncCall(h, [BinExpr(+, Id(f), BinExpr(*, Id(r), IntegerLit(2)))])), BinExpr(*, Id(i), IntegerLit(2)), CallStmt(hic, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_65_for_ret(self):
        input = r"""
main: function void() {   
    for (i = 1, i<10, i+2) return;
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(2)), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_66_for_none(self):
        input = r"""
main: function void() {
    for (i= 1, i < 10, i+1){}
    
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_67_for_comp(self):
        input = r"""
main: function void() {
    for (i = 1, i< 10, i + 1) {
        ok();
        a = 4;
        return;
        break;
        continue;
        return hoho;
    }
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(ok, ), AssignStmt(Id(a), IntegerLit(4)), ReturnStmt(), BreakStmt(), ContinueStmt(), ReturnStmt(Id(hoho))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_68_while_call(self):
        input = r"""
main: function void() {
    while (true) gogo();  
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), CallStmt(gogo, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_69_while_ret(self):
        input = r"""
main: function void() {
    while (true)return;    
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_70_while_none(self):
        input = r"""
main: function void() {
    while (true) {}
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_71_while_call_none(self):
        input = r"""
main: function void() {
    while (Foo()){}
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(FuncCall(Foo, []), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_72_while_comp(self):
        input = r"""
main: function void() {
    while (false ) {
        ok();
        a = 4;
        return;
        break;
        continue;
        return hoho;
    }
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(False), BlockStmt([CallStmt(ok, ), AssignStmt(Id(a), IntegerLit(4)), ReturnStmt(), BreakStmt(), ContinueStmt(), ReturnStmt(Id(hoho))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_73_n_dimen_array(self):
        input = r"""
main: function void() {
    a[1,2,3,4] = 1;   
}

"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_74(self):
        input = r"""
main: function void(
    a: array [999999999999999999999999999999999999999 , 999999999999999999999999999999999999999] of string,
    b: array [999999999999999999999999999999999999999 , 999999999999999999999999999999999999999] of string,
    c: array [999999999999999999999999999999999999999 , 999999999999999999999999999999999999999] of string, 
    d: array [999999999999999999999999999999999999999 , 999999999999999999999999999999999999999] of float
){
    return a;
}    
"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, ArrayType([999999999999999999999999999999999999999, 999999999999999999999999999999999999999], StringType)), Param(b, ArrayType([999999999999999999999999999999999999999, 999999999999999999999999999999999999999], StringType)), Param(c, ArrayType([999999999999999999999999999999999999999, 999999999999999999999999999999999999999], StringType)), Param(d, ArrayType([999999999999999999999999999999999999999, 999999999999999999999999999999999999999], FloatType))], None, BlockStmt([ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_75(self):
        input = r"""
main: function void() {
    a = a+5*f - !( -true || (a < b*"String"+"false"*false) || fgh % TYR ------ 666666 *
    ("abc" <= "xyz") ) / false % QUE + ---- false * "{{}}1e5" + 2e5;
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, BinExpr(-, BinExpr(+, Id(a), BinExpr(*, IntegerLit(5), Id(f))), BinExpr(%, BinExpr(/, UnExpr(!, BinExpr(||, BinExpr(||, UnExpr(-, BooleanLit(True)), BinExpr(<, Id(a), BinExpr(+, BinExpr(*, Id(b), StringLit(String)), BinExpr(*, StringLit(false), BooleanLit(False))))), BinExpr(-, BinExpr(%, Id(fgh), Id(TYR)), BinExpr(*, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(666666)))))), BinExpr(<=, StringLit(abc), StringLit(xyz)))))), BooleanLit(False)), Id(QUE))), BinExpr(*, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, BooleanLit(False))))), StringLit({{}}1e5))), FloatLit(200000.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_76(self):
        input = r"""
main: function void() {
    a = b[1,2,get(3),4] ;
    foo[b,3,bar()] = true;   
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayCell(b, [IntegerLit(1), IntegerLit(2), FuncCall(get, [IntegerLit(3)]), IntegerLit(4)])), AssignStmt(ArrayCell(foo, [Id(b), IntegerLit(3), FuncCall(bar, [])]), BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_77(self):
        input = r"""
main: function void() {
    a = b;
    a = (((((((u)))))));
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), Id(u))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))
    def test_78_var_arr(self):
        input = r"""
a: array[1 , 2] of integer;
"""
        expect ="""Program([
	VarDecl(a, ArrayType([1, 2], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_79_var_arr_n(self):
        input = r"""
a, b, c: array[1, 2] of integer;
"""
        expect ="""Program([
	VarDecl(a, ArrayType([1, 2], IntegerType))
	VarDecl(b, ArrayType([1, 2], IntegerType))
	VarDecl(c, ArrayType([1, 2], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_80_var_arr_nlist(self):
        input = r"""
a: array[1,2] of integer;
    u, v: array[1,2] of float;
"""
        expect ="""Program([
	VarDecl(a, ArrayType([1, 2], IntegerType))
	VarDecl(u, ArrayType([1, 2], FloatType))
	VarDecl(v, ArrayType([1, 2], FloatType))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_81_var_complex(self):
        input = r"""
main: function void(
    x: integer,
    y: float,
    g: string,
    arr_nodes: array[0 , 1000] of float
){  
    a, b, c: float;
    p: boolean;
    q: string;
    i, j: integer;
    dd: array[0 , 1000005] of boolean;
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(y, FloatType), Param(g, StringType), Param(arr_nodes, ArrayType([0, 1000], FloatType))], None, BlockStmt([VarDecl(a, FloatType), VarDecl(b, FloatType), VarDecl(c, FloatType), VarDecl(p, BooleanType), VarDecl(q, StringType), VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(dd, ArrayType([0, 1000005], BooleanType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_82_random(self):
        input = r"""
main: function void() {
    a = a[b[f+y[2]]] + 3;
    
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, ArrayCell(a, [ArrayCell(b, [BinExpr(+, Id(f), ArrayCell(y, [IntegerLit(2)]))])]), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_83_random(self):
        input = r"""
main: function void() {
    foo[3+x] = a[b[f+y[2]-h[t[5+j]] * 4]] + 3;   
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(foo, [BinExpr(+, IntegerLit(3), Id(x))]), BinExpr(+, ArrayCell(a, [ArrayCell(b, [BinExpr(-, BinExpr(+, Id(f), ArrayCell(y, [IntegerLit(2)])), BinExpr(*, ArrayCell(h, [ArrayCell(t, [BinExpr(+, IntegerLit(5), Id(j))])]), IntegerLit(4)))])]), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_84_random(self):
        input = r"""
main: function void() {
    a = ! - F * G / 5 + (I || L && N + Y || Q * ! -P) && 6 * 5 + O / ! (5 % T) ;    
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(&&, BinExpr(+, BinExpr(/, BinExpr(*, UnExpr(!, UnExpr(-, Id(F))), Id(G)), IntegerLit(5)), BinExpr(||, BinExpr(&&, BinExpr(||, Id(I), Id(L)), BinExpr(+, Id(N), Id(Y))), BinExpr(*, Id(Q), UnExpr(!, UnExpr(-, Id(P)))))), BinExpr(+, BinExpr(*, IntegerLit(6), IntegerLit(5)), BinExpr(/, Id(O), UnExpr(!, BinExpr(%, IntegerLit(5), Id(T)))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_85_random(self):
        input = r"""
main: function void() {
    a = (((5 < 6) < (6 == 5)) >= (4 + 5 > 1)) <= 1 ;   
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(<=, BinExpr(>=, BinExpr(<, BinExpr(<, IntegerLit(5), IntegerLit(6)), BinExpr(==, IntegerLit(6), IntegerLit(5))), BinExpr(>, BinExpr(+, IntegerLit(4), IntegerLit(5)), IntegerLit(1))), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_86_random(self):
        input = r"""
main: function void(a:float) {
    if (a == 1){
        if (b > 3) c = 5;
        else d = 1;
        if (e < 4)ok();
    } else {
        if (h > 5) nty(); else lyo();
        g = 5;
    }
}

"""
        expect ="""Program([
	FuncDecl(main, VoidType, [Param(a, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, Id(b), IntegerLit(3)), AssignStmt(Id(c), IntegerLit(5)), AssignStmt(Id(d), IntegerLit(1))), IfStmt(BinExpr(<, Id(e), IntegerLit(4)), CallStmt(ok, ))]), BlockStmt([IfStmt(BinExpr(>, Id(h), IntegerLit(5)), CallStmt(nty, ), CallStmt(lyo, )), AssignStmt(Id(g), IntegerLit(5))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_87_random(self):
        input = r"""
main: function void() {   
    while (i < 1){
        i = i+1;
        if (i == 1)  i = i - 1;
    }
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), IfStmt(BinExpr(==, Id(i), IntegerLit(1)), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_88_random(self):
        input = r"""
main: function void() {
    for (i[0] = 1, i[0] <= 10, i[0]+1)
        for (j[0] = i[0], j[0] >= 10, j[0]+1)
            if ((i + j) % 2 == 1) break;
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(i, [IntegerLit(0)]), IntegerLit(1)), BinExpr(<=, ArrayCell(i, [IntegerLit(0)]), IntegerLit(10)), BinExpr(+, ArrayCell(i, [IntegerLit(0)]), IntegerLit(1)), ForStmt(AssignStmt(ArrayCell(j, [IntegerLit(0)]), ArrayCell(i, [IntegerLit(0)])), BinExpr(>=, ArrayCell(j, [IntegerLit(0)]), IntegerLit(10)), BinExpr(+, ArrayCell(j, [IntegerLit(0)]), IntegerLit(1)), IfStmt(BinExpr(==, BinExpr(%, BinExpr(+, Id(i), Id(j)), IntegerLit(2)), IntegerLit(1)), BreakStmt())))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_89_random(self):
        input = r"""
main: function void() {
    a: integer;
    b, c: array [0 ,    15] of boolean;
    x, y, z: float = 3.2,2.,3e-3;
    x = y;
    
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, ArrayType([0, 15], BooleanType)), VarDecl(c, ArrayType([0, 15], BooleanType)), VarDecl(x, FloatType, FloatLit(3.2)), VarDecl(y, FloatType, FloatLit(2.0)), VarDecl(z, FloatType, FloatLit(0.003)), AssignStmt(Id(x), Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_90_random(self):
        input = r"""
a, b, c: float;
x, y, z: boolean;
g, h, y: integer;

nty: function integer(out x: integer, inherit y:integer, inherit out z:integer) {
    readLine();
    // This is readLine()
    fs = readStdin();
        for (i = 4, i >= -5, i-1) h = 6;
    if (i > 6) return 0;
    return 1;
}
q, w : integer;
main: function integer() inherit nty {
    /*
        =======================================
        Comment here
        =======================================
    */
    
}
"""
        expect ="""Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
	VarDecl(x, BooleanType)
	VarDecl(y, BooleanType)
	VarDecl(z, BooleanType)
	VarDecl(g, IntegerType)
	VarDecl(h, IntegerType)
	VarDecl(y, IntegerType)
	FuncDecl(nty, IntegerType, [OutParam(x, IntegerType), InheritParam(y, IntegerType), InheritOutParam(z, IntegerType)], None, BlockStmt([CallStmt(readLine, ), AssignStmt(Id(fs), FuncCall(readStdin, [])), ForStmt(AssignStmt(Id(i), IntegerLit(4)), BinExpr(>=, Id(i), UnExpr(-, IntegerLit(5))), BinExpr(-, Id(i), IntegerLit(1)), AssignStmt(Id(h), IntegerLit(6))), IfStmt(BinExpr(>, Id(i), IntegerLit(6)), ReturnStmt(IntegerLit(0))), ReturnStmt(IntegerLit(1))]))
	VarDecl(q, IntegerType)
	VarDecl(w, IntegerType)
	FuncDecl(main, IntegerType, [], nty, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_91_random(self):
        input = r"""
main: function void(
        a: integer,
        b: array [0 , 15] of boolean,
        x: float
    )
    {
        a = 3;
    }
         
foo: function void() {
    if (a == 1){
        if (b > 3) c = 5;
        if (e < 4) ok();
        else d = 1;
    } else {
        if (h()> 5) nty(); else lyo();
        g = 5;
    }
}
a:integer;
b:string;
f,g: float;
t,h: string;
p,q: boolean;
foo2: function void() {
    if (true ){
        hic();
        break;
        continue;
    }else return oh();
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [Param(a, IntegerType), Param(b, ArrayType([0, 15], BooleanType)), Param(x, FloatType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(3))]))
	FuncDecl(foo, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, Id(b), IntegerLit(3)), AssignStmt(Id(c), IntegerLit(5))), IfStmt(BinExpr(<, Id(e), IntegerLit(4)), CallStmt(ok, ), AssignStmt(Id(d), IntegerLit(1)))]), BlockStmt([IfStmt(BinExpr(>, FuncCall(h, []), IntegerLit(5)), CallStmt(nty, ), CallStmt(lyo, )), AssignStmt(Id(g), IntegerLit(5))]))]))
	VarDecl(a, IntegerType)
	VarDecl(b, StringType)
	VarDecl(f, FloatType)
	VarDecl(g, FloatType)
	VarDecl(t, StringType)
	VarDecl(h, StringType)
	VarDecl(p, BooleanType)
	VarDecl(q, BooleanType)
	FuncDecl(foo2, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([CallStmt(hic, ), BreakStmt(), ContinueStmt()]), ReturnStmt(FuncCall(oh, [])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_92_random(self):
        input = r"""
main: function void(
        a: integer,
        b: array [0 , 15] of boolean,
        x: float)
    {
        a = 3;
    }
          
foo: function void() {
    if (a == 1){
        if (b > 3) c = 5;
        if (e < 4) ok();
        else d = 1;
    } else {
        if (h()> 5) nty(); else lyo();
        g = 5;
    }
}

g, h, y: integer;

nty: function integer(out x: integer, inherit y:integer, inherit out z:integer) {
    readLine();
    // This is readLine()
    fs = readStdin();
        for (i = 4, i >= -5, i-1) h = 6;
    if (i > 6) return 0;
    return 1;
}
q, w : integer;
main: function integer() inherit nty {
    /*
        =======================================
        Comment here
        =======================================
    */
    
}
"""
        expect ="""Program([
	FuncDecl(main, VoidType, [Param(a, IntegerType), Param(b, ArrayType([0, 15], BooleanType)), Param(x, FloatType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(3))]))
	FuncDecl(foo, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, Id(b), IntegerLit(3)), AssignStmt(Id(c), IntegerLit(5))), IfStmt(BinExpr(<, Id(e), IntegerLit(4)), CallStmt(ok, ), AssignStmt(Id(d), IntegerLit(1)))]), BlockStmt([IfStmt(BinExpr(>, FuncCall(h, []), IntegerLit(5)), CallStmt(nty, ), CallStmt(lyo, )), AssignStmt(Id(g), IntegerLit(5))]))]))
	VarDecl(g, IntegerType)
	VarDecl(h, IntegerType)
	VarDecl(y, IntegerType)
	FuncDecl(nty, IntegerType, [OutParam(x, IntegerType), InheritParam(y, IntegerType), InheritOutParam(z, IntegerType)], None, BlockStmt([CallStmt(readLine, ), AssignStmt(Id(fs), FuncCall(readStdin, [])), ForStmt(AssignStmt(Id(i), IntegerLit(4)), BinExpr(>=, Id(i), UnExpr(-, IntegerLit(5))), BinExpr(-, Id(i), IntegerLit(1)), AssignStmt(Id(h), IntegerLit(6))), IfStmt(BinExpr(>, Id(i), IntegerLit(6)), ReturnStmt(IntegerLit(0))), ReturnStmt(IntegerLit(1))]))
	VarDecl(q, IntegerType)
	VarDecl(w, IntegerType)
	FuncDecl(main, IntegerType, [], nty, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

        
    def test_93_comment(self):
        """ Test Comment Line in Block """
        input = r"""
main: function integer ()
{
    // Line Comment
    /* Block Comment */
    return 2;
}
"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))
        

    def test_94_comment(self):
        """ Test Comment Block in Line """
        input = r"""
// Line Comment { Block Comment }
// Line Comment /* Block Comment */
    a /* Block */ : integer = /*Block */ 5;
"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(5))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
        

    def test_95_arr_subscript(self):
        """ Test Supscript Array is expression """
        input = r"""
a: array[1, 5 ] of integer;
"""
        expect = """Program([
	VarDecl(a, ArrayType([1, 5], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
        

        

    def test_96_idx_exp(self):
        """ Test Index Expression """
        input = r"""
foo: function void()
{
    a[(1+2+3)-(4+5*6/abc &&(123))]= a[(((-5)))] + a[(((-5))),a[0]] == 0;
}
"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(-, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), BinExpr(&&, BinExpr(+, IntegerLit(4), BinExpr(/, BinExpr(*, IntegerLit(5), IntegerLit(6)), Id(abc))), IntegerLit(123)))]), BinExpr(==, BinExpr(+, ArrayCell(a, [UnExpr(-, IntegerLit(5))]), ArrayCell(a, [UnExpr(-, IntegerLit(5)), ArrayCell(a, [IntegerLit(0)])])), IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_97_empty_prog(self):
        """ Test Empty Program """
        input = r"""a: integer = 3;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_98_arr_subscript(self):
        """ Test Array Subscript """
        input = r"""
main: function void(){
a[5 + (1 * 4/ 2) , 14] =3;
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(5), BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(4)), IntegerLit(2))), IntegerLit(14)]), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))
    
    def test_99_arr_subscript(self):
        """ Test Array Subscript """
        input = r""" 
a : array[1      , 14] of string;
"""
        expect = """Program([
	VarDecl(a, ArrayType([1, 14], StringType))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_100_if_else(self):
        """ Test If Else Again """
        input = r"""
abc: function integer (x: float, y:float)
{
        if (x == y)
            a= 1000;
        else
            b= 999;
    
}
"""
        expect = """Program([
	FuncDecl(abc, IntegerType, [Param(x, FloatType), Param(y, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(x), Id(y)), AssignStmt(Id(a), IntegerLit(1000)), AssignStmt(Id(b), IntegerLit(999)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))