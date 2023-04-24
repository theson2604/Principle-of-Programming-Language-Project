import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    #test simple program
#     def test0(self):
#         input = """
#         main: function void () {
#         }
#         """
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input, expect, 400))

#     def test1(self):
#         input = """x, y, z: integer = 1, 2, 3;
#         main: function void () {
#         }  
#         """
#         expect = """[]"""
#         self.assertTrue(TestChecker.test(input, expect, 401))

#     def test2(self):
#         input = """x, y, z: integer = 1, 2, 3;
#         a, b: float;
#         main: function void () {
#         }  
#         """
#         expect = """[]"""
#         self.assertTrue(TestChecker.test(input, expect, 402))

#     def test3(self):
#         """Simple program"""
#         input = """main: function void () {
#         }"""
#         expect = """[]"""
#         self.assertTrue(TestChecker.test(input, expect, 403))

#     def test4(self):
#         """More complex program"""
#         input = """main: function void () {
#             printInteger(4);
#         }"""
#         expect = """[]"""
#         self.assertTrue(TestChecker.test(input, expect, 404))

#     def test5(self):
#         input = """
# a, B, c: array [5,1000] of boolean ;
#         main: function void () {
#         printBoolean(false);
#         }
# """
#         expect = """[]"""
#         self.assertTrue(TestChecker.test(input, expect, 405))

#     def test6(self):
#         input = """
#         a: integer;
#         main: function void() {
#                     for (a=1, a<10, a+1) {
#                         printInteger(a);
#                     }
#                    }"""
#         expect = """[]"""
#         self.assertTrue(TestChecker.test(input,expect,406))

#     def test7(self):
#         input = """main: function void() {
#                     while(true) {
#                         a: boolean = false;
#                         c: float = 2.333333;
#                         continue;}
#                    }"""
#         expect = """[]"""
#         self.assertTrue(TestChecker.test(input,expect,407))

#     def test8(self):
#         input = """test: function boolean() {
#         a: array[23,5,3] of integer;
#         b: boolean;
#         while(true) {
#             test();
#             break;}
#         return b;
# }
#         main: function void() {
#             a: integer = 3;
#         }
# """
#         expect = """[]"""
#         self.assertTrue(TestChecker.test(input,expect,408))

#     def test9(self):
#         input = """
#         var, b: auto = false, true;
#         a: float = 3.0;
#         test: function boolean(inherit a: float, b: boolean) {
# return true;
# }
#     main: function void() {
#         printBoolean(var);
#         test(a, b);
#     }
# """
#         expect = """[]"""
#         self.assertTrue(TestChecker.test(input,expect,409))

#     #test redeclare
#     def test10(self):
#         input = """
#         var, b: auto = false, true;
#         a: float = 3.0;
#         test: function boolean(inherit a: float, b: boolean) {
#         b: integer = 999;
# return true;
# }
# """
#         expect = """Redeclared Variable: b"""
#         self.assertTrue(TestChecker.test(input,expect,410))
        
#     def test11(self):
#         input = """
#         var, b: auto = false, true;
#         a: float = 3.0;
#         test: function boolean(inherit a: float, b: boolean) {
#             var: integer;
#             return true;
#             printInteger(123);
#             a: integer = 123;
# }
# """
#         expect = """Redeclared Variable: a"""
#         self.assertTrue(TestChecker.test(input,expect,411))

#     def test12(self):
#         input = """
#         var, b: auto = false, true;
#         a: float = 3.0;
#         test: function boolean(inherit a: float, b: boolean, var: array [3] of float, a: string) {
#             var: integer;
#             return true;
#             printInteger(123);
#             a: integer = 123;
# }
# """
#         expect = """Redeclared Parameter: a"""
#         self.assertTrue(TestChecker.test(input,expect,412))


#     def test13(self):
#         input = """
#         var, b: auto = false, true;
#         a: integer = 3;
#         arr: array [3] of integer;
#         test: function boolean(inherit a: float, b: boolean, var: array [3] of float) {
#             return true;
#             printInteger(123);
#             test: integer = 123;
# }
#         b: function array [3] of integer() {
#             return arr;
#         }
# """
#         expect = """Redeclared Function: b"""
#         self.assertTrue(TestChecker.test(input,expect,413))

#     #test auto type
#     def test14(self):
#         input = """
#         var, b: auto = false, true;
#         a: float = 3.0;
#         arr: array [3] of integer;
#         test: function boolean(inherit a: float, b: auto, var: array [3] of float) {
#             return true;
#             printInteger(123);
#             w: integer = 123;
#             func(b, "123");
#             b = true;
# }
#         func: function array [3] of integer(f: boolean, y: string) {
#         return {1,2,3};
#         }
# """
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input,expect,414))

#     def test15(self):
#         input = """
#         var, b: auto = false, true;
#         a: float = 3.0;
#         arr: array [3] of integer;
#         test: function auto(inherit a: float) {
# }
#         func: function array [3] of integer(f: boolean, y: string) {
#             var = test(a);
#             return {1,2,3};
#             b = test(a);
#         }
# """
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input,expect,415))

#     def test16(self):
#         input = """
#         var, b: auto = false, true;
#         a: float = 3.0;
#         arr: array [3] of integer;
#         test: function auto(inherit a: float) {
#             func(true, "aaaa");
# }
#         func: function array [3] of integer(f: boolean, y: string) {
#             var = test(a);
#             return {1,2,3};
#             b = test(a);
#         }
# """
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input,expect,416))

#     #test Undeclare
#     def test17(self):
#         input = """
#         var, b: auto = false, true;
#         a: float = 3.0;
#         arr: array [3] of integer;
#         test: function auto(inherit a: float) {
#             var = test(al);
# }
#         func: function array [3] of integer(f: boolean, y: float) {
#             var = test(a);
#             return {1,2,3};
#             b = test(a);
#         }
# """
#         expect = """Undeclared Identifier: al"""
#         self.assertTrue(TestChecker.test(input,expect,417))

#     def test18(self):
#         input = """
#         var, b: auto = false, true;
#         a: float = 3.0;
#         arr: array [3] of integer;
#         test: function auto(inherit a: float) {
#             for (aw=1, a<10, a+1) {
#                 printInteger(a);
#             }
# }
#         func: function array [3] of integer(f: boolean, y: float) {
#             var = test(a);
#             return {1,2,3};
#             b = test(a);
#         }
# """
#         expect = """Undeclared Identifier: aw"""
#         self.assertTrue(TestChecker.test(input,expect,418))

#     def test19(self):
#         input = """
#         var, b: auto = false, true;
#         a: float = 3.0;
#         i: integer;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (flag == var) {
#                     printInteger(i);
#                 }
#             }
# }
#         func: function array [3] of integer(f: boolean, y: float) {
#             var = test(a);
#             return {1,2,3};
#             b = test(a);
#         }
# """
#         expect = """Undeclared Identifier: flag"""
#         self.assertTrue(TestChecker.test(input,expect,419))

#     #test Redeclare
#     def test20(self):
#         input = """
#         var, b: auto = false, true;
#         i: integer;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (b == var) {
#                     printInteger(i);
#                 }
#             }
# }
#         func: function float(f: boolean, y: float) inherit test{
#             super(3.0);
#             var = test(a);
#             return a;
#             a: integer;
#             b = test(a);
#         }
# """
#         expect = """Redeclared Variable: a"""
#         self.assertTrue(TestChecker.test(input,expect,420))

#     def test21(self):
#         input = """
#         var, b: auto = false, true;
#         i: integer;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (b == var) {
#                     printInteger(i);
#                 }
#             }
# }
#         func: function float(f: boolean, y: float){
#             a: float;
#             var = test(a);
#             return a;
#             b = test(a);
#         }

#         b: auto = {1,2,3};
# """
#         expect = """Redeclared Variable: b"""
#         self.assertTrue(TestChecker.test(input,expect,421))

#     def test22(self):
#         input = """
#         var, b: auto = false, true;
#         i: integer;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (b == var) {
#                     printInteger(i);
#                 }
#             }
# }
#         var: function float(f: boolean, y: float){
#             a: float;
#             var = test(a);
#             return a;
#             b = test(a);
#         }

#         b: auto = {1,2,3};
# """
#         expect = """Redeclared Function: var"""
#         self.assertTrue(TestChecker.test(input,expect,422))

#     def test23(self):
#         input = """
#         var, b: auto = false, true;
#         i: integer;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (b == var) {
#                     printInteger(i);
#                 }
#             }
# }
#         test1: function float(f: boolean, y: float){
#             a: float;
#             var = test(a);
#             return a;
#             b = test(a);
#         }

#         test: auto = {1,2,3};
# """
#         expect = """Redeclared Variable: test"""
#         self.assertTrue(TestChecker.test(input,expect,423))

#     def test24(self):
#         input = """
#         var, b: auto = false, true;
#         i: integer;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (b == var) {
#                     printInteger(i);
#                 }
#             }
# }
#         test1: function float(f: boolean, y: float, f: string){
#             a: float;
#             var = test(a);
#             return a;
#             b = test(a);
#         }

#         test: auto = {1,2,3};
# """
#         expect = """Redeclared Parameter: f"""
#         self.assertTrue(TestChecker.test(input,expect,424))

#     def test25(self):
#         input = """
#         var, b: auto = false, true;
#         i: integer;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (b == var) {
#                     printInteger(i);
#                 }
#             }
# }
#         test1: function float(f: boolean, y: float){
#             a: float;
#             var = test(a);
#             return a;
#             y: array [1,2,3] of boolean;
#             b = test(a);
#         }

#         test: auto = {1,2,3};
# """
#         expect = """Redeclared Variable: y"""
#         self.assertTrue(TestChecker.test(input,expect,425))

#     def test26(self):
#         input = """
#         var, b: auto = false, true;
#         i: integer;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (b == var) {
#                     printInteger(i);
#                 }
#             }
# }
#         func: function float(f: boolean, y: float) inherit test{
#             super(3.0);
#             var = test(a);
#             func: boolean = false;
#             return a;
#         }

#         func: auto = {1,2,3};
# """
#         expect = """Redeclared Variable: func"""
#         self.assertTrue(TestChecker.test(input,expect,426))

#     #test Invalid
#     def test27(self):
#         input = """
#         var: auto;
#         i: integer;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (b == var) {
#                     printInteger(i);
#                 }
#             }
# }
#         func: function float(f: boolean, y: float) inherit test{
#             super(3.0);
#             var = test(a);
#             func: boolean = false;
#             return a;
#         }

#         func: auto = {1,2,3};
# """
#         expect = """Invalid Variable: var"""
#         self.assertTrue(TestChecker.test(input,expect,427))

#     def test28(self):
#         input = """
#         var: auto = 2.0;
#         i: integer;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (i == 2) {
#                     printInteger(i);
#                 }
#             }
#             var= func(true, var);
# }
#         func: function float(f: boolean, y: float){
#             foo: auto;
#             func: boolean = false;
#             return y;
#         }

#         func: auto = {1,2,3};
# """
#         expect = """Invalid Variable: foo"""
#         self.assertTrue(TestChecker.test(input,expect,428))

#     def test29(self):
#         input = """
#         var: auto = 2.0;
#         i: integer;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (i == 2) {
#                     printInteger(i);
#                 }
#             }
#             var= func(true, var);
# }
#         func: function float(f: boolean, y: float){
#             foo: auto;
#             func: boolean = false;
#             return y;
#         }

#         func: auto = {1,2,3};
# """
#         expect = """Invalid Variable: foo"""
#         self.assertTrue(TestChecker.test(input,expect,429))

#     def test30(self):
#         input = """
#         var: auto = 2.0;
#         i: integer;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (i == 2) {
#                     printInteger(i);
#                 }
#             }
#             var= func(true, i);
# }
#         func: function float(f: boolean, a: integer) inherit test{
#             super(var);
#             func: boolean = false;
#             return y;
#         }

#         func: auto = {1,2,3};
# """
#         expect = """Invalid Parameter: a"""
#         self.assertTrue(TestChecker.test(input,expect,430))

#     def test31(self):
#         input = """
#         var: auto = 2.0;
#         i: integer;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (i == 2) {
#                     printInteger(i);
#                 }
#             }
#             var: auto;
#             var= func(true, i);
# }
#         func: function float(f: boolean, a: integer) inherit test{
#             super(var);
#             func: boolean = false;
#             return y;
#         }

#         func: auto = {1,2,3};
# """
#         expect = """Invalid Variable: var"""
#         self.assertTrue(TestChecker.test(input,expect,431))

#     #test mismatch in var
#     def test32(self):
#         input = """
#         var: auto = 2.0;
#         i: integer = var;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (i == 2) {
#                     printInteger(i);
#                 }
#             }
#             var: auto;
#             var= func(true, i);
# }
#         func: function float(f: boolean, a: integer) inherit test{
#             super(var);
#             func: boolean = false;
#             return y;
#         }

#         func: auto = {1,2,3};
# """
#         expect = """Type mismatch in Variable Declaration: VarDecl(i, IntegerType, Id(var))"""
#         self.assertTrue(TestChecker.test(input,expect,432))

#     def test33(self):
#         input = """
#         var: auto = 2.0;
#         i: integer = 2;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (i == 2) {
#                     printInteger(i);
#                 }
#             }
#             var= test(var);
# }
#         foo: integer = test(var);
#         func: function float(f: boolean, a: integer) inherit test{
#             super(var);
#             func: boolean = false;
#             return y;
#         }

#         func: auto = {1,2,3};
# """
#         expect = """Type mismatch in Variable Declaration: VarDecl(foo, IntegerType, FuncCall(test, [Id(var)]))"""
#         self.assertTrue(TestChecker.test(input,expect,433))

#     def test33(self):
#         input = """
#         var: auto = 2.0;
#         i: integer = 2;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (i == 2) {
#                     printInteger(i);
#                 }
#             }
#             var= test(var);
# }
#         foo: integer = test(var);
#         func: function float(f: boolean, a: integer) inherit test{
#             super(var);
#             func: boolean = false;
#             return y;
#         }

#         func: auto = {1,2,3};
# """
#         expect = """Type mismatch in Variable Declaration: VarDecl(foo, IntegerType, FuncCall(test, [Id(var)]))"""
#         self.assertTrue(TestChecker.test(input,expect,433))

#     def test34(self):
#         input = """
#         var: auto = 2.0;
#         i: integer = test(var);
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (i == 2) {
#                     printInteger(i);
#                 }
#             }
#             var: integer = test(a);
# }
#         func: function auto(f: boolean, y: integer) inherit test{
#             super(var);
#             return y;
#         }
#         foo : function auto (inherit n: auto, m: auto){
#             a: string = n + m;
#         }
# """
#         expect = """Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(+, Id(n), Id(m)))"""
#         self.assertTrue(TestChecker.test(input,expect,434))

#     #test mismatch in expr
#     #array subscripting
#     def test35(self):
#         input = """
#         var: auto = {1,2,3,4,5};
#         i: integer = test(2.0);
#         test: function auto(inherit a: float) {
#             i = var[a];
#             for (i=1, i<10, i+1) {
#                 while (i == 2) {
#                     printInteger(i);
#                 }
#             }
#             var: float = test(a);
# }
#         func: function auto(f: boolean, y: integer) inherit test{
#             super(var);
#             return y;
#         }
#         new_id: boolean = func(true, 123);
# """
#         expect = """Type mismatch in expression: ArrayCell(var, [Id(a)])"""
#         self.assertTrue(TestChecker.test(input,expect,435))

    
#     def test36(self):
#         input = """
#         var: auto = {{32,3,4},{1,2,3},{2,3,3}};
#         i: integer = test(2.0);
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (var[i, a] == 2) {
#                     printInteger(i);
#                 }
#             }
#             var: float = test(a);
# }
#         func: function auto(f: boolean, y: integer) inherit test{
#             super(var);
#             return y;
#         }
#         new_id: boolean = func(true, 123);
# """
#         expect = """Type mismatch in expression: ArrayCell(var, [Id(i), Id(a)])"""
#         self.assertTrue(TestChecker.test(input,expect,436))

#     def test37(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(2.0);
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (var[test(1.3333)] == 2) {
#                     printInteger(i);
#                 }
#             }
#             o: integer = var[a];
# }
#         func: function auto(f: boolean, y: integer) inherit test{
#             super(var[i]);
#             return f;
#         }
#         new_id: boolean = func(true, 123);
#         x: integer = var[func(true, i)];
# """
#         expect = """Type mismatch in expression: ArrayCell(var, [Id(a)])"""
#         self.assertTrue(TestChecker.test(input,expect,437))

#     #binop and unop
#     def test38(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(2.0);
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (var[i] == (2 + a)) {
#                     printInteger(i);
#                 }
#             }
# }
#         func: function auto(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in expression: BinExpr(==, ArrayCell(var, [Id(i)]), BinExpr(+, IntegerLit(2), Id(a)))"""
#         self.assertTrue(TestChecker.test(input,expect,438))
    
#     def test39(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(2.0);
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (var[i] == (2 + i)) {
#                     a = a % 3;
#                     printInteger(i);
#                 }
#             }
# }
#         func: function auto(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in expression: BinExpr(%, Id(a), IntegerLit(3))"""
#         self.assertTrue(TestChecker.test(input,expect,439))

#     def test40(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(2.0);
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (flag == true) {
#                     i = var[i] % 3;
#                     printInteger(i);
#                 }
                
#             }
#             s: string = "hello world";
#             s = s :: "!!!!!!!!!!!!!!!";
#             if (!s) {
#                 return ;
#             }
# }
#         func: function auto(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in expression: UnExpr(!, Id(s))"""
#         self.assertTrue(TestChecker.test(input,expect,440))


#     def test41(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(2.0);
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (flag == true) {
#                     i = var[i] % 3;
#                     printInteger(i);
#                 }
                
#             }
#             s: string = "hello world";
#             s = i :: "!!!!!!!!!!!!!!!";
#             if (!s) {
#                 return ;
#             }
# }
#         func: function auto(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in expression: BinExpr(::, Id(i), StringLit(!!!!!!!!!!!!!!!))"""
#         self.assertTrue(TestChecker.test(input,expect,441))

#     def test42(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(2.0);
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (a == 3.0) {
#                     i = var[i] % 3;
#                     printInteger(i);
#                 }
                
#             }
#             s: string = "hello world";
#             s = i :: "!!!!!!!!!!!!!!!";
#             if (!s) {
#                 return ;
#             }
# }
#         func: function auto(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in expression: BinExpr(==, Id(a), FloatLit(3.0))"""
#         self.assertTrue(TestChecker.test(input,expect,442))

#     #FuncCall
#     def test43(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(2.0);
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (flag) {
#                     i = var[i] % 3;
#                     a = func(flag, i);
#                 }
                
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in expression: FuncCall(func, [Id(flag), Id(i)])"""
#         self.assertTrue(TestChecker.test(input,expect,443))

#     def test44(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(2.0);
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (flag) {
#                     i = var[i] % 3;
#                     a = func(flag, i, var[3], test(3.0));
#                 }
                
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in expression: FuncCall(func, [Id(flag), Id(i), ArrayCell(var, [IntegerLit(3)]), FuncCall(test, [FloatLit(3.0)])])"""
#         self.assertTrue(TestChecker.test(input,expect,444))

#     def test45(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(var[3]);
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (flag) {
#                     i = var[i] % 3;
#                     a = func(var[3], i);
#                 }
                
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in expression: FuncCall(func, [ArrayCell(var, [IntegerLit(3)]), Id(i)])"""
#         self.assertTrue(TestChecker.test(input,expect,445))

#     def test46(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test();
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (flag) {
#                     i = var[i] % 3;
#                     a = func(var[3], i);
#                 }
                
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in expression: FuncCall(test, [])"""
#         self.assertTrue(TestChecker.test(input,expect,446))

#     #test mismatch in stmt
#     def test47(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=1, i<10, i+1) {
#                 while (var[3] + i) {
#                     i = var[i] % 3;
#                     a = func(var[3], i);
#                 }
                
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in statement: WhileStmt(BinExpr(+, ArrayCell(var, [IntegerLit(3)]), Id(i)), BlockStmt([AssignStmt(Id(i), BinExpr(%, ArrayCell(var, [Id(i)]), IntegerLit(3))), AssignStmt(Id(a), FuncCall(func, [ArrayCell(var, [IntegerLit(3)]), Id(i)]))]))"""
#         self.assertTrue(TestChecker.test(input,expect,447))

#     def test48(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=1, i%2, i+1) {
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(%, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))"""
#         self.assertTrue(TestChecker.test(input,expect,448))

#     def test49(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=1, i!=var[0], i+1) {
#                 var = {1,2,3,4,5,6};
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in statement: AssignStmt(Id(var), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)]))"""
#         self.assertTrue(TestChecker.test(input,expect,449))

#     def test50(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         e: float = i;
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=1, i!=var[0], i+1) {
#                 a = var[2];
#                 var[6] = e; 
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in statement: AssignStmt(ArrayCell(var, [IntegerLit(6)]), Id(e))"""
#         self.assertTrue(TestChecker.test(input,expect,450))

#     def test51(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         e: float = i;
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i="!!!!!!!!!!!", i!=var[0], i+1) {
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in statement: AssignStmt(Id(i), StringLit(!!!!!!!!!!!))"""
#         self.assertTrue(TestChecker.test(input,expect,451))

#     def test52(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         e: float = i;
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=2, i!=var[0], i+1) {
#                 printInteger(a);
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in statement: CallStmt(printInteger, Id(a))"""
#         self.assertTrue(TestChecker.test(input,expect,452))

#     def test53(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         e: float = i;
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             func(test(e), i);
#             for (i=2, i!=var[0], i+1) {
#                 printInteger(a);
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(var);
#             return f;
#         }
# """
#         expect = """Type mismatch in statement: CallStmt(func, FuncCall(test, [Id(e)]), Id(i))"""
#         self.assertTrue(TestChecker.test(input,expect,453))

#     def test54(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         e: float = i;
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=2, i!=var[0], i+1) {
#                 printInteger(i);
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(e);
#             func(test(e));
#         }
# """
#         expect = """Type mismatch in statement: CallStmt(func, FuncCall(test, [Id(e)]))"""
#         self.assertTrue(TestChecker.test(input,expect,454))

#     def test55(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         e: float = i;
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             func(test(e), i);
#             for (i=2, i!=var[0], i+1) {
#                 printInteger(a, flag, i, e);
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(e);
#             return f;
#         }
# """
#         expect = """Type mismatch in statement: CallStmt(func, FuncCall(test, [Id(e)]), Id(i))"""
#         self.assertTrue(TestChecker.test(input,expect,455))

#     def test56(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         e: float = i;
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             func(flag, i);
#             for (i=2, i!=var[0], i+1) {
#                 return a;
#             }
#         }
#         func: function void(f: boolean, y: integer) inherit test{
#             super(e);
#             return f;
#         }
# """
#         expect = """Type mismatch in statement: ReturnStmt(Id(a))"""
#         self.assertTrue(TestChecker.test(input,expect,456))

#     def test57(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         e: float = i;
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             func(flag, i);
#             for (i=2, i!=var[0], i+1) {
#                 return i;
#             }
#         }
#         func: function string(f: boolean, y: integer) inherit test{
#             super(e);
#             return f;
#         }
# """
#         expect = """Type mismatch in statement: ReturnStmt(Id(f))"""
#         self.assertTrue(TestChecker.test(input,expect,457))

#     #test must in loop
#     def test58(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         e: float = i;
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             func(flag, i);
#             for (i=2, i!=var[0], i+1) {
#                 break;
#                 return i;
#             }
#         }
#         func: function string(f: boolean, y: integer) inherit test{
#             super(e);
#             continue;
#             return f;
#         }
# """
#         expect = """Must in loop: ContinueStmt()"""
#         self.assertTrue(TestChecker.test(input,expect,458))
    
#     def test59(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         e: float = i;
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             func(flag, i);
#             for (i=2, i!=var[0], i+1) {
#                 break;
#                 return i;
#             }
#         }
#         func: function string(f: boolean, y: integer) inherit test{
#             super(e);
#             while(1 != 2) {
#                 break;
#             }
#             break;
#             return f;
#         }
# """
#         expect = """Must in loop: BreakStmt()"""
#         self.assertTrue(TestChecker.test(input,expect,459))

#     #test illegal arraylit
#     def test60(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         e: float = i;
#         flag: boolean = false;
#         s: string = "!!!!";
#         test: function auto(inherit a: float) {
#             func(flag, i);
#             for (i=2, i!=var[0], i+1) {
#                 break;
#                 return i;
#             }
#         }
#         func: function string(f: boolean, y: integer) inherit test{
#             super(e);
#             while(1 != 2) {
#                 break;
#             }
#             return s;
#         }
#         arr: array [4] of float = {1.3, 20e-2, 4.2, 5};
# """
#         expect = """Illegal array literal: ArrayLit([FloatLit(1.3), FloatLit(0.2), FloatLit(4.2), IntegerLit(5)])"""
#         self.assertTrue(TestChecker.test(input,expect,460))

#     def test61(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         e: float = i;
#         s: string = "!!!!";
#         arr: array [4] of string = {"123", "hello", "world", s};
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             func(flag, i);
#             for (i=2, i!=var[0], i+1) {
#                 break;
#                 return i;
#                 new_arr: array [4] of string = {"123", "hello", e, s};
#             }
#         }
#         func: function string(f: boolean, y: integer) inherit test{
#             super(e);
#             while(1 != 2) {
#                 break;
#             }
#             return s;
#         }
#         arr: array [4] of float = {1.3, 20e-2, 4.2, 5};
# """
#         expect = """Illegal array literal: ArrayLit([StringLit(123), StringLit(hello), Id(e), Id(s)])"""
#         self.assertTrue(TestChecker.test(input,expect,461))

#     #test invalid first stmt
#     def test62(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test(3.2e-1);
#         e: float = i;
#         flag: boolean = false;
#         test: function auto(inherit a: float) {
#             for (i=2, i!=var[0], i+1) {
#                 break;
#                 return i;
#             }
#         }
#         func: function string(f: boolean, y: integer) inherit test{
#             while(1 != 2) {
#                 break;
#             }
#             return s;
#         }
# """
#         expect = """Invalid statement in function: func"""
#         self.assertTrue(TestChecker.test(input,expect,462))

#     def test63(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test();
#         e: float = i;
#         flag: boolean = false;
#         func: function string(inherit f: boolean, y: integer) inherit test{
#             while(1 != 2) {
#                 break;
#             }
#             return "owowowowo";
#         }
#         test: function auto() {
#             for (i=2, i!=var[0], i+1) {
#                 break;
#                 return i;
#             }
#         }
#         foo: function auto(bar: string, boo: float) inherit func {
#             var: integer = 2;
#         }
# """
#         expect = """Invalid statement in function: foo"""
#         self.assertTrue(TestChecker.test(input,expect,463))

#     def test64(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test();
#         e: float = i;
#         flag: boolean = false;
#         func: function string(inherit f: boolean, y: integer) inherit test{
#             preventDefault();
#             while(1 != 2) {
#                 break;
#             }
#             return "owowowowo";
#         }
#         test: function auto() {
#             for (i=2, i!=var[0], i+1) {
#                 break;
#                 return i;
#             }
#         }
#         foo: function auto(bar: string, boo: float) inherit func {
#             test();
#             var: integer = 2;
#         }
# """
#         expect = """Invalid statement in function: foo"""
#         self.assertTrue(TestChecker.test(input,expect,464))

#     #test no entry
#     def test65(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = test();
#         e: float = i;
#         flag: boolean = false;
#         func: function string(inherit f: boolean, y: integer) inherit test{
#             preventDefault();
#             while(1 != 2) {
#                 break;
#             }
#             return "owowowowo";
#         }
#         test: function auto() {
#             for (i=2, i!=var[0], i+1) {
#                 break;
#                 return i;
#             }
#         }
#         foo: function auto(bar: string, boo: float) inherit func {
#             super(true, i);
#             var: boolean = f;
#         }
# """
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input,expect,465))

#     def test66(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = foo("not", 3.333e9);
#         e: float = i;
#         flag: boolean = false;
#         func: function string(inherit f: boolean, y: integer){
#             while(1 != 2) {
#                 break;
#             }
#             return "owowowowo";
#         }
#         main: function boolean() {
#             return true;
#         }
#         foo: function auto(bar: string, boo: float) inherit func {
#             super(true, 1);
#             var: boolean = f;
#         }
# """
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input,expect,466))

#     def test67(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = foo("not", 3.333e9);
#         e: float = i;
#         flag: boolean = false;
#         func: function string(inherit f: boolean, y: integer){
#             while(1 != 2) {
#                 break;
#             }
#             return "owowowowo";
#         }
#         main: auto = {1,2,3,4,5};
#         foo: function auto(bar: string, boo: float) inherit func {
#             super(true, var[i]);
#             var: boolean = f;
#         }
# """
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input,expect,467))

#     #test inherit
#     def test68(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = foo(3.333e9, var[3]);
#         e: float = i;
#         flag: boolean = false;
#         inc : function void (out n: integer, a:float) inherit foo{}
#         foo : function auto (inherit n: float, n: integer){}
# """
#         expect = """Invalid Parameter: n"""
#         self.assertTrue(TestChecker.test(input,expect,468))

#     def test69(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = foo(3.333e9, var[3]);
#         e: float = i;
#         flag: boolean = false;
#         inc : function void (out o: integer, a:float) inherit foo{}
#         foo : function auto (inherit n: float, n: integer){}
# """
#         expect = """Invalid statement in function: inc"""
#         self.assertTrue(TestChecker.test(input,expect,469))

#     def test70(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = foo(3.333e9, var[3]);
#         e: float = i;
#         flag: boolean = false;
#         inc : function void (out o: integer, a:float) inherit foo{
#             preventDefault();
#             a: float = foo(n, 2);
#         }
#         foo : function auto (inherit n: float, n: integer){}
# """
#         expect = """Redeclared Variable: a"""
#         self.assertTrue(TestChecker.test(input,expect,470))

#     def test71(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = foo(3.333e9, var[3]);
#         e: float = i;
#         flag: boolean = false;
#         inc : function void (out o: integer, a:float) inherit foo{
#             super(3.2);
#             a: float = foo(n, 2);
#         }
#         foo : function auto (inherit n: float, n: integer){}
# """
#         expect = """Type mismatch in expression: """
#         self.assertTrue(TestChecker.test(input,expect,471))

#     def test72(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = foo(3.333e9, var[3]);
#         e: float = i;
#         flag: boolean = false;
#         inc : function void (out o: integer, a:float) inherit foo{
#             super(3.2, i, var[31]);
#             a: float = foo(n, 2);
#         }
#         foo : function auto (inherit n: float, n: integer){}
# """
#         expect = """Type mismatch in expression: ArrayCell(var, [IntegerLit(31)])"""
#         self.assertTrue(TestChecker.test(input,expect,472))

#     def test73(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = foo(3.333e9, var[3]);
#         e: float = i;
#         flag: boolean = false;
#         inc : function void (out o: integer, a:float) inherit foo{
#             super(3.2, i, var[31]);
#             a: float = foo(n, 2);
#         }
#         foo : function auto (inherit n: float, n: integer){}
# """
#         expect = """Type mismatch in expression: ArrayCell(var, [IntegerLit(31)])"""
#         self.assertTrue(TestChecker.test(input,expect,473))

#     def test74(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = foo(3.333e9, var[3]);
#         e: float = i;
#         flag: boolean = false;
#         inc : function void (out o: integer, a:float) inherit foo{
#             super(3.2, i, var[31]);
#             a: float = foo(n, 2);
#         }
#         foo : function auto (inherit n: float, n: integer){}
# """
#         expect = """Type mismatch in expression: ArrayCell(var, [IntegerLit(31)])"""
#         self.assertTrue(TestChecker.test(input,expect,474))

#     def test75(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = foo(3.333e9, var[3]);
#         e: float = i;
#         flag: boolean = false;
#         inc : function void (out o: integer, a:float) inherit foo{
#             super(3.2, e);
#             a: float = foo(n, 2);
#         }
#         foo : function auto (inherit n: float, n: integer){}
# """
#         expect = """Type mismatch in expression: Id(e)"""
#         self.assertTrue(TestChecker.test(input,expect,475))

#     def test76(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = foo();
#         e: float = i;
#         flag: boolean = false;
#         inc : function void (out o: integer, a:float) inherit foo{
#             prevenDefault();
#             a: float = foo(n, 2);
#         }
#         foo : function auto (){}
# """
#         expect = """Undeclared Function: prevenDefault"""
#         self.assertTrue(TestChecker.test(input,expect,476))

#     #test random
#     def test77(self):
#         input = """
#         main: function void() {
#             a = b; 
#         }
# """
#         expect = """Undeclared Identifier: a"""
#         self.assertTrue(TestChecker.test(input,expect,477))

#     def test78(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = foo();
#         e: float = i;
#         flag: boolean = false;
#         inc : function void (out o: auto, a:auto) inherit foo{
#             preventDefault();
#             b: string = a + o;
#         }
#         foo : function auto (){}
# """
#         expect = """Type mismatch in Variable Declaration: VarDecl(b, StringType, BinExpr(+, Id(a), Id(o)))"""
#         self.assertTrue(TestChecker.test(input,expect,478))

#     def test79(self):
#         input = """
#         var: auto = {32,3,4,1,2,3};
#         i: integer = foo();
#         e: float = i;
#         flag: boolean = false;
#         inc : function void (out o: auto, a:auto) inherit foo{
#             preventDefault();
#             b: string = i != flag;
#         }
#         foo : function auto (){}
# """
#         expect = """Type mismatch in Variable Declaration: VarDecl(b, StringType, BinExpr(!=, Id(i), Id(flag)))"""
#         self.assertTrue(TestChecker.test(input,expect,479))

#     def test80(self):
#         input = """
#         var: auto = {{{{1,2,3}}}};
#         main: function void() {
#             a: integer = var[3,3,3];
#         }
# """
#         expect = """Type mismatch in expression: ArrayCell(var, [IntegerLit(3), IntegerLit(3), IntegerLit(3)])"""
#         self.assertTrue(TestChecker.test(input,expect,480))

#     def test81(self):
#         input = """
#         var: auto = {{1,2,3},{1,2,3.45}};
#         main: function void() {
#             a: integer = var[3,3,3];
#         }
# """
#         expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.45)])])"""
#         self.assertTrue(TestChecker.test(input,expect,481))

#     def test82(self):
#         input = """
#         i: integer = 3;
#         e: boolean;
#         var: auto = {{1,2,3},{i+e,2,2}};
#         main: function void() {
#             a: integer = var[3,3,3];
#         }
# """
#         expect = """Type mismatch in expression: BinExpr(+, Id(i), Id(e))"""
#         self.assertTrue(TestChecker.test(input,expect,482))

#     def test83(self):
#         input = """
#         i: integer = 3;
#         e: boolean;
#         var: auto =  { {1 , 2}, { 1,1.5} };
#         main: function void() {
#             a: integer = var[3,3,3];
#         }
# """
#         expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), FloatLit(1.5)])])"""
#         self.assertTrue(TestChecker.test(input,expect,483))

#     def test84(self):
#         input = """
#         i: integer;
#         e: boolean;
#         var: auto =  { {true , e}, { e,1.5>3.2} };
#         main: function void() {
#             a: integer = var[3,3];
#         }
# """
#         expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, ArrayCell(var, [IntegerLit(3), IntegerLit(3)]))"""
#         self.assertTrue(TestChecker.test(input,expect,484))

#     def test85(self):
#         input = """
#         i: integer;
#         e: boolean;
#         var: auto =  { {true , e}, { e!=i,1.5>i} };
#         main: function void() {
#             a: integer = var[3,3];
#         }
# """
#         expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, ArrayCell(var, [IntegerLit(3), IntegerLit(3)]))"""
#         self.assertTrue(TestChecker.test(input,expect,485))

#     def test_0(self):
#         input = """a: auto;"""
#         expect = "Invalid Variable: a"
#         self.assertTrue(TestChecker().test(input, expect, 500))

#     def test_1(self):
#         input = """delta: integer = 3;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 501))

#     def test_2(self):
#         input = """a: integer = 3.2;"""
#         expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(3.2))"
#         self.assertTrue(TestChecker().test(input, expect, 502))

#     def test_3(self):
#         input = """a: float = 3;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 503))

#     def test_4(self):
#         input = """arra2 : array [2,3] of integer = {{2,1,2},{3,1,1}};"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 504))

#     def test_5(self):
#         input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4,"hello"} } };"""
#         expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(3), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(4)]), ArrayLit([IntegerLit(1), IntegerLit(5)])]), ArrayLit([ArrayLit([IntegerLit(4), IntegerLit(3)]), ArrayLit([IntegerLit(2), IntegerLit(1)]), ArrayLit([IntegerLit(5), IntegerLit(4), StringLit(hello)])])])"
#         self.assertTrue(TestChecker().test(input, expect, 505))

#     def test_6(self):
#         input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
# array2 : array [3,2] of integer = array1[2,1,3];"""
#         expect = "Type mismatch in Variable Declaration: VarDecl(array2, ArrayType([3, 2], IntegerType), ArrayCell(array1, [IntegerLit(2), IntegerLit(1), IntegerLit(3)]))"
#         self.assertTrue(TestChecker().test(input, expect, 506))

# #     def test_7(self):
# #         input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
# # array2 : array [3,2] of integer = array1[2];
# # a: float = array2[2,1];"""
# #         expect = "No entry point"
# #         self.assertTrue(TestChecker().test(input, expect, 507))

# #     def test_8(self):
# #         input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
# # array2 : array [3,2] of integer = array1[2];
# # a: float = array2[2,1];
# # a: integer = 3;"""
# #         expect = "Redeclared Variable: a"
# #         self.assertTrue(TestChecker().test(input, expect, 508))

# #     def test_9(self):
# #         input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
# # array2 : array [3,2] of integer = array1[2];
# # a: float = array2[2,1];
# # array3 : array [3,2] of integer = array2;"""
# #         expect = "No entry point"
# #         self.assertTrue(TestChecker().test(input, expect, 509))

#     def test_10(self):
#         input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
# array2 : array [3,2] of integer = array1[2];
# a: float = array2[2,1];
# array3 : array [3,2] of integer = array2;
# bcd : auto = array1[2];
# array4 : array [3,2] of integer = bcd;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 510))

#     def test_11(self):
#         input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
# array2 : array [3,2] of integer = array1[2];
# a: float = array2[2,1];
# array3 : array [3,2] of integer = array2;
# bcd : auto = array1[2];
# array4 : array [3,2] of float = bcd;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 511))

#     def test_12(self):
#         input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
# array2 : array [3,2] of integer = array1[2];
# a: float = array2[2,1];
# array3 : array [3,2] of integer = array2;
# bcd : auto = array1[2];
# array4 : array [3,2] of float = bcd;
# b: array[2]of float  = array2[array3];"""
#         expect = "Type mismatch in expression: Id(array3)"
#         self.assertTrue(TestChecker().test(input, expect, 512))

#     def test_13(self):
#         input = """a: integer;
# b: auto = a;

# foo: function void () {
#     a = 3;
#     b = 2;
# }"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 513))

#     def test_14(self):
#         input = """a: integer;
# b: auto = a;

# main: function void () {
#     a : float;

#     b : auto = 2.1;
#     a = b;
#     {a = foo(2,3);}
# }"""
#         expect = "Undeclared Function: foo"
#         self.assertTrue(TestChecker().test(input, expect, 514))

#     def test_15(self):
#         input = """main:function void() inherit foo{
#     super(12);
#     y:auto = foo(1);
#     foo2();
#     arr:array[2,2] of integer = {{1,2}, {1,2}};
#     arr[1,2,3] = 1;
# }
# foo:function float(x:integer){
#     return x + 1.2;
# }
# foo2: function void(){}"""
#         expect = "Type mismatch in expression: ArrayCell(arr, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])"
#         self.assertTrue(TestChecker().test(input, expect, 515))

#     def test_16(self):
#         input = """main : function void() inherit foo{
#     super(1.0, 2.0, 3.0);
#     z: boolean = true;
#     x:string = "abc";
#     y = 3.2;
# }
# foo : function auto(inherit x : auto, inherit y : auto, z : auto){
#     //x = true;
#     z = 2;
#     return x + y + z;
# }"""
#         expect = "Redeclared Variable: x"
#         self.assertTrue(TestChecker().test(input, expect, 516))

#     def test_17(self):
#         input = """foo: function integer(){}

# main: function void(){

# 	foo: integer = 3;

# 	a: integer;

# 	a = foo(); // line 5

# }"""
#         expect = "Type mismatch in expression: FuncCall(foo, [])"
#         self.assertTrue(TestChecker().test(input, expect, 517))

#     def test_18(self):
#         input = """a: integer = 1;

# foo: function void (b: integer) inherit a {}

# a: function string (inherit c: string) {}"""
#         expect = "Invalid statement in function: foo"
#         self.assertTrue(TestChecker().test(input, expect, 518))

#     def test_19(self):
#         input = """foo: function auto (inherit out z: auto, t:auto) {
#     z = 5;
#     return z + t;
# }

# a:auto = foo(2.0, 2);
# b:auto = foo(3.0, 1);
# c: float = a + b;"""
#         expect = "Type mismatch in expression: FuncCall(foo, [FloatLit(2.0), IntegerLit(2)])"
#         self.assertTrue(TestChecker().test(input, expect, 519))

#     def test_20(self):
#         input = """main: function auto (){
#     if (1==2) {
#         return 1;
#     }
#     return;
# }
# """
#         expect = "Type mismatch in statement: ReturnStmt()"
#         self.assertTrue(TestChecker().test(input, expect, 520))

#     def test_21(self):
#         input = """main: function auto (){
#     if (1==2) {
#         return;
#     }
#     return;
# }

# a: array [2] of integer = {{2},{3}};
# """
#         expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([ArrayLit([IntegerLit(2)]), ArrayLit([IntegerLit(3)])]))"
#         self.assertTrue(TestChecker().test(input, expect, 521))

#     def test_22(self):
#         input = """a :auto = {3,2,1};
# main: function auto (){
#     a = 3*"abc";
# }

# a: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Type mismatch in statement: AssignStmt(Id(a), BinExpr(*, IntegerLit(3), StringLit(abc)))"
#         self.assertTrue(TestChecker().test(input, expect, 522))

#     def test_23(self):
#         input = """a :auto = 2;
# main: function auto (){
#     a = 3*"abc";
# }

# a: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Type mismatch in expression: BinExpr(*, IntegerLit(3), StringLit(abc))"
#         self.assertTrue(TestChecker().test(input, expect, 523))

#     def test_24(self):
#         input = """a :auto = 2;
# main: function auto (){
#     x:integer = x + x;
# }

# a: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker().test(input, expect, 524))

#     def test_25(self):
#         input = """a :auto = 2;
# main: function auto (){
#     x:auto = x + x;
# }

# a: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker().test(input, expect, 525))

#     def test_26(self):
#         input = """a :auto = 2;
# main: function auto (){
#     printInteger(2);
#     foo(3,2);
# }

# foo: function auto (a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Type mismatch in statement: AssignStmt(Id(a), StringLit(abc))"
#         self.assertTrue(TestChecker().test(input, expect, 526))

#     def test_27(self):
#         input = """a :auto = 2;

# foo: function auto (a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }

# main: function auto (){
#     printInteger(2);
#     foo(3,2);
# }



# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(3), IntegerLit(2))"
#         self.assertTrue(TestChecker().test(input, expect, 527))

#     def test_28(self):
#         input = """a :auto = 2;

# foo: function auto (a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }

# main: function auto (){
#     printInteger(2.3);
#     foo(3,2);
# }



# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Type mismatch in statement: CallStmt(printInteger, FloatLit(2.3))"
#         self.assertTrue(TestChecker().test(input, expect, 528))

#     def test_29(self):
#         input = """a :auto = 2;

# foo: function auto (a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }

# main: function auto (){
#     writeFloat(2);
#     foo(3,2);
# }



# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(3), IntegerLit(2))"
#         self.assertTrue(TestChecker().test(input, expect, 529))

#     def test_30(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit foo {

# }
# main: function auto (){
#     writeFloat(2);
#     foo(3,2);
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Invalid statement in function: bar"
#         self.assertTrue(TestChecker().test(input, expect, 530))

#     def test_31(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit foo {
#     super("ab",2);
# }
# main: function auto (){
#     writeFloat(2);
#     foo(3,2);
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Invalid Parameter: a"
#         self.assertTrue(TestChecker().test(input, expect, 531))

#     def test_32(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit foo {
#     preventDefault();
# }
# main: function auto (){
#     writeFloat(2);
#     foo(3,2);
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(3), IntegerLit(2))"
#         self.assertTrue(TestChecker().test(input, expect, 532))

#     def test_33(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit foo {
#     preventDefault(true,2,1);
# }
# main: function auto (){
#     writeFloat(2);
#     foo(3,2);
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Type mismatch in expression: BooleanLit(True)"
#         self.assertTrue(TestChecker().test(input, expect, 533))

#     def test_34(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     super(3,2);
#     a: auto = 3;
#     return a;
# }
# main: function auto (){
#     writeFloat(2);
#     foo("a",2);
# }

# b: array [2,1] of integer = {{2},{3}, {2}};
# """
#         expect = "Type mismatch in Variable Declaration: VarDecl(b, ArrayType([2, 1], IntegerType), ArrayLit([ArrayLit([IntegerLit(2)]), ArrayLit([IntegerLit(3)]), ArrayLit([IntegerLit(2)])]))"
#         self.assertTrue(TestChecker().test(input, expect, 534))

#     def test_35(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (inherit a: integer, d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     super(3,2);
#     a: auto = 3;
#     return a;
# }
# main: function auto (){
#     writeFloat(2);
#     foo("a",2);
# }

# b: array [2,1] of integer = {{2},{3}, {2}};
# """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker().test(input, expect, 535))

#     def test_36(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     super(3,2);
#     a: auto = 3;
#     return a;
# }
# main: function auto (){
#     writeFloat(2);
#     foo("a",2);
# }

# b: array [2,1] of integer = {{2},{3}, {2}};
# """
#         expect = "Type mismatch in Variable Declaration: VarDecl(b, ArrayType([2, 1], IntegerType), ArrayLit([ArrayLit([IntegerLit(2)]), ArrayLit([IntegerLit(3)]), ArrayLit([IntegerLit(2)])]))"
#         self.assertTrue(TestChecker().test(input, expect, 536))

#     def test_37(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     super(3,2);
#     d: auto = 3;
#     return a;
# }
# main: function auto (){
#     writeFloat(2);
#     foo("a",2);
#     bar(d, c);
# }

# b: array [2,1] of integer = {{2},{3}, {2}};
# """
#         expect = "Undeclared Identifier: d"
#         self.assertTrue(TestChecker().test(input, expect, 537))

#     def test_38(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     super(3,2);
#     d: auto = 3;
#     return a;
# }
# main: function auto (){
#     writeFloat(2);
#     for (i = 3, i < 5, i+1)
#         printInteger(i);
# }

# b: array [2,1] of integer = {{2},{3}, {2}};
# """
#         expect = "Undeclared Identifier: i"
#         self.assertTrue(TestChecker().test(input, expect, 538))

#     def test_39(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     super(3,2);
#     d: auto = 3;
#     return a;
# }

# test2: function auto (i: auto){
#     writeFloat(2);
    
#     for (i = 3, i < 5, i+1)
#         printInteger(i);
# }

# main: function auto(){
#     return;
# }

# a: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker().test(input, expect, 539))

#     def test_40(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     super(3,2);
#     d: auto = 3;
#     return a;
# }

# test2: function auto (i: auto){
#     writeFloat(2);
#     break;
#     for (i = 3, i < 5, i+1)
#         printInteger(i);
# }

# main: function auto(){
#     return;
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Must in loop: BreakStmt()"
#         self.assertTrue(TestChecker().test(input, expect, 540))

#     def test_41(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     super(3,2);
#     d: auto = 3;
#     return a;
# }

# test2: function auto (i: auto){
#     writeFloat(2);
    
#     for (i = 3, i < 5, i+1)
#         break;
        
# }

# main: function auto(){
#     return;
# }

# a: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker().test(input, expect, 541))

#     def test_42(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar2 {
#     super(3,2);
#     d: auto = 3;
#     return a;
# }

# test2: function auto (i: auto){
#     writeFloat(2);
    
#     for (i = 3, i < 5, i+1)
#         printInteger(i);
# }

# main: function auto(){
#     return;
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Undeclared Function: bar2"
#         self.assertTrue(TestChecker().test(input, expect, 542))

#     def test_43(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     super(3,2);
#     d: auto = 3;
#     return a;
# }

# test2: function auto (i: auto){
#     writeFloat(2);
    
#     for (i = 3, i < 5, i+1)
#         if (a == 2) return 3;
#         else if (i % 2 == 0) return 2;
#         else continue;
# }

# main: function auto(){
#     return;
# }

# a: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker().test(input, expect, 543))

#     def test_44(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     super(3,2);
#     d: auto = 3;
#     return a;
# }

# test2: function auto (i: auto){
#     writeFloat(2);
    
#     for (i = 3, i < 5, i+1)
#     {
#         if (a == 2) return 3;
#         else if (i % 2 == 0) return 2;
#         else continue;
#         break;
#         return 1.2;
#     }
# }

# main: function auto(){
#     return;
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Type mismatch in statement: ReturnStmt(FloatLit(1.2))"
#         self.assertTrue(TestChecker().test(input, expect, 544))

#     def test_45(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, inherit d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     super(3,2);
#     d: auto = 3;
#     return a;
# }

# test2: function auto (i: auto){
#     writeFloat(2);
    
#     do
#     {
#         if (a == 2) return 3;
#         else if (i % 2 == 0) return 2;
#         else continue;
#         break;
#     }
#     while(true);
#     return 1.2;
# }

# main: function auto(){
#     return;
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Redeclared Variable: d"
#         self.assertTrue(TestChecker().test(input, expect, 545))

#     def test_46(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, inherit d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     preventDefault();
#     d: auto = 3;
#     return a;
# }

# test2: function auto (i: auto) inherit bar{
#     super(2, 3);
#     writeFloat(2);
    
#     do
#     {
#         if (a == 2) return 3.1;
#         else if (i % 2 == 0) return 2;
#         else continue;
#         break;
#     }
#     while(true);
#     return 1.2;
#     d = foo("ab",2);

# }

# main: function auto(){
#     return;
# }

# a: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker().test(input, expect, 546))

#     def test_47(self):
#         input = """a :auto = 2;

# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, inherit d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     preventDefault();
#     d: auto = 3;
#     return a;
# }

# test2: function auto (i: auto) inherit bar{
#     super(2, 3);
#     writeFloat(2);
    
#     do
#     {
#         if (a == 2) return 3.1;
#         else if (i % 2 == 0) return 2;
#         else continue;
#         break;
#     }
#     while(true);
#     return 1.2;
#     a = foo("ab",2);
#     k = 3;

# }

# main: function auto(){
#     return;
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Undeclared Identifier: k"
#         self.assertTrue(TestChecker().test(input, expect, 547))

#     def test_48(self):
#         input = """a :auto = 2;
# o : auto = {{1},{2}};
# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, inherit d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     preventDefault();
#     d: auto = 3;
#     return a;
# }

# test2: function auto (i: auto) inherit bar{
#     super(2, 3);
#     writeFloat(2);
    
#     do
#     {
#         for (o[0] = 3,o[0] > 1, o[1]+1)
#             if (a == 2) return 3.1;
#             else if (i % 2 == 0) return 2;
#             else continue;
#         break;
#     }
#     while(true);
#     return 1.2;
#     a = foo("ab",2);
   

# }

# main: function auto(){
#     return;
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Type mismatch in statement: ForStmt(AssignStmt(ArrayCell(o, [IntegerLit(0)]), IntegerLit(3)), BinExpr(>, ArrayCell(o, [IntegerLit(0)]), IntegerLit(1)), BinExpr(+, ArrayCell(o, [IntegerLit(1)]), IntegerLit(1)), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), ReturnStmt(FloatLit(3.1)), IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), ReturnStmt(IntegerLit(2)), ContinueStmt())))"
#         self.assertTrue(TestChecker().test(input, expect, 548))

#     def test_49(self):
#         input = """a :auto = 2;
# o : auto = {{1},{2}};
# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, inherit d: auto) inherit test {
#     foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     preventDefault();
#     d: auto = 3;
#     return a;
# }

# test2: function auto (i: auto) inherit bar{
#     super(2, 3);
#     writeFloat(2);
    
#     do
#     {
#         while (false)
#             for (o[0,0] = 3,o[0,0] > 1, o[1,0]+1)
#                 if (a == 2) return 3.1;
#                 else if (i % 2 == 0) return 2;
#                 else continue;
#         break;
#     }
#     while(true);
#     break;
#     return 1.2;
#     a = foo("ab",2);
   

# }

# main: function auto(){
#     return;
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Must in loop: BreakStmt()"
#         self.assertTrue(TestChecker().test(input, expect, 549))

#     def test_50(self):
#         input = """a :auto = 2;
# o : auto = {{1},{2}};
# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, inherit d: auto) inherit test {
#     //foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     preventDefault();
#     d: auto = 3;
#     return a;
# }

# test2: function auto (i: auto) inherit bar{
#     super(2, 3);
#     writeFloat(2);
    
#     do
#     {
#         while (false)
#             for (o[0,0] = bar2(),o[0,0] > 1, o[0,1]+1)
#                 if (a == 2) return 3.1;
#                 else if (i % 2 == 0) return 2;
#                 else continue;
#         break;
#     }
#     while(true);
#     break;
#     return 1.2;
#     a = foo("ab",2);
   

# }
# bar2: function auto () {

#     return 1;
# }
# main: function auto(){
#     return;
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Must in loop: BreakStmt()"
#         self.assertTrue(TestChecker().test(input, expect, 550))

#     def test_51(self):
#         input = """a :auto = 2;
# o : auto = {{1},{2}};
# foo: function auto (inherit a: auto, b: auto) inherit main {
#     x:integer = a + b;
#     a = "abc";
#     return 2;
# }


# bar: function string (a: integer, inherit d: auto) inherit test {
#     //foo("ab", 2.4);
#     arr1 : auto = {{3,2},{2,1}};
#     return "done";
# }

# test: function integer () inherit bar {
#     preventDefault();
#     d: auto = 3;
#     return a;
# }

# test2: function auto (i: auto) inherit bar{
#     super(2, 3);
#     writeFloat(2);
    
#     do
#     {
#         while (false)
#             for (o[1,0] = bar2(),o[0,0] > 1, o[0,1]+1)
#                 if (a == 2) return 3.1;
#                 else if (i % 2 == 0) return 2;
#                 else continue;
#         break;
#     }
#     while(true);
#     break;
#     return 1.2;
#     a = foo("ab",2);
   

# }
# bar2: function auto () {

#     return 1.2;
# }
# main: function auto(){
#     return;
# }

# b: array [2,1] of integer = {{2},{3}};
# """
#         expect = "Type mismatch in statement: AssignStmt(ArrayCell(o, [IntegerLit(1), IntegerLit(0)]), FuncCall(bar2, []))"
#         self.assertTrue(TestChecker().test(input, expect, 551))

#     def test_52(self):
#         input = """main : function void() inherit foo{
#     super(1.0, 2.0, 3.0);
#     z: integer = foo(1,2,3) + 1;
#     x = "abc";
#     y = true;
# }
# foo : function auto(inherit x : auto, inherit y : auto, z : auto){
#     x = true;
#     return x + y + z;
# }"""
#         expect = "Type mismatch in statement: AssignStmt(Id(x), BooleanLit(True))"
#         self.assertTrue(TestChecker().test(input, expect, 552))

#     def test_53(self):
#         input = """foo: function void (b: auto, c: auto){

# 	a: string = b + c;

# }"""
#         expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(+, Id(b), Id(c)))"
#         self.assertTrue(TestChecker().test(input, expect, 553))

#     def test_54(self):
#         input = """inc : function void (out n : integer, n: float) inherit foo{
#       super(0.1, 1);
#       n: string = 124;    
# } 
# foo : function auto (inherit n: float, b: integer){}"""
#         expect = "Invalid Parameter: n"
#         self.assertTrue(TestChecker().test(input, expect, 554))

#     def test_55(self):
#         input = """foo: function integer(){}

# main: function void(){

# 	foo: integer = 3;

# 	a: integer;

# 	a = foo();

# }"""
#         expect = "Type mismatch in expression: FuncCall(foo, [])"
#         self.assertTrue(TestChecker().test(input, expect, 555))

#     def test_56(self):
#         input = """M: function void (a: integer) inherit N {} 

# N: function void (inherit a: integer) {}"""
#         expect = "Invalid statement in function: M"
#         self.assertTrue(TestChecker().test(input, expect, 556))

#     def test_57(self):
#         input = """main: function void () {
#     b: float = foo() > bar();
# }

# foo: function auto () {
    
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
# }"""
#         expect = "Type mismatch in Variable Declaration: VarDecl(b, FloatType, BinExpr(>, FuncCall(foo, []), FuncCall(bar, [])))"
#         self.assertTrue(TestChecker().test(input, expect, 557))

#     def test_58(self):
#         input = """main: function void () {
#     b: boolean = foo() > bar();
# }

# foo: function auto () {
    
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
# }

# a: function auto () inherit bar1 {}"""
#         expect = "Undeclared Function: bar1"
#         self.assertTrue(TestChecker().test(input, expect, 558))

#     def test_59(self):
#         input = """main: function void () {
#     b: float ;
#     b = foo() > bar();
# }

# foo: function auto () {
    
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Type mismatch in statement: AssignStmt(Id(b), BinExpr(>, FuncCall(foo, []), FuncCall(bar, [])))"
#         self.assertTrue(TestChecker().test(input, expect, 559))

# #     def test_60(self):
# #         input = """main: function void () {
# #     b: string;
# #     b = foo() :: bar();
# # }

# # foo: function auto () {
    
# # }
# # bar: function auto() {
# #     a:auto = {{2},{3}};
# # }
# # a: function auto () inherit bar1 {}"""
# #         expect = "Undeclared Function: bar1"
# #         self.assertTrue(TestChecker().test(input, expect, 560))

#     def test_61(self):
#         input = """main: function void () {
#     b: boolean ;
#     b = foo() > bar();
# }

# foo: function auto () {
#     return 3;
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Undeclared Function: bar1"
#         self.assertTrue(TestChecker().test(input, expect, 561))

#     def test_62(self):
#         input = """main: function void () {
#     b: boolean ;
#     b = foo() > bar();
# }

# foo: function auto () {
#     return 3;
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
#     return 2.1;
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Undeclared Function: bar1"
#         self.assertTrue(TestChecker().test(input, expect, 562))

#     def test_63(self):
#         input = """main: function void () {
#     b: boolean ;
#     b = foo() > bar();
# }

# foo: function auto () {
#     return 3;
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
#     foo: integer = 3;
#     foo();
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Type mismatch in expression: CallStmt(foo, )"
#         self.assertTrue(TestChecker().test(input, expect, 563))

#     def test_64(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > bar();
# }

# foo: function array[2,1] of integer () {
#     return 3;
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Type mismatch in statement: ReturnStmt(IntegerLit(3))"
#         self.assertTrue(TestChecker().test(input, expect, 564))

#     def test_65(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > bar();
# }

# foo: function array[2,1] of integer () {
#     return 3;
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Type mismatch in statement: ReturnStmt(IntegerLit(3))"
#         self.assertTrue(TestChecker().test(input, expect, 565))

#     def test_66(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > bar();
# }

# foo: function array[2,1] of integer () {
#     return {{2},{1}};
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Undeclared Function: bar1"
#         self.assertTrue(TestChecker().test(input, expect, 566))

#     def test_67(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > bar();
#     a:auto = readInteger();
#     c = a%2;
#     printInteger(c);
# }

# foo: function array[2,1] of integer () {
#     return {{2},{1}};
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Type mismatch in statement: AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(2)))"
#         self.assertTrue(TestChecker().test(input, expect, 567))

#     def test_68(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > bar();
#     a:auto = readInteger();
#     {
#         c:integer = a%2;
#     }
#     printInteger(c);
# }

# foo: function array[2,1] of integer () {
#     return {{2},{1}};
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Type mismatch in statement: CallStmt(printInteger, Id(c))"
#         self.assertTrue(TestChecker().test(input, expect, 568))

#     def test_69(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > bar();
#     a:auto = readInteger();
#     {
#         c:integer = a%2;
#         printInteger(c);
#     }
# }

# foo: function array[2,1] of integer () {
#     return {{2},{1}};
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Undeclared Function: bar1"
#         self.assertTrue(TestChecker().test(input, expect, 569))

#     def test_70(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > bar();
#     a:auto = printInteger();
#     {
#         c:integer = a%2;
#         printInteger(c);
#     }
# }

# foo: function array[2,1] of integer () {
#     return {{2},{1}};
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Type mismatch in expression: FuncCall(printInteger, [])"
#         self.assertTrue(TestChecker().test(input, expect, 570))

#     def test_71(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > bar();
#     a:float = readInteger();
#     {
#         a: auto = {{{2},{1}}};
#         c:integer = a[0,0,0]%2;
#     }
#     printInteger(a);
# }

# foo: function array[2,1] of integer () {
#     return {{2},{1}};
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Type mismatch in statement: CallStmt(printInteger, Id(a))"
#         self.assertTrue(TestChecker().test(input, expect, 571))

#     def test_72(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > bar();
#     a:auto = readInteger();
#     {
#         c:integer = a%2;
#     }
#     writeFloat(a);
# }

# foo: function array[2,1] of integer () {
#     return {{2},{1}};
# }
# bar: function auto() {
#     a:auto = {{2},{3}};
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Undeclared Function: bar1"
#         self.assertTrue(TestChecker().test(input, expect, 572))

#     def test_73(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > 3;
#     a:auto = readInteger();
#     {
#         c:integer = a%2;
#     }
#     writeFloat(a);
# }

# barr: function auto() {
#     return 2;
# }

# foo: function array[2,1] of integer () inherit bar {
#     super({{{1,3},{3,1}}, {{barr(),4},{1,3}}}, {3,2,barr()});
#     b[2] = 3 - 3;
# }
# bar: function auto(inherit a : auto, b: auto) {
#     a[2,1,2] = a[2,1,1] + b[1,2];
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Undeclared Identifier: b"
#         self.assertTrue(TestChecker().test(input, expect, 573))

#     def test_74(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > 3;
#     a:auto = readInteger();
#     {
#         c:integer = a%2;
#     }
#     writeFloat(a);
# }

# barr: function auto() {
#     return 2;
# }

# foo: function array[2,1] of integer () inherit bar {
#     super({{{1,3},{3,1}}, {{barr(),4},{1,3}}}, {3,2,barr()});
#     b[2] = 3 - 3;
# }
# bar: function auto(inherit a : auto, inherit b: auto) {
#     a[2,1,2] = a[2,1,1] + b[1,2];
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Type mismatch in expression: ArrayCell(b, [IntegerLit(1), IntegerLit(2)])"
#         self.assertTrue(TestChecker().test(input, expect, 574))

#     def test_75(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > 3;
#     a:auto = readInteger();
#     {
#         c:integer = a%2;
#     }
#     writeFloat(a);
# }

# barr: function auto() {
#     return 2;
# }

# foo: function array[2,1] of integer () inherit bar {
#     super({{{1,3},{3,1}}, {{barr(),4},{1,3}}}, {3,2,barr()});
#     b[2] = 3 - 3;
# }
# bar: function auto(inherit a : auto, inherit b: auto) {
#     a[2,1,2] = a[2,1,1] + b[2];
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Undeclared Function: bar1"
#         self.assertTrue(TestChecker().test(input, expect, 575))

#     def test_76(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > 3;
#     a:auto = readInteger();
#     {
#         c:integer = a%2;
#     }
#     writeFloat(a);
# }

# barr: function auto() {
#     return 2;
# }

# foo: function array[2,1] of integer () inherit bar {
#     preventDefault();
#     b:float = 3;
#     b = b - 3;

# }
# bar: function auto(inherit a : auto, inherit b: auto) {
#     a[2,1,2] = a[2,1,1] + b[1,2];
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Type mismatch in expression: ArrayCell(a, [IntegerLit(2), IntegerLit(1), IntegerLit(2)])"
#         self.assertTrue(TestChecker().test(input, expect, 576))

#     def test_77(self):
#         input = """main: function void () {
#     b: boolean ;
#     a:auto = readInteger();
#     {
#         c:integer = a%2;
#     }
#     writeFloat(a);
# }
# bar: function integer () {}
# foo: function void (i: auto, j: auto) {
#     bar: integer = 3;
#     for (i = 1, i < 100, i+2) {
#         a: array[2] of integer = {3,bar};
#         for (j = 1, j < bar(), j+1)
#            printInteger(a[j]);
#     }
# }"""
#         expect = "Type mismatch in expression: FuncCall(bar, [])"
#         self.assertTrue(TestChecker().test(input, expect, 577))

#     def test_78(self):
#         input = """main: function void () {
#     b: boolean ;
#     a:auto = readInteger();
#     {
#         c:integer = a%2;
#     }
#     writeFloat(a);
# }
# bar: function integer () {}
# foo: function void (i: auto, j: auto) {
   
#     for (i = 1, i < 100, i+2) {
#         a: array[2] of integer = {3,bar};
#         for (j = 1, j < bar(), j+1)
#            printInteger(a[j]);
#     }
# }"""
#         expect = "Undeclared Identifier: bar"
#         self.assertTrue(TestChecker().test(input, expect, 578))

#     def test_79(self):
#         input = """bar: function void () {
#     a: array[2] of integer = {3,2};
#     a[foo()] = 4;
# }

# foo: function auto () {return 3;}"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 579))

# #     def test_80(self):
# #         input = """bar: function void () {
# #     a: array[2] of integer = {3,2};
# #     a[foo()] = 4;
# # }

# # foo: function auto () {return;}"""
# #         expect = "Type mismatch in expression: FuncCall(foo, [])"
#         self.assertTrue(TestChecker().test(input, expect, 580))

#     def test_81(self):
#         input = """bar: function void () {
#     a: array[2] of integer = {3,2};
#     a[foo()] = 4;
# }

# test: function void() {
#     a:float = foo() + 2.3;
#     printInteger(foo());
# }

# foo: function auto () {}"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 581))

#     def test_82(self):
#         input = """bar: function void () {
#     a: array[2] of integer = {3,2};
#     a[foo()] = 4;
# }
# a:auto = 3;
# test: function void() {
#    a:string = a;
# }

# foo: function auto () {}"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 582))

#     def test_83(self):
#         input = """bar: function void () {
#     a: array[2] of integer = {3,2};
#     a[foo()] = 4;
# }
# a:auto = 3;
# test: function void() {
#    a:string = a;
# }

# foo: function auto () {}"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 583))

#     def test_84(self):
#         input = """bar: function void () {
#     a: array[2] of integer = {{3,2,1},{2,1}, {1,4}};
#     a[foo()] = 4;
# }

# foo: function auto () {}"""
#         expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(3), IntegerLit(2), IntegerLit(1)]), ArrayLit([IntegerLit(2), IntegerLit(1)]), ArrayLit([IntegerLit(1), IntegerLit(4)])])"
#         self.assertTrue(TestChecker().test(input, expect, 584))

#     def test_85(self):
#         input = """bar: function void () {
#     a: array[2] of integer = {{3,2,1},{2,1,1}, {1,"abc",4}};
#     a[foo()] = 4;
# }

# foo: function auto () {}"""
#         expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(3), IntegerLit(2), IntegerLit(1)]), ArrayLit([IntegerLit(2), IntegerLit(1), IntegerLit(1)]), ArrayLit([IntegerLit(1), StringLit(abc), IntegerLit(4)])])"
#         self.assertTrue(TestChecker().test(input, expect, 585))

#     def test_86(self):
#         input = """bar: function void () {
#     a: auto = {{3,2,1},{2,1,1}, {1,2,4}};
#     b: auto = {{4,8,7},{1,3,1}, {2,1}};
    
# }

# foo: function auto () {}"""
#         expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(4), IntegerLit(8), IntegerLit(7)]), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(1)]), ArrayLit([IntegerLit(2), IntegerLit(1)])])"
#         self.assertTrue(TestChecker().test(input, expect, 586))

#     def test_87(self):
#         input = """bar: function void () {
#     a: auto = {{3,2,1},{2,1,1}, {1,2,4}};
#     b: auto = {{4,8,7},{1,3,1}, {2,1,1}};
    
# }

# foo: function auto () {}"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 587))

#     def test_88(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > 3;
#     a:auto = readInteger();
#     {
#         c:integer = a%2;
#     }
#     writeFloat(a);
# }

# barr: function auto() {
#     return 2.2;
# }

# foo: function array[2,1] of integer () inherit bar {
#     super({{{1,3},{3,1}}, {{barr(),4},{1,3}}}, {3,2,barr()});
#     b[2] = 3 - 3;
# }
# bar: function auto(inherit a : auto, inherit b: auto) {
#     a[2,1,2] = a[2,1,1] + b[1,2];
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(1)])]), ArrayLit([ArrayLit([FuncCall(barr, []), IntegerLit(4)]), ArrayLit([IntegerLit(1), IntegerLit(3)])])])"
#         self.assertTrue(TestChecker().test(input, expect, 588))

#     def test_89(self):
#         input = """main: function void () {
#     b: boolean ;
#     c:auto = foo();
#     b = c[0,1] > 3;
#     a:auto = readInteger();
#     {
#         c:integer = a%2;
#     }
#     writeFloat(a);
# }

# barr: function auto() {
#     return 2;
# }

# foo: function array[2,1] of integer () inherit bar {
#     super({{{1,3},{3,1}}, {{barr(),4},{1,3}}}, {3,2,barr()});
#     c: auto = {{{5,3},{3,1}}, {{4},{1,3}}};
#     b[2] = 3 - 3;
# }
# bar: function auto(inherit a : auto, inherit b: auto) {
#     a[2,1,2] = a[2,1,1] + b[1,2];
# }
# a: function auto () inherit bar1 {}"""
#         expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(5), IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(1)])]), ArrayLit([ArrayLit([IntegerLit(4)]), ArrayLit([IntegerLit(1), IntegerLit(3)])])])"
#         self.assertTrue(TestChecker().test(input, expect, 589))

# #     def test_90(self):
# #         input = """a :auto = 2;

# # foo: function auto (inherit a: auto, b: auto) inherit main {
# #     x:integer = a + b;
# #     a = "abc";
# #     return 2;
# # }


# # bar: function string (a: integer, d: auto) inherit test {
# #     foo("ab", 2.4);
# #     arr1 : auto = {{3,2},{2,1}};
# #     return "done";
# # }

# # test: function integer () inherit bar {
# #     super(3,2);
# #     d: auto = 3;
# #     return a;
# # }
# # main: function auto (){
# #     writeFloat(2);
# #     for (i = 3, i < 5, i+1)
# #         printInteger(i);
# # }

# # b: array [2,1] of integer = {{2},{3}, {2}};
# # """
# #         expect = "Undeclared Identifier: i"
#         self.assertTrue(TestChecker().test(input, expect, 590))

#     def test_91(self):
#         input = """var: auto = {3_2,3,4,1,2,3};
#     i: integer = foo(3.333e9, var[3]);
#     e: float = i;
#     flag: boolean = false;
#     inc : function void (out o: integer, a:float) inherit foo{
#         preventDefault();
#         a: float = foo(n, 2);
#     }
#     foo : function auto (inherit n: float, n: integer){}"""
#         expect = "Redeclared Parameter: n"
#         self.assertTrue(TestChecker().test(input, expect, 591))

#     def test_92(self):
#         input = """var: auto = {32,3,4,1,2,3};
# i: integer = test2();
# e: float = i;
# flag2: boolean = true;
# func: function string(inherit f: boolean, y: integer) inherit test{
#     while(i != 2) {
#         break;
#     }
#     return "done";
# }
# test2: function auto() {
#     for (i=2, i!=var[0], i+1) {
#         break;
#         return i;
#     }
# }
# foo: function auto(bar: string, boo: float) inherit func {
#     var: integer = 2;
# }"""
#         expect = "Undeclared Function: test"
#         self.assertTrue(TestChecker().test(input, expect, 592))

    def test_93(self):
        input = """var: auto = {32,3,4,1,2,3};
i: integer = test2();
e: float = i;
flag2: boolean = true;
func: function string(inherit f: boolean, y: integer) inherit test2{
    while(i != 2) {
        break;
    }
    return "done";
}
test2: function auto() {
    for (i=2, i!=var[0], i+1) {
        break;
        return i;
    }
}
foo: function auto(bar: string, boo: float) inherit func {
    var: integer = 2;
}"""
        expect = "Redeclared Function: test2"
        self.assertTrue(TestChecker().test(input, expect, 593))

#     def test_94(self):
#         input = """avar: auto = {32,3,4,1,2,3};
# i: integer = test(3.2e-1);
# test: function auto(inherit a: float) {
#     for (i=9, i<10, i+1) {
#         while (avar[3] + i) {
#             i = avar[i] % 3;
#             a = func(avar[3], i);
#         }
        
#     }
# }
# func: function void(f: boolean, y: integer) inherit test{
#     super(avar);
#     return f;
# }"""
#         expect = "Type mismatch in statement: WhileStmt(BinExpr(+, ArrayCell(avar, [IntegerLit(3)]), Id(i)), BlockStmt([AssignStmt(Id(i), BinExpr(%, ArrayCell(avar, [Id(i)]), IntegerLit(3))), AssignStmt(Id(a), FuncCall(func, [ArrayCell(avar, [IntegerLit(3)]), Id(i)]))]))"
#         self.assertTrue(TestChecker().test(input, expect, 594))

#     def test_95(self):
#         input = """a: integer;
# b: auto = a;

# main: function void () {
#     a : float;

#     b : auto = 2.1;
#     a = b;
#     {a = foo(2,3);}
# }"""
#         expect = "Undeclared Function: foo"
#         self.assertTrue(TestChecker().test(input, expect, 595))

#     def test_96(self):
#         input = """test: function auto (e: auto) {}
# func: function string(f: boolean, y: integer) inherit test{
#     super(3);
#     while(1 != 2) {
#         break;
#     }
#     return s;
# }
# arr: array [4] of float = {1.3, 20e-2, 4.2, 5};"""
#         expect = "Undeclared Identifier: s"
#         self.assertTrue(TestChecker().test(input, expect, 596))

#     def test_97(self):
#         input = """test: function auto (e: auto) {}
# func: function string(f: boolean, y: integer) inherit test{
#     super(3);
#     s:auto = "hello world!";
#     while(1 != 2) {
#         break;
#     }
#     return s;
# }
# arr: array [4] of float = {1.3, 20e-2, 4.2, 5};"""
#         expect = "Illegal array literal: ArrayLit([FloatLit(1.3), FloatLit(0.2), FloatLit(4.2), IntegerLit(5)])"
#         self.assertTrue(TestChecker().test(input, expect, 597))

# #     def test_98(self):
# #         input = """var: auto = {32,3,4,1,2,3};
# # inc : function void (out n: integer, a:float) inherit foo{}
# # foo : function auto (inherit n: float, n: integer){}"""
# #         expect = "Invalid statement in function: inc"
# #         self.assertTrue(TestChecker().test(input, expect, 598))

#     def test_99(self):
#         input = """a, B, c: array [3] of boolean ={true,true,true},{true,true,true},{true,false,true};
# foo: function void () {
#     printBoolean(false);
# }"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 599))

    def test_0(self):
        input = """a: auto;"""
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker().test(input, expect, 500))

    def test_1(self):
        input = """delta: integer = 3;"""
        expect = "No entry point"
        self.assertTrue(TestChecker().test(input, expect, 501))

    def test_2(self):
        input = """a: integer = 3.2;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(3.2))"
        self.assertTrue(TestChecker().test(input, expect, 502))

    def test_3(self):
        input = """a: float = 3;"""
        expect = "No entry point"
        self.assertTrue(TestChecker().test(input, expect, 503))

    def test_4(self):
        input = """arra2 : array [2,3] of integer = {{2,1,2},{3,1,1}};"""
        expect = "No entry point"
        self.assertTrue(TestChecker().test(input, expect, 504))

    def test_5(self):
        input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4,"hello"} } };"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(3), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(4)]), ArrayLit([IntegerLit(1), IntegerLit(5)])]), ArrayLit([ArrayLit([IntegerLit(4), IntegerLit(3)]), ArrayLit([IntegerLit(2), IntegerLit(1)]), ArrayLit([IntegerLit(5), IntegerLit(4), StringLit(hello)])])])"
        self.assertTrue(TestChecker().test(input, expect, 505))

    def test_6(self):
        input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
array2 : array [3,2] of integer = array1[2,1,3];"""
        expect = "Type mismatch in Variable Declaration: VarDecl(array2, ArrayType([3, 2], IntegerType), ArrayCell(array1, [IntegerLit(2), IntegerLit(1), IntegerLit(3)]))"
        self.assertTrue(TestChecker().test(input, expect, 506))

    def test_7(self):
        input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
array2 : array [3,2] of integer = array1[2];
a: float = array2[2,1];"""
        expect = "No entry point"
        self.assertTrue(TestChecker().test(input, expect, 507))

    def test_8(self):
        input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
array2 : array [3,2] of integer = array1[2];
a: float = array2[2,1];
a: integer = 3;"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker().test(input, expect, 508))

    def test_9(self):
        input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
array2 : array [3,2] of integer = array1[2];
a: float = array2[2,1];
array3 : array [3,2] of integer = array2;"""
        expect = "No entry point"
        self.assertTrue(TestChecker().test(input, expect, 509))

#     def test_10(self):
#         input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
# array2 : array [3,2] of integer = array1[2];
# a: float = array2[2,1];
# array3 : array [3,2] of integer = array2;
# bcd : auto = array1[2];
# array4 : array [3,2] of integer = bcd;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 510))

#     def test_11(self):
#         input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
# array2 : array [3,2] of integer = array1[2];
# a: float = array2[2,1];
# array3 : array [3,2] of integer = array2;
# bcd : auto = array1[2];
# array4 : array [3,2] of float = bcd;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker().test(input, expect, 511))

#     def test_12(self):
#         input = """array1 : array [2,3,2] of integer = {{{3,2},{2,4},{1,5}}, {{4,3},{2,1},{5,4}}};
# array2 : array [3,2] of integer = array1[2];
# a: float = array2[2,1];
# array3 : array [3,2] of integer = array2;
# bcd : auto = array1[2];
# array4 : array [3,2] of float = bcd;
# b: array[2]of float  = array2[array3];"""
#         expect = "Type mismatch in expression: Id(array3)"
#         self.assertTrue(TestChecker().test(input, expect, 512))

    def test_13(self):
        input = """a: integer;
b: auto = a;

foo: function void () {
    a = 3;
    b = 2;
}"""
        expect = "No entry point"
        self.assertTrue(TestChecker().test(input, expect, 513))

    def test_14(self):
        input = """a: integer;
b: auto = a;

main: function void () {
    a : float;

    b : auto = 2.1;
    a = b;
    {a = foo(2,3);}
}"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker().test(input, expect, 514))

    def test_15(self):
        input = """main:function void() inherit foo{
    super(12);
    y:auto = foo(1);
    foo2();
    arr:array[2,2] of integer = {{1,2}, {1,2}};
    arr[1,2,3] = 1;
}
foo:function float(x:integer){
    return x + 1.2;
}
foo2: function void(){}"""
        expect = "Type mismatch in expression: ArrayCell(arr, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])"
        self.assertTrue(TestChecker().test(input, expect, 515))

    def test_16(self):
        input = """main : function void() inherit foo{
    super(1.0, 2.0, 3.0);
    z: boolean = true;
    x:string = "abc";
    y = 3.2;
}
foo : function auto(inherit x : auto, inherit y : auto, z : auto){
    //x = true;
    z = 2;
    return x + y + z;
}"""
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker().test(input, expect, 516))

    def test_17(self):
        input = """foo: function integer(){}

main: function void(){

	foo: integer = 3;

	a: integer;

	a = foo(); // line 5

}"""
        expect = "Type mismatch in expression: FuncCall(foo, [])"
        self.assertTrue(TestChecker().test(input, expect, 517))

    def test_18(self):
        input = """a: integer = 1;

foo: function void (b: integer) inherit a {}

a: function string (inherit c: string) {}"""
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker().test(input, expect, 518))

    def test_19(self):
        input = """foo: function auto (inherit out z: auto, t:auto) {
    z = 5;
    return z + t;
}

a:auto = foo(2.0, 2);
b:auto = foo(3.0, 1);
c: float = a + b;"""
        expect = "Type mismatch in expression: FuncCall(foo, [FloatLit(2.0), IntegerLit(2)])"
        self.assertTrue(TestChecker().test(input, expect, 519))

    def test_20(self):
        input = """main: function auto (){
    if (1==2) {
        return 1;
    }
    return;
}
"""
        expect = "Type mismatch in statement: ReturnStmt()"
        self.assertTrue(TestChecker().test(input, expect, 520))

    def test_21(self):
        input = """main: function auto (){
    if (1==2) {
        return;
    }
    return;
}

a: array [2] of integer = {{2},{3}};
"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([ArrayLit([IntegerLit(2)]), ArrayLit([IntegerLit(3)])]))"
        self.assertTrue(TestChecker().test(input, expect, 521))

    def test_22(self):
        input = """a :auto = {3,2,1};
main: function auto (){
    a = 3*"abc";
}

a: array [2,1] of integer = {{2},{3}};
"""
        expect = "Type mismatch in statement: AssignStmt(Id(a), BinExpr(*, IntegerLit(3), StringLit(abc)))"
        self.assertTrue(TestChecker().test(input, expect, 522))

    def test_23(self):
        input = """a :auto = 2;
main: function auto (){
    a = 3*"abc";
}

a: array [2,1] of integer = {{2},{3}};
"""
        expect = "Type mismatch in expression: BinExpr(*, IntegerLit(3), StringLit(abc))"
        self.assertTrue(TestChecker().test(input, expect, 523))

    def test_24(self):
        input = """a :auto = 2;
main: function auto (){
    x:integer = x + x;
}

a: array [2,1] of integer = {{2},{3}};
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker().test(input, expect, 524))

    def test_25(self):
        input = """a :auto = 2;
main: function auto (){
    x:auto = x + x;
}

a: array [2,1] of integer = {{2},{3}};
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker().test(input, expect, 525))

    def test_26(self):
        input = """a :auto = 2;
main: function auto (){
    printInteger(2);
    foo(3,2);
}

foo: function auto (a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Type mismatch in statement: AssignStmt(Id(a), StringLit(abc))"
        self.assertTrue(TestChecker().test(input, expect, 526))

    def test_27(self):
        input = """a :auto = 2;

foo: function auto (a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}

main: function auto (){
    printInteger(2);
    foo(3,2);
}



b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(3), IntegerLit(2))"
        self.assertTrue(TestChecker().test(input, expect, 527))

    def test_28(self):
        input = """a :auto = 2;

foo: function auto (a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}

main: function auto (){
    printInteger(2.3);
    foo(3,2);
}



b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Type mismatch in statement: CallStmt(printInteger, FloatLit(2.3))"
        self.assertTrue(TestChecker().test(input, expect, 528))

    def test_29(self):
        input = """a :auto = 2;

foo: function auto (a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}

main: function auto (){
    writeFloat(2);
    foo(3,2);
}



b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(3), IntegerLit(2))"
        self.assertTrue(TestChecker().test(input, expect, 529))

    def test_30(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit foo {

}
main: function auto (){
    writeFloat(2);
    foo(3,2);
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Invalid statement in function: bar"
        self.assertTrue(TestChecker().test(input, expect, 530))

    def test_31(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit foo {
    super("ab",2);
}
main: function auto (){
    writeFloat(2);
    foo(3,2);
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker().test(input, expect, 531))

    def test_32(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit foo {
    preventDefault();
}
main: function auto (){
    writeFloat(2);
    foo(3,2);
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(3), IntegerLit(2))"
        self.assertTrue(TestChecker().test(input, expect, 532))

    def test_33(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit foo {
    preventDefault(true,2,1);
}
main: function auto (){
    writeFloat(2);
    foo(3,2);
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker().test(input, expect, 533))

    def test_34(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    super(3,2);
    a: auto = 3;
    return a;
}
main: function auto (){
    writeFloat(2);
    foo("a",2);
}

b: array [2,1] of integer = {{2},{3}, {2}};
"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, ArrayType([2, 1], IntegerType), ArrayLit([ArrayLit([IntegerLit(2)]), ArrayLit([IntegerLit(3)]), ArrayLit([IntegerLit(2)])]))"
        self.assertTrue(TestChecker().test(input, expect, 534))

    def test_35(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (inherit a: integer, d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    super(3,2);
    a: auto = 3;
    return a;
}
main: function auto (){
    writeFloat(2);
    foo("a",2);
}

b: array [2,1] of integer = {{2},{3}, {2}};
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker().test(input, expect, 535))

    def test_36(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    super(3,2);
    a: auto = 3;
    return a;
}
main: function auto (){
    writeFloat(2);
    foo("a",2);
}

b: array [2,1] of integer = {{2},{3}, {2}};
"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, ArrayType([2, 1], IntegerType), ArrayLit([ArrayLit([IntegerLit(2)]), ArrayLit([IntegerLit(3)]), ArrayLit([IntegerLit(2)])]))"
        self.assertTrue(TestChecker().test(input, expect, 536))

    def test_37(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    super(3,2);
    d: auto = 3;
    return a;
}
main: function auto (){
    writeFloat(2);
    foo("a",2);
    bar(d, c);
}

b: array [2,1] of integer = {{2},{3}, {2}};
"""
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker().test(input, expect, 537))

    def test_38(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    super(3,2);
    d: auto = 3;
    return a;
}
main: function auto (){
    writeFloat(2);
    for (i = 3, i < 5, i+1)
        printInteger(i);
}

b: array [2,1] of integer = {{2},{3}, {2}};
"""
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker().test(input, expect, 538))

    def test_39(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    super(3,2);
    d: auto = 3;
    return a;
}

test2: function auto (i: auto){
    writeFloat(2);
    
    for (i = 3, i < 5, i+1)
        printInteger(i);
}

main: function auto(){
    return;
}

a: array [2,1] of integer = {{2},{3}};
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker().test(input, expect, 539))

    def test_40(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    super(3,2);
    d: auto = 3;
    return a;
}

test2: function auto (i: auto){
    writeFloat(2);
    break;
    for (i = 3, i < 5, i+1)
        printInteger(i);
}

main: function auto(){
    return;
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker().test(input, expect, 540))

    def test_41(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    super(3,2);
    d: auto = 3;
    return a;
}

test2: function auto (i: auto){
    writeFloat(2);
    
    for (i = 3, i < 5, i+1)
        break;
        
}

main: function auto(){
    return;
}

a: array [2,1] of integer = {{2},{3}};
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker().test(input, expect, 541))

    def test_42(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar2 {
    super(3,2);
    d: auto = 3;
    return a;
}

test2: function auto (i: auto){
    writeFloat(2);
    
    for (i = 3, i < 5, i+1)
        printInteger(i);
}

main: function auto(){
    return;
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Undeclared Function: bar2"
        self.assertTrue(TestChecker().test(input, expect, 542))

    def test_43(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    super(3,2);
    d: auto = 3;
    return a;
}

test2: function auto (i: auto){
    writeFloat(2);
    
    for (i = 3, i < 5, i+1)
        if (a == 2) return 3;
        else if (i % 2 == 0) return 2;
        else continue;
}

main: function auto(){
    return;
}

a: array [2,1] of integer = {{2},{3}};
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker().test(input, expect, 543))

    def test_44(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    super(3,2);
    d: auto = 3;
    return a;
}

test2: function auto (i: auto){
    writeFloat(2);
    
    for (i = 3, i < 5, i+1)
    {
        if (a == 2) return 3;
        else if (i % 2 == 0) return 2;
        else continue;
        break;
        return 1.2;
    }
}

main: function auto(){
    return;
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(1.2))"
        self.assertTrue(TestChecker().test(input, expect, 544))

    def test_45(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, inherit d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    super(3,2);
    d: auto = 3;
    return a;
}

test2: function auto (i: auto){
    writeFloat(2);
    
    do
    {
        if (a == 2) return 3;
        else if (i % 2 == 0) return 2;
        else continue;
        break;
    }
    while(true);
    return 1.2;
}

main: function auto(){
    return;
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker().test(input, expect, 545))

    def test_46(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, inherit d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    preventDefault();
    d: auto = 3;
    return a;
}

test2: function auto (i: auto) inherit bar{
    super(2, 3);
    writeFloat(2);
    
    do
    {
        if (a == 2) return 3.1;
        else if (i % 2 == 0) return 2;
        else continue;
        break;
    }
    while(true);
    return 1.2;
    d = foo("ab",2);

}

main: function auto(){
    return;
}

a: array [2,1] of integer = {{2},{3}};
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker().test(input, expect, 546))

    def test_47(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, inherit d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    preventDefault();
    d: auto = 3;
    return a;
}

test2: function auto (i: auto) inherit bar{
    super(2, 3);
    writeFloat(2);
    
    do
    {
        if (a == 2) return 3.1;
        else if (i % 2 == 0) return 2;
        else continue;
        break;
    }
    while(true);
    return 1.2;
    a = foo("ab",2);
    k = 3;

}

main: function auto(){
    return;
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker().test(input, expect, 547))

    def test_48(self):
        input = """a :auto = 2;
o : auto = {{1},{2}};
foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, inherit d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    preventDefault();
    d: auto = 3;
    return a;
}

test2: function auto (i: auto) inherit bar{
    super(2, 3);
    writeFloat(2);
    
    do
    {
        for (o[0] = 3,o[0] > 1, o[1]+1)
            if (a == 2) return 3.1;
            else if (i % 2 == 0) return 2;
            else continue;
        break;
    }
    while(true);
    return 1.2;
    a = foo("ab",2);
   

}

main: function auto(){
    return;
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Type mismatch in statement: ForStmt(AssignStmt(ArrayCell(o, [IntegerLit(0)]), IntegerLit(3)), BinExpr(>, ArrayCell(o, [IntegerLit(0)]), IntegerLit(1)), BinExpr(+, ArrayCell(o, [IntegerLit(1)]), IntegerLit(1)), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), ReturnStmt(FloatLit(3.1)), IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), ReturnStmt(IntegerLit(2)), ContinueStmt())))"
        self.assertTrue(TestChecker().test(input, expect, 548))

    def test_49(self):
        input = """a :auto = 2;
o : auto = {{1},{2}};
foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, inherit d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    preventDefault();
    d: auto = 3;
    return a;
}

test2: function auto (i: auto) inherit bar{
    super(2, 3);
    writeFloat(2);
    
    do
    {
        while (false)
            for (o[0,0] = 3,o[0,0] > 1, o[1,0]+1)
                if (a == 2) return 3.1;
                else if (i % 2 == 0) return 2;
                else continue;
        break;
    }
    while(true);
    break;
    return 1.2;
    a = foo("ab",2);
   

}

main: function auto(){
    return;
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker().test(input, expect, 549))

    def test_50(self):
        input = """a :auto = 2;
o : auto = {{1},{2}};
foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, inherit d: auto) inherit test {
    //foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    preventDefault();
    d: auto = 3;
    return a;
}

test2: function auto (i: auto) inherit bar{
    super(2, 3);
    writeFloat(2);
    
    do
    {
        while (false)
            for (o[0,0] = bar2(),o[0,0] > 1, o[0,1]+1)
                if (a == 2) return 3.1;
                else if (i % 2 == 0) return 2;
                else continue;
        break;
    }
    while(true);
    break;
    return 1.2;
    a = foo("ab",2);
   

}
bar2: function auto () {

    return 1;
}
main: function auto(){
    return;
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker().test(input, expect, 550))

    def test_51(self):
        input = """a :auto = 2;
o : auto = {{1},{2}};
foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, inherit d: auto) inherit test {
    //foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    preventDefault();
    d: auto = 3;
    return a;
}

test2: function auto (i: auto) inherit bar{
    super(2, 3);
    writeFloat(2);
    
    do
    {
        while (false)
            for (o[1,0] = bar2(),o[0,0] > 1, o[0,1]+1)
                if (a == 2) return 3.1;
                else if (i % 2 == 0) return 2;
                else continue;
        break;
    }
    while(true);
    break;
    return 1.2;
    a = foo("ab",2);
   

}
bar2: function auto () {

    return 1.2;
}
main: function auto(){
    return;
}

b: array [2,1] of integer = {{2},{3}};
"""
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(o, [IntegerLit(1), IntegerLit(0)]), FuncCall(bar2, []))"
        self.assertTrue(TestChecker().test(input, expect, 551))

    def test_52(self):
        input = """main : function void() inherit foo{
    super(1.0, 2.0, 3.0);
    z: integer = foo(1,2,3) + 1;
    x = "abc";
    y = true;
}
foo : function auto(inherit x : auto, inherit y : auto, z : auto){
    x = true;
    return x + y + z;
}"""
        expect = "Type mismatch in statement: AssignStmt(Id(x), BooleanLit(True))"
        self.assertTrue(TestChecker().test(input, expect, 552))

    def test_53(self):
        input = """foo: function void (b: auto, c: auto){

	a: string = b + c;

}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(+, Id(b), Id(c)))"
        self.assertTrue(TestChecker().test(input, expect, 553))

    def test_54(self):
        input = """inc : function void (out n : integer, n: float) inherit foo{
      super(0.1, 1);
      n: string = 124;    
} 
foo : function auto (inherit n: float, b: integer){}"""
        expect = "Invalid Parameter: n"
        self.assertTrue(TestChecker().test(input, expect, 554))

    def test_55(self):
        input = """foo: function integer(){}

main: function void(){

	foo: integer = 3;

	a: integer;

	a = foo();

}"""
        expect = "Type mismatch in expression: FuncCall(foo, [])"
        self.assertTrue(TestChecker().test(input, expect, 555))

    def test_56(self):
        input = """M: function void (a: integer) inherit N {} 

N: function void (inherit a: integer) {}"""
        expect = "Invalid statement in function: M"
        self.assertTrue(TestChecker().test(input, expect, 556))

    def test_57(self):
        input = """main: function void () {
    b: float = foo() > bar();
}

foo: function auto () {
    
}
bar: function auto() {
    a:auto = {{2},{3}};
}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, FloatType, BinExpr(>, FuncCall(foo, []), FuncCall(bar, [])))"
        self.assertTrue(TestChecker().test(input, expect, 557))

    def test_58(self):
        input = """main: function void () {
    b: boolean = foo() > bar();
}

foo: function auto () {
    
}
bar: function auto() {
    a:auto = {{2},{3}};
}

a: function auto () inherit bar1 {}"""
        expect = "Undeclared Function: bar1"
        self.assertTrue(TestChecker().test(input, expect, 558))

    def test_59(self):
        input = """main: function void () {
    b: float ;
    b = foo() > bar();
}

foo: function auto () {
    
}
bar: function auto() {
    a:auto = {{2},{3}};
}
a: function auto () inherit bar1 {}"""
        expect = "Type mismatch in statement: AssignStmt(Id(b), BinExpr(>, FuncCall(foo, []), FuncCall(bar, [])))"
        self.assertTrue(TestChecker().test(input, expect, 559))

    def test_60(self):
        input = """main: function void () {
    b: string;
    b = foo() :: bar();
}

foo: function auto () {
    
}
bar: function auto() {
    a:auto = {{2},{3}};
}
a: function auto () inherit bar1 {}"""
        expect = "Undeclared Function: bar1"
        self.assertTrue(TestChecker().test(input, expect, 560))

    def test_61(self):
        input = """main: function void () {
    b: boolean ;
    b = foo() > bar();
}

foo: function auto () {
    return 3;
}
bar: function auto() {
    a:auto = {{2},{3}};
}
a: function auto () inherit bar1 {}"""
        expect = "Undeclared Function: bar1"
        self.assertTrue(TestChecker().test(input, expect, 561))

    def test_62(self):
        input = """main: function void () {
    b: boolean ;
    b = foo() > bar();
}

foo: function auto () {
    return 3;
}
bar: function auto() {
    a:auto = {{2},{3}};
    return 2.1;
}
a: function auto () inherit bar1 {}"""
        expect = "Undeclared Function: bar1"
        self.assertTrue(TestChecker().test(input, expect, 562))

    def test_63(self):
        input = """main: function void () {
    b: boolean ;
    b = foo() > bar();
}

foo: function auto () {
    return 3;
}
bar: function auto() {
    a:auto = {{2},{3}};
    foo: integer = 3;
    foo();
}
a: function auto () inherit bar1 {}"""
        expect = "Type mismatch in statement: CallStmt(foo, )"
        self.assertTrue(TestChecker().test(input, expect, 563))

    def test_64(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > bar();
}

foo: function array[2,1] of integer () {
    return 3;
}
bar: function auto() {
    a:auto = {{2},{3}};
}
a: function auto () inherit bar1 {}"""
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(3))"
        self.assertTrue(TestChecker().test(input, expect, 564))

    def test_65(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > bar();
}

foo: function array[2,1] of integer () {
    return 3;
}
bar: function auto() {
    a:auto = {{2},{3}};
}
a: function auto () inherit bar1 {}"""
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(3))"
        self.assertTrue(TestChecker().test(input, expect, 565))

    def test_66(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > bar();
}

foo: function array[2,1] of integer () {
    return {{2},{1}};
}
bar: function auto() {
    a:auto = {{2},{3}};
}
a: function auto () inherit bar1 {}"""
        expect = "Undeclared Function: bar1"
        self.assertTrue(TestChecker().test(input, expect, 566))

    def test_67(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > bar();
    a:auto = readInteger();
    c = a%2;
    printInteger(c);
}

foo: function array[2,1] of integer () {
    return {{2},{1}};
}
bar: function auto() {
    a:auto = {{2},{3}};
}
a: function auto () inherit bar1 {}"""
        expect = "Type mismatch in statement: AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(2)))"
        self.assertTrue(TestChecker().test(input, expect, 567))

    def test_68(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > bar();
    a:auto = readInteger();
    {
        c:integer = a%2;
    }
    printInteger(c);
}

foo: function array[2,1] of integer () {
    return {{2},{1}};
}
bar: function auto() {
    a:auto = {{2},{3}};
}
a: function auto () inherit bar1 {}"""
        expect = "Type mismatch in statement: CallStmt(printInteger, Id(c))"
        self.assertTrue(TestChecker().test(input, expect, 568))

    def test_69(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > bar();
    a:auto = readInteger();
    {
        c:integer = a%2;
        printInteger(c);
    }
}

foo: function array[2,1] of integer () {
    return {{2},{1}};
}
bar: function auto() {
    a:auto = {{2},{3}};
}
a: function auto () inherit bar1 {}"""
        expect = "Undeclared Function: bar1"
        self.assertTrue(TestChecker().test(input, expect, 569))

    def test_70(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > bar();
    a:auto = printInteger();
    {
        c:integer = a%2;
        printInteger(c);
    }
}

foo: function array[2,1] of integer () {
    return {{2},{1}};
}
bar: function auto() {
    a:auto = {{2},{3}};
}
a: function auto () inherit bar1 {}"""
        expect = "Type mismatch in expression: FuncCall(printInteger, [])"
        self.assertTrue(TestChecker().test(input, expect, 570))

    def test_71(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > bar();
    a:float = readInteger();
    {
        a: auto = {{{2},{1}}};
        c:integer = a[0,0,0]%2;
    }
    printInteger(a);
}

foo: function array[2,1] of integer () {
    return {{2},{1}};
}
bar: function auto() {
    a:auto = {{2},{3}};
}
a: function auto () inherit bar1 {}"""
        expect = "Type mismatch in statement: CallStmt(printInteger, Id(a))"
        self.assertTrue(TestChecker().test(input, expect, 571))

    def test_72(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > bar();
    a:auto = readInteger();
    {
        c:integer = a%2;
    }
    writeFloat(a);
}

foo: function array[2,1] of integer () {
    return {{2},{1}};
}
bar: function auto() {
    a:auto = {{2},{3}};
}
a: function auto () inherit bar1 {}"""
        expect = "Undeclared Function: bar1"
        self.assertTrue(TestChecker().test(input, expect, 572))

    def test_73(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > 3;
    a:auto = readInteger();
    {
        c:integer = a%2;
    }
    writeFloat(a);
}

barr: function auto() {
    return 2;
}

foo: function array[2,1] of integer () inherit bar {
    super({{{1,3},{3,1}}, {{barr(),4},{1,3}}}, {3,2,barr()});
    b[2] = 3 - 3;
}
bar: function auto(inherit a : auto, b: auto) {
    a[2,1,2] = a[2,1,1] + b[1,2];
}
a: function auto () inherit bar1 {}"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker().test(input, expect, 573))

    def test_74(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > 3;
    a:auto = readInteger();
    {
        c:integer = a%2;
    }
    writeFloat(a);
}

barr: function auto() {
    return 2;
}

foo: function array[2,1] of integer () inherit bar {
    super({{{1,3},{3,1}}, {{barr(),4},{1,3}}}, {3,2,barr()});
    b[2] = 3 - 3;
}
bar: function auto(inherit a : auto, inherit b: auto) {
    a[2,1,2] = a[2,1,1] + b[1,2];
}
a: function auto () inherit bar1 {}"""
        expect = "Type mismatch in expression: ArrayCell(b, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker().test(input, expect, 574))

    def test_75(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > 3;
    a:auto = readInteger();
    {
        c:integer = a%2;
    }
    writeFloat(a);
}

barr: function auto() {
    return 2;
}

foo: function array[2,1] of integer () inherit bar {
    super({{{1,3},{3,1}}, {{barr(),4},{1,3}}}, {3,2,barr()});
    b[2] = 3 - 3;
}
bar: function auto(inherit a : auto, inherit b: auto) {
    a[2,1,2] = a[2,1,1] + b[2];
}
a: function auto () inherit bar1 {}"""
        expect = "Undeclared Function: bar1"
        self.assertTrue(TestChecker().test(input, expect, 575))

    def test_76(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > 3;
    a:auto = readInteger();
    {
        c:integer = a%2;
    }
    writeFloat(a);
}

barr: function auto() {
    return 2;
}

foo: function array[2,1] of integer () inherit bar {
    preventDefault();
    b:float = 3;
    b = b - 3;

}
bar: function auto(inherit a : auto, inherit b: auto) {
    a[2,1,2] = a[2,1,1] + b[1,2];
}
a: function auto () inherit bar1 {}"""
        expect = "Type mismatch in expression: ArrayCell(a, [IntegerLit(2), IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker().test(input, expect, 576))

    def test_77(self):
        input = """main: function void () {
    b: boolean ;
    a:auto = readInteger();
    {
        c:integer = a%2;
    }
    writeFloat(a);
}
bar: function integer () {}
foo: function void (i: auto, j: auto) {
    bar: integer = 3;
    for (i = 1, i < 100, i+2) {
        a: array[2] of integer = {3,bar};
        for (j = 1, j < bar(), j+1)
           printInteger(a[j]);
    }
}"""
        expect = "Type mismatch in expression: FuncCall(bar, [])"
        self.assertTrue(TestChecker().test(input, expect, 577))

    def test_78(self):
        input = """main: function void () {
    b: boolean ;
    a:auto = readInteger();
    {
        c:integer = a%2;
    }
    writeFloat(a);
}
bar: function integer () {}
foo: function void (i: auto, j: auto) {
   
    for (i = 1, i < 100, i+2) {
        a: array[2] of integer = {3,bar};
        for (j = 1, j < bar(), j+1)
           printInteger(a[j]);
    }
}"""
        expect = "Undeclared Identifier: bar"
        self.assertTrue(TestChecker().test(input, expect, 578))

    def test_79(self):
        input = """bar: function void () {
    a: array[2] of integer = {3,2};
    a[foo()] = 4;
}

foo: function auto () {return 3;}"""
        expect = "No entry point"
        self.assertTrue(TestChecker().test(input, expect, 579))

    def test_80(self):
        input = """bar: function void () {
    a: array[2] of integer = {3,2};
    a[foo()] = 4;
}

foo: function auto () {return;}"""
        expect = "Type mismatch in expression: FuncCall(foo, [])"
        self.assertTrue(TestChecker().test(input, expect, 580))

    def test_81(self):
        input = """bar: function void () {
    a: array[2] of integer = {3,2};
    a[foo()] = 4;
}

test: function void() {
    a:float = foo() + 2.3;
    printInteger(foo());
}

foo: function auto () {}"""
        expect = "No entry point"
        self.assertTrue(TestChecker().test(input, expect, 581))

    def test_82(self):
        input = """bar: function void () {
    a: array[2] of integer = {3,2};
    a[foo()] = 4;
}
a:auto = 3;
test: function void() {
   a:string = a;
}

foo: function auto () {}"""
        expect = "No entry point"
        self.assertTrue(TestChecker().test(input, expect, 582))

    def test_83(self):
        input = """bar: function void () {
    a: array[2] of integer = {3,2};
    a[foo()] = 4;
}
a:auto = 3;
test: function void() {
   a:string = a;
}

foo: function auto () {}"""
        expect = "No entry point"
        self.assertTrue(TestChecker().test(input, expect, 583))

    def test_84(self):
        input = """bar: function void () {
    a: array[2] of integer = {{3,2,1},{2,1}, {1,4}};
    a[foo()] = 4;
}

foo: function auto () {}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(3), IntegerLit(2), IntegerLit(1)]), ArrayLit([IntegerLit(2), IntegerLit(1)]), ArrayLit([IntegerLit(1), IntegerLit(4)])])"
        self.assertTrue(TestChecker().test(input, expect, 584))

    def test_85(self):
        input = """bar: function void () {
    a: array[2] of integer = {{3,2,1},{2,1,1}, {1,"abc",4}};
    a[foo()] = 4;
}

foo: function auto () {}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(3), IntegerLit(2), IntegerLit(1)]), ArrayLit([IntegerLit(2), IntegerLit(1), IntegerLit(1)]), ArrayLit([IntegerLit(1), StringLit(abc), IntegerLit(4)])])"
        self.assertTrue(TestChecker().test(input, expect, 585))

    def test_86(self):
        input = """bar: function void () {
    a: auto = {{3,2,1},{2,1,1}, {1,2,4}};
    b: auto = {{4,8,7},{1,3,1}, {2,1}};
    
}

foo: function auto () {}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(4), IntegerLit(8), IntegerLit(7)]), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(1)]), ArrayLit([IntegerLit(2), IntegerLit(1)])])"
        self.assertTrue(TestChecker().test(input, expect, 586))

    def test_87(self):
        input = """bar: function void () {
    a: auto = {{3,2,1},{2,1,1}, {1,2,4}};
    b: auto = {{4,8,7},{1,3,1}, {2,1,1}};
    
}

foo: function auto () {}"""
        expect = "No entry point"
        self.assertTrue(TestChecker().test(input, expect, 587))

    def test_88(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > 3;
    a:auto = readInteger();
    {
        c:integer = a%2;
    }
    writeFloat(a);
}

barr: function auto() {
    return 2.2;
}

foo: function array[2,1] of integer () inherit bar {
    super({{{1,3},{3,1}}, {{barr(),4},{1,3}}}, {3,2,barr()});
    b[2] = 3 - 3;
}
bar: function auto(inherit a : auto, inherit b: auto) {
    a[2,1,2] = a[2,1,1] + b[1,2];
}
a: function auto () inherit bar1 {}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(1)])]), ArrayLit([ArrayLit([FuncCall(barr, []), IntegerLit(4)]), ArrayLit([IntegerLit(1), IntegerLit(3)])])])"
        self.assertTrue(TestChecker().test(input, expect, 588))

    def test_89(self):
        input = """main: function void () {
    b: boolean ;
    c:auto = foo();
    b = c[0,1] > 3;
    a:auto = readInteger();
    {
        c:integer = a%2;
    }
    writeFloat(a);
}

barr: function auto() {
    return 2;
}

foo: function array[2,1] of integer () inherit bar {
    super({{{1,3},{3,1}}, {{barr(),4},{1,3}}}, {3,2,barr()});
    c: auto = {{{5,3},{3,1}}, {{4},{1,3}}};
    b[2] = 3 - 3;
}
bar: function auto(inherit a : auto, inherit b: auto) {
    a[2,1,2] = a[2,1,1] + b[1,2];
}
a: function auto () inherit bar1 {}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(5), IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(1)])]), ArrayLit([ArrayLit([IntegerLit(4)]), ArrayLit([IntegerLit(1), IntegerLit(3)])])])"
        self.assertTrue(TestChecker().test(input, expect, 589))

    def test_90(self):
        input = """a :auto = 2;

foo: function auto (inherit a: auto, b: auto) inherit main {
    x:integer = a + b;
    a = "abc";
    return 2;
}


bar: function string (a: integer, d: auto) inherit test {
    foo("ab", 2.4);
    arr1 : auto = {{3,2},{2,1}};
    return "done";
}

test: function integer () inherit bar {
    super(3,2);
    d: auto = 3;
    return a;
}
main: function auto (){
    writeFloat(2);
    for (i = 3, i < 5, i+1)
        printInteger(i);
}

b: array [2,1] of integer = {{2},{3}, {2}};
"""
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker().test(input, expect, 590))

    def test_91(self):
        input = """var: auto = {3_2,3,4,1,2,3};
    i: integer = foo(3.333e9, var[3]);
    e: float = i;
    flag: boolean = false;
    inc : function void (out o: integer, a:float) inherit foo{
        preventDefault();
        a: float = foo(n, 2);
    }
    foo : function auto (inherit n: float, n: integer){}"""
        expect = "Redeclared Parameter: n"
        self.assertTrue(TestChecker().test(input, expect, 591))

    def test_92(self):
        input = """var: auto = {32,3,4,1,2,3};
i: integer = test2();
e: float = i;
flag2: boolean = true;
func: function string(inherit f: boolean, y: integer) inherit test{
    while(i != 2) {
        break;
    }
    return "done";
}
test2: function auto() {
    for (i=2, i!=var[0], i+1) {
        break;
        return i;
    }
}
foo: function auto(bar: string, boo: float) inherit func {
    var: integer = 2;
}"""
        expect = "Undeclared Function: test"
        self.assertTrue(TestChecker().test(input, expect, 592))

    def test_94(self):
        input = """avar: auto = {32,3,4,1,2,3};
i: integer = test(3.2e-1);
test: function auto(inherit a: float) {
    for (i=9, i<10, i+1) {
        while (avar[3] + i) {
            i = avar[i] % 3;
            a = func(avar[3], i);
        }
        
    }
}
func: function void(f: boolean, y: integer) inherit test{
    super(avar);
    return f;
}"""
        expect = "Type mismatch in statement: WhileStmt(BinExpr(+, ArrayCell(avar, [IntegerLit(3)]), Id(i)), BlockStmt([AssignStmt(Id(i), BinExpr(%, ArrayCell(avar, [Id(i)]), IntegerLit(3))), AssignStmt(Id(a), FuncCall(func, [ArrayCell(avar, [IntegerLit(3)]), Id(i)]))]))"
        self.assertTrue(TestChecker().test(input, expect, 594))

    def test_95(self):
        input = """a: integer;
b: auto = a;

main: function void () {
    a : float;

    b : auto = 2.1;
    a = b;
    {a = foo(2,3);}
}"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker().test(input, expect, 595))

    def test_96(self):
        input = """test: function auto (e: auto) {}
func: function string(f: boolean, y: integer) inherit test{
    super(3);
    while(1 != 2) {
        break;
    }
    return s;
}
arr: array [4] of float = {1.3, 20e-2, 4.2, 5};"""
        expect = "Undeclared Identifier: s"
        self.assertTrue(TestChecker().test(input, expect, 596))

    def test_97(self):
        input = """test: function auto (e: auto) {}
func: function string(f: boolean, y: integer) inherit test{
    super(3);
    s:auto = "hello world!";
    while(1 != 2) {
        break;
    }
    return s;
}
arr: array [4] of float = {1.3, 20e-2, 4.2, 5};"""
        expect = "Illegal array literal: ArrayLit([FloatLit(1.3), FloatLit(0.2), FloatLit(4.2), IntegerLit(5)])"
        self.assertTrue(TestChecker().test(input, expect, 597))

    def test_98(self):
        input = """var: auto = {32,3,4,1,2,3};
inc : function void (out n: integer, a:float) inherit foo{}
foo : function auto (inherit n: float, n: integer){}"""
        expect = "Invalid statement in function: inc"
        self.assertTrue(TestChecker().test(input, expect, 598))

    def test_99(self):
        input = """a, B, c: array [3] of boolean ={true,true,true},{true,true,true},{true,false,true};
foo: function void () {
    printBoolean(false);
}"""
        expect = "No entry point"
        self.assertTrue(TestChecker().test(input, expect, 599))
