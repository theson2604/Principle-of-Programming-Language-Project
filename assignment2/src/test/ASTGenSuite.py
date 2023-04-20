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
        input = r"""var, b: boolean = false, true;
        a: float = 3.0;
        test: function boolean(a: float, b: boolean) {
test(a, b);
return true;
}
    main: function void() {
        printBoolean(var);
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
        input = r"""test: function boolean(a: array[3] of boolean) {
if (true)
if (false)
else return true;
return true;
}"""
        expect = """Program([
	FuncDecl(test, BooleanType, [Param(a, ArrayType([3], BooleanType))], None, BlockStmt([IfStmt(BooleanLit(True), IfStmt(BooleanLit(False), ReturnStmt(BooleanLit(True)))), ReturnStmt(BooleanLit(True))]))
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
            while(true) a = func();
        }

}"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(3))
	FuncDecl(func, StringType, [], None, BlockStmt([VarDecl(var, StringType, StringLit(test)), ReturnStmt(Id(var))]))
	FuncDecl(test, VoidType, [], None, BlockStmt([VarDecl(a, StringType), CallStmt(print, StringLit(hello wrodl)), WhileStmt(BooleanLit(True), AssignStmt(Id(a), FuncCall(func, [])))]))
])"""
        self.assertTrue(TestAST.test(input,expect,315))

    def test_16(self):
        input = r"""
        i: integer = 3;
        func: function void(a: integer, c: float){
            a = a + c;
            writeLn(a, "hello world");
        }

}"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(3))
	FuncDecl(func, VoidType, [Param(a, IntegerType), Param(c, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(c))), CallStmt(writeLn, Id(a), StringLit(hello world))]))
])"""
        self.assertTrue(TestAST.test(input,expect,316))
        
    def test_17(self):
        input = r"""
        i, i2, i3: integer = 3, 4, 5;
        func: function void(a: integer, c: float){
            Write("nhap so 1:");
			Readln(Num1);
			Writeln("nhap so 2:");
			Readln(Num2);
			Sum = Num1 + Num2;
			Write(Sum);
			Readln();
        }

}"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(3))
	VarDecl(i2, IntegerType, IntegerLit(4))
	VarDecl(i3, IntegerType, IntegerLit(5))
	FuncDecl(func, VoidType, [Param(a, IntegerType), Param(c, FloatType)], None, BlockStmt([CallStmt(Write, StringLit(nhap so 1:)), CallStmt(Readln, Id(Num1)), CallStmt(Writeln, StringLit(nhap so 2:)), CallStmt(Readln, Id(Num2)), AssignStmt(Id(Sum), BinExpr(+, Id(Num1), Id(Num2))), CallStmt(Write, Id(Sum)), CallStmt(Readln, )]))
])"""
        self.assertTrue(TestAST.test(input,expect,317))
        
    def test_18(self):
        input = r"""
        i, i2, i3: integer = 3, 4, 5;
        main: function integer(a: array [444, 444, 444] of string, b: array [333] of integer){
            a[b[2], b[22], b[222]] = 444;
            return a[b[2], b[22], b[222]];
        }

}"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(3))
	VarDecl(i2, IntegerType, IntegerLit(4))
	VarDecl(i3, IntegerType, IntegerLit(5))
	FuncDecl(main, IntegerType, [Param(a, ArrayType([444, 444, 444], StringType)), Param(b, ArrayType([333], IntegerType))], None, BlockStmt([AssignStmt(ArrayCell(a, [ArrayCell(b, [IntegerLit(2)]), ArrayCell(b, [IntegerLit(22)]), ArrayCell(b, [IntegerLit(222)])]), IntegerLit(444)), ReturnStmt(ArrayCell(a, [ArrayCell(b, [IntegerLit(2)]), ArrayCell(b, [IntegerLit(22)]), ArrayCell(b, [IntegerLit(222)])]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,318))
        
    def test_19(self):
        input = r"""
        main: function integer(a: array [444, 444, 444] of string, b: array [333] of integer){
            if (a[1,2,1] == b[2]) return a[3,2,b[120]];
            else {
				if (a[b[2],b[3],b[111]] == 0) foo(a[2,3,b[22]==a[b[3],3,8]]);
                else return 0;
			}
            return a[b[2], b[22], b[222]];
        }

}"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, ArrayType([444, 444, 444], StringType)), Param(b, ArrayType([333], IntegerType))], None, BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(1)]), ArrayCell(b, [IntegerLit(2)])), ReturnStmt(ArrayCell(a, [IntegerLit(3), IntegerLit(2), ArrayCell(b, [IntegerLit(120)])])), BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [ArrayCell(b, [IntegerLit(2)]), ArrayCell(b, [IntegerLit(3)]), ArrayCell(b, [IntegerLit(111)])]), IntegerLit(0)), CallStmt(foo, ArrayCell(a, [IntegerLit(2), IntegerLit(3), BinExpr(==, ArrayCell(b, [IntegerLit(22)]), ArrayCell(a, [ArrayCell(b, [IntegerLit(3)]), IntegerLit(3), IntegerLit(8)]))])), ReturnStmt(IntegerLit(0)))])), ReturnStmt(ArrayCell(a, [ArrayCell(b, [IntegerLit(2)]), ArrayCell(b, [IntegerLit(22)]), ArrayCell(b, [IntegerLit(222)])]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,319))
        
    def test_20(self):
        input = r"""
        main: function void(a: array [444, 444, 444] of string, b: array [333] of integer){
			arr: array[222] of boolean;
            i,j,k: integer = 30,21,2;
            for (a[4,j,i] = 0, i<2, i+333) {
				for (aa = 0, i<2, i+333) {
					if (a[3,3,3] <= a[b[4],i,j]) break;
                    else continue;
                }
			}
        }

}"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, ArrayType([444, 444, 444], StringType)), Param(b, ArrayType([333], IntegerType))], None, BlockStmt([VarDecl(arr, ArrayType([222], BooleanType)), VarDecl(i, IntegerType, IntegerLit(30)), VarDecl(j, IntegerType, IntegerLit(21)), VarDecl(k, IntegerType, IntegerLit(2)), ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(4), Id(j), Id(i)]), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(333)), BlockStmt([ForStmt(AssignStmt(Id(aa), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(333)), BlockStmt([IfStmt(BinExpr(<=, ArrayCell(a, [IntegerLit(3), IntegerLit(3), IntegerLit(3)]), ArrayCell(a, [ArrayCell(b, [IntegerLit(4)]), Id(i), Id(j)])), BreakStmt(), ContinueStmt())]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,320))
        
    def test_21(self):
        input = r"""
        count_x: function integer(arr: array [10] of integer, x: integer){
			count: integer = 0;
            for (i = 0, i<len(arr), i+1) {
				if (arr[i] == x) count = count + 1;
			}
            return count;
        }

}"""
        expect = """Program([
	FuncDecl(count_x, IntegerType, [Param(arr, ArrayType([10], IntegerType)), Param(x, IntegerType)], None, BlockStmt([VarDecl(count, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(arr)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(arr, [Id(i)]), Id(x)), AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1))))])), ReturnStmt(Id(count))]))
])"""
        self.assertTrue(TestAST.test(input,expect,321))
        
    def test_22(self):
        input = r"""
        sum_real_array: function float(a: array [444, 444, 444] of float, b: integer){
			i:integer; s:float = 0;
            for (i = a[3,2,b]-1, i<2, i%3333) {
				s = s + a[3,i,2];
			}
            return s;
        }
        main: function void(){
			a: array[222] of boolean;
            writeLn("Helloworld");
        }

}"""
        expect = """Program([
	FuncDecl(sum_real_array, FloatType, [Param(a, ArrayType([444, 444, 444], FloatType)), Param(b, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(s, FloatType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), BinExpr(-, ArrayCell(a, [IntegerLit(3), IntegerLit(2), Id(b)]), IntegerLit(1))), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(%, Id(i), IntegerLit(3333)), BlockStmt([AssignStmt(Id(s), BinExpr(+, Id(s), ArrayCell(a, [IntegerLit(3), Id(i), IntegerLit(2)])))])), ReturnStmt(Id(s))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([222], BooleanType)), CallStmt(writeLn, StringLit(Helloworld))]))
])"""
        self.assertTrue(TestAST.test(input,expect,322))
        
    def test_23(self):
        input = r"""
        test_input: function void(){
			i:integer; s:float = 0;
            write("input your number: ");
            readLn(i)
            for (s = .e-10, s!=0, s*s) {
				print(s);
			}
        }

}"""
        expect = """Program([
	FuncDecl(test_input, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(s, FloatType, IntegerLit(0)), CallStmt(write, StringLit(input your number: )), CallStmt(readLn, Id(i)), ForStmt(AssignStmt(Id(s), FloatLit(0.0)), BinExpr(!=, Id(s), IntegerLit(0)), BinExpr(*, Id(s), Id(s)), BlockStmt([CallStmt(print, Id(s))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,323))
        
    def test_24(self):
        input = r"""
        mod_5: function integer(arr: array [10] of integer){
			num: integer = 0;
            for (i = 0, i<len(arr), i+1) {
				if (arr[i] % 5 == 0) num = num + 1;
			}
            return num;
        }

}"""
        expect = """Program([
	FuncDecl(mod_5, IntegerType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(num, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(arr)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(i)]), IntegerLit(5)), IntegerLit(0)), AssignStmt(Id(num), BinExpr(+, Id(num), IntegerLit(1))))])), ReturnStmt(Id(num))]))
])"""
        self.assertTrue(TestAST.test(input,expect,324))
        
    def test_25(self):
        input = r"""
        sum_mod_5: function integer(arr: array [10] of integer){
			sum: integer = 0;
            for (i = 0, i<len(arr), i+1) {
				if (arr[i] % 5 == 0) sum = sum + arr[i];
			}
            return sum;
        }

}"""
        expect = """Program([
	FuncDecl(sum_mod_5, IntegerType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(arr)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(i)]), IntegerLit(5)), IntegerLit(0)), AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i)]))))])), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input,expect,325))
        
    def test_26(self):
        input = r"""
        is_prime: function boolean(num: integer){
            for (i = 2, i<sqrt(num), i+1) {
				if (num % i == 0) return false;
			}
            return true;
        }

}"""
        expect = """Program([
	FuncDecl(is_prime, BooleanType, [Param(num, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), FuncCall(sqrt, [Id(num)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(num), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input,expect,326))
        
    def test_27(self):
        input = r"""
        replace_all: function array[10] of string(arr: array [10] of string, x: string, alter: string){
            for (i = 0, i<len(arr), i+1) {
				if (arr[i] == x) arr[i] = alter;
			}
            return arr;
        }

}"""
        expect = """Program([
	FuncDecl(replace_all, ArrayType([10], StringType), [Param(arr, ArrayType([10], StringType)), Param(x, StringType), Param(alter, StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(arr)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(arr, [Id(i)]), Id(x)), AssignStmt(ArrayCell(arr, [Id(i)]), Id(alter)))])), ReturnStmt(Id(arr))]))
])"""
        self.assertTrue(TestAST.test(input,expect,327))
        
    def test_28(self):
        input = r"""
        check_increment: function boolean(arr: array [10] of integer){
			cur: integer = arr[0];
            for (i = 1, i<len(arr), i+1) {
				if (arr[i] < cur) return false;
			}
            return true;
        }

}"""
        expect = """Program([
	FuncDecl(check_increment, BooleanType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(cur, IntegerType, ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(len, [Id(arr)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(arr, [Id(i)]), Id(cur)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input,expect,328))

    def test_29(self):
        input = r"""
        x,y: float; a,b,c:integer;
        foo: function boolean(){
			x = 9.E-32;
            return true;
        }

}"""
        expect = """Program([
	VarDecl(x, FloatType)
	VarDecl(y, FloatType)
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(c, IntegerType)
	FuncDecl(foo, BooleanType, [], None, BlockStmt([AssignStmt(Id(x), FloatLit(9e-32)), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input,expect,329))        
		
    def test_30(self):
        input = r"""
        x,y: float; a,b,c:integer;
        foo: function boolean(){
			if (a == 3) {
				x = .4e-33333333;
			}
            return true;
        }

}"""
        expect = """Program([
	VarDecl(x, FloatType)
	VarDecl(y, FloatType)
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(c, IntegerType)
	FuncDecl(foo, BooleanType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), FloatLit(0.0))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input,expect,330))   
        
    def test_31(self):
        input = r"""
        x,y: float; a,b,c:integer;
        main: function boolean(){
			while (a*c+b >= x) {
				a = a + b - c * y;
			}
            return true;
        }

}"""
        expect = """Program([
	VarDecl(x, FloatType)
	VarDecl(y, FloatType)
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(c, IntegerType)
	FuncDecl(main, BooleanType, [], None, BlockStmt([WhileStmt(BinExpr(>=, BinExpr(+, BinExpr(*, Id(a), Id(c)), Id(b)), Id(x)), BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(+, Id(a), Id(b)), BinExpr(*, Id(c), Id(y))))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input,expect,331))  


    def test_32(self):
        input = r"""
        x,y: float; a,b,c:integer;
        _foo: function boolean(){
			for(x = 0, x < 20, x+1) {
				a = c+4;
			}
            return true;
        }

}"""
        expect = """Program([
	VarDecl(x, FloatType)
	VarDecl(y, FloatType)
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(c, IntegerType)
	FuncDecl(_foo, BooleanType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), IntegerLit(20)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(c), IntegerLit(4)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input,expect,332))  

    def test_33(self):
        input = r"""
        a : array [4,5,6] of integer;
        b : array [5,6,7] of float;
        c : array [5,6,7] of boolean;
        d : array [20,21,22] of string;
}"""
        expect = """Program([
	VarDecl(a, ArrayType([4, 5, 6], IntegerType))
	VarDecl(b, ArrayType([5, 6, 7], FloatType))
	VarDecl(c, ArrayType([5, 6, 7], BooleanType))
	VarDecl(d, ArrayType([20, 21, 22], StringType))
])"""
        self.assertTrue(TestAST.test(input,expect,333))  

    def test_34(self):
        input = r"""
        a : array [4,5,6] of integer;
        b : array [5,6,7] of float;
        c : array [5,6,7] of boolean;
        d : array [20,21,22] of string;
        main: function void(){
			a[3,3,3] = b[c[3,3,3],d[3,3,3],a[2,3,5]];
        }
}"""
        expect = """Program([
	VarDecl(a, ArrayType([4, 5, 6], IntegerType))
	VarDecl(b, ArrayType([5, 6, 7], FloatType))
	VarDecl(c, ArrayType([5, 6, 7], BooleanType))
	VarDecl(d, ArrayType([20, 21, 22], StringType))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(3), IntegerLit(3), IntegerLit(3)]), ArrayCell(b, [ArrayCell(c, [IntegerLit(3), IntegerLit(3), IntegerLit(3)]), ArrayCell(d, [IntegerLit(3), IntegerLit(3), IntegerLit(3)]), ArrayCell(a, [IntegerLit(2), IntegerLit(3), IntegerLit(5)])]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,334)) 

    def test_35(self):
        input = r"""
        a : array [4,5,6] of integer;
        b : array [5,6,7] of float;
        c : array [5,6,7] of boolean;
        d : array [20,21,22] of string;
        main: function void(){
			
        }
}"""
        expect = """Program([
	VarDecl(a, ArrayType([4, 5, 6], IntegerType))
	VarDecl(b, ArrayType([5, 6, 7], FloatType))
	VarDecl(c, ArrayType([5, 6, 7], BooleanType))
	VarDecl(d, ArrayType([20, 21, 22], StringType))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,335)) 


    def test_36(self):
        input = r"""
        a : array [4,5,6] of integer;
        b : array [5,6,7] of float;
        c : array [5,6,7] of boolean;
        d : array [20,21,22] of string;
        main: function void(){
			if (true)
                if (a[4,3,2] == b[3,c[2,3,4],6])
                    if (a == b)
                        error();
            else 
                print("else of first if");
        }
}"""
        expect = """Program([
	VarDecl(a, ArrayType([4, 5, 6], IntegerType))
	VarDecl(b, ArrayType([5, 6, 7], FloatType))
	VarDecl(c, ArrayType([5, 6, 7], BooleanType))
	VarDecl(d, ArrayType([20, 21, 22], StringType))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(4), IntegerLit(3), IntegerLit(2)]), ArrayCell(b, [IntegerLit(3), ArrayCell(c, [IntegerLit(2), IntegerLit(3), IntegerLit(4)]), IntegerLit(6)])), IfStmt(BinExpr(==, Id(a), Id(b)), CallStmt(error, ), CallStmt(print, StringLit(else of first if)))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,336)) 

    def test_37(self):
        input = r"""
        /* global variables*/
        a: integer = 100; // global int
        b: float = 3.e-16; // global float
        func: function string(num: integer) {
            if (a < num) return tostring(a) + " is less than" + tostring(num);
            else return tostring(a) + " is greater than" + tostring(num);
        }
}"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(100))
	VarDecl(b, FloatType, FloatLit(3e-16))
	FuncDecl(func, StringType, [Param(num, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(a), Id(num)), ReturnStmt(BinExpr(+, BinExpr(+, FuncCall(tostring, [Id(a)]), StringLit( is less than)), FuncCall(tostring, [Id(num)]))), ReturnStmt(BinExpr(+, BinExpr(+, FuncCall(tostring, [Id(a)]), StringLit( is greater than)), FuncCall(tostring, [Id(num)]))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,337)) 

    def test_38(self):
        input = r"""
        foo: function void(){
            a[(1+2+3)-(4+5*6/abc &&(123))]= a[(((-5)))] + a[(((-5))),a[0]];
            return a[(1+2+3)-(4+5*6/abc &&(123))];
        }
}"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(-, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), BinExpr(&&, BinExpr(+, IntegerLit(4), BinExpr(/, BinExpr(*, IntegerLit(5), IntegerLit(6)), Id(abc))), IntegerLit(123)))]), BinExpr(+, ArrayCell(a, [UnExpr(-, IntegerLit(5))]), ArrayCell(a, [UnExpr(-, IntegerLit(5)), ArrayCell(a, [IntegerLit(0)])]))), ReturnStmt(ArrayCell(a, [BinExpr(-, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), BinExpr(&&, BinExpr(+, IntegerLit(4), BinExpr(/, BinExpr(*, IntegerLit(5), IntegerLit(6)), Id(abc))), IntegerLit(123)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,338)) 

    def test_39(self):
        input = r"""
        main: function void() {   
            a[1,foo(1,1,1*3.14)] = foo(gen(.e19), "mul", true, "string");
        }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), FuncCall(foo, [IntegerLit(1), IntegerLit(1), BinExpr(*, IntegerLit(1), FloatLit(3.14))])]), FuncCall(foo, [FuncCall(gen, [FloatLit(0.0)]), StringLit(mul), BooleanLit(True), StringLit(string)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,339)) 

    def test_40(self):
        input = r"""
        main: function void() {   
            a[5] = "hellooooooo /n welcome";
        }}
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(5)]), StringLit(hellooooooo /n welcome))]))
])"""
        self.assertTrue(TestAST.test(input,expect,340)) 

    def test_41(self):
        input = r"""
        main: function void() {   
            a = "      abc                ;;   cltq ";
        }}
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(      abc                ;;   cltq ))]))
])"""
        self.assertTrue(TestAST.test(input,expect,341)) 

    def test_42(self):
        input = r"""
        main: function void() {   
            a = foo(3)*fucn(3.14)/pi(3222)%2+a--32+to_int(s);
            return a;
        }}
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(-, BinExpr(+, BinExpr(%, BinExpr(/, BinExpr(*, FuncCall(foo, [IntegerLit(3)]), FuncCall(fucn, [FloatLit(3.14)])), FuncCall(pi, [IntegerLit(3222)])), IntegerLit(2)), Id(a)), UnExpr(-, IntegerLit(32))), FuncCall(to_int, [Id(s)]))), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input,expect,342)) 

    def test_43(self):
        input = r"""
        main: function void() {   
            a = a+5*f - (eee %(a != b*333+c*s) + fgh % adc ------ 666666 *(3.e11) ) / ee % qUE + ---- 4 * (((((.e-23))))) + 2e5;
            return a;
        }}
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, BinExpr(-, BinExpr(+, Id(a), BinExpr(*, IntegerLit(5), Id(f))), BinExpr(%, BinExpr(/, BinExpr(-, BinExpr(+, BinExpr(%, Id(eee), BinExpr(!=, Id(a), BinExpr(+, BinExpr(*, Id(b), IntegerLit(333)), BinExpr(*, Id(c), Id(s))))), BinExpr(%, Id(fgh), Id(adc))), BinExpr(*, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(666666)))))), FloatLit(300000000000.0))), Id(ee)), Id(qUE))), BinExpr(*, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(4))))), FloatLit(0.0))), FloatLit(200000.0))), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input,expect,343)) 

    def test_44(self):
        input = r"""
        main: function array [1,2,3,4,5] of string(a: boolean, b: string) {   
            a = (arr[3,1,23,bnm[a, b]]==3 && foo(arr[3,2,1,4,5], dev()));
            if (a) return arr;
            return arr;
        }}
}"""
        expect = """Program([
	FuncDecl(main, ArrayType([1, 2, 3, 4, 5], StringType), [Param(a, BooleanType), Param(b, StringType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(==, ArrayCell(arr, [IntegerLit(3), IntegerLit(1), IntegerLit(23), ArrayCell(bnm, [Id(a), Id(b)])]), BinExpr(&&, IntegerLit(3), FuncCall(foo, [ArrayCell(arr, [IntegerLit(3), IntegerLit(2), IntegerLit(1), IntegerLit(4), IntegerLit(5)]), FuncCall(dev, [])])))), IfStmt(Id(a), ReturnStmt(Id(arr))), ReturnStmt(Id(arr))]))
])"""
        self.assertTrue(TestAST.test(input,expect,344)) 

    def test_45(self):
        input = r"""
        main: function void(a: boolean, b: string) {   
            while (a) while (len(b) != 0) {
                for (i = 0, a != false, i*i) print(i);
            }
        }}
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, BooleanType), Param(b, StringType)], None, BlockStmt([WhileStmt(Id(a), WhileStmt(BinExpr(!=, FuncCall(len, [Id(b)]), IntegerLit(0)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(!=, Id(a), BooleanLit(False)), BinExpr(*, Id(i), Id(i)), CallStmt(print, Id(i)))])))]))
])"""
        self.assertTrue(TestAST.test(input,expect,345)) 

    def test_46(self):
        input = r"""
        main: function boolean(a: boolean, b: string) {   
            if (a){
                while (a) while (len(b) != 0) {
                    for (i = 0, a != false, i*i) print(i);
                }
            }
            else {
                a = !true && (b == "cool") || true&& !false && (a && 3);
            }
            return a;
        }}
}"""
        expect = """Program([
	FuncDecl(main, BooleanType, [Param(a, BooleanType), Param(b, StringType)], None, BlockStmt([IfStmt(Id(a), BlockStmt([WhileStmt(Id(a), WhileStmt(BinExpr(!=, FuncCall(len, [Id(b)]), IntegerLit(0)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(!=, Id(a), BooleanLit(False)), BinExpr(*, Id(i), Id(i)), CallStmt(print, Id(i)))])))]), BlockStmt([AssignStmt(Id(a), BinExpr(&&, BinExpr(&&, BinExpr(||, BinExpr(&&, UnExpr(!, BooleanLit(True)), BinExpr(==, Id(b), StringLit(cool))), BooleanLit(True)), UnExpr(!, BooleanLit(False))), BinExpr(&&, Id(a), IntegerLit(3))))])), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input,expect,346)) 

    def test_47(self):
        input = r"""
        main: function void(a: boolean, b: string) {   
            foo(boo(test(a,b),a),b,foo(a,b,c));
        }}
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, BooleanType), Param(b, StringType)], None, BlockStmt([CallStmt(foo, FuncCall(boo, [FuncCall(test, [Id(a), Id(b)]), Id(a)]), Id(b), FuncCall(foo, [Id(a), Id(b), Id(c)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,347)) 

    def test_48(self):
        input = r"""
        a,b,c: integer = 1, 3 ,7;
        d,e,f: float = 3.3, .e10, 1.2E333;
        foo: function integer(a: boolean, b: string) {   
            while (foo(boo(test(a,b),a),b,foo(a,b,c))) {
                print("hellowold!");
            }
            return 0;
        }}
}"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(3))
	VarDecl(c, IntegerType, IntegerLit(7))
	VarDecl(d, FloatType, FloatLit(3.3))
	VarDecl(e, FloatType, FloatLit(0.0))
	VarDecl(f, FloatType, FloatLit(inf))
	FuncDecl(foo, IntegerType, [Param(a, BooleanType), Param(b, StringType)], None, BlockStmt([WhileStmt(FuncCall(foo, [FuncCall(boo, [FuncCall(test, [Id(a), Id(b)]), Id(a)]), Id(b), FuncCall(foo, [Id(a), Id(b), Id(c)])]), BlockStmt([CallStmt(print, StringLit(hellowold!))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input,expect,348)) 

    def test_49(self):
        input = r"""
        a,b,c: integer = 1, 3 ,7;
}"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(3))
	VarDecl(c, IntegerType, IntegerLit(7))
])"""
        self.assertTrue(TestAST.test(input,expect,349)) 

    def test_50(self):
        input = r"""
        main: function integer() {
            if (a)
            if (b)
            if (c)
            if (d)
            else a=c;
            else d=f;
            else return 0;
            return 0;
        }
}"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([IfStmt(Id(a), IfStmt(Id(b), IfStmt(Id(c), IfStmt(Id(d), AssignStmt(Id(a), Id(c)), AssignStmt(Id(d), Id(f))), ReturnStmt(IntegerLit(0))))), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input,expect,350)) 

    def test_51_if_else(self):
        """ Test If Else Again """
        input = r"""
abc: function integer (x: float, y:float)
{
        if (a>0) if (b>0) if (d==0) if (e > 3) a = a - 1; else b = a; else c = d; else b = 3;
    
}
"""
        expect = """Program([
	FuncDecl(abc, IntegerType, [Param(x, FloatType), Param(y, FloatType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(0)), IfStmt(BinExpr(>, Id(b), IntegerLit(0)), IfStmt(BinExpr(==, Id(d), IntegerLit(0)), IfStmt(BinExpr(>, Id(e), IntegerLit(3)), AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1))), AssignStmt(Id(b), Id(a))), AssignStmt(Id(c), Id(d))), AssignStmt(Id(b), IntegerLit(3))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))


    def test_52(self):
        input = r"""
        main: function integer() {
            if (a)
            if (b)
            if (c)
            if (d)
            b=c;
            else a=c;
            else d=f;
            else return 0;
            return 0;
}"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([IfStmt(Id(a), IfStmt(Id(b), IfStmt(Id(c), IfStmt(Id(d), AssignStmt(Id(b), Id(c)), AssignStmt(Id(a), Id(c))), AssignStmt(Id(d), Id(f))), ReturnStmt(IntegerLit(0)))), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input,expect,352))

    