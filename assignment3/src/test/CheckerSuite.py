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

    def test33(self):
        input = """
        var: auto = 2.0;
        i: integer = 2;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (i == 2) {
                    printInteger(i);
                }
            }
            var= test(var);
}
        foo: integer = test(var);
        func: function float(f: boolean, a: integer) inherit test{
            super(var);
            func: boolean = false;
            return y;
        }

        func: auto = {1,2,3};
"""
        expect = """Type mismatch in Variable Declaration: VarDecl(foo, IntegerType, FuncCall(test, [Id(var)]))"""
        self.assertTrue(TestChecker.test(input,expect,433))

    def test34(self):
        input = """
        var: auto = 2.0;
        i: integer = test(var);
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (i == 2) {
                    printInteger(i);
                }
            }
            var: float = test(a);
}
        func: function auto(f: boolean, y: integer) inherit test{
            super(var);
            return y;
        }
        new_id: boolean = func(true, 123);
"""
        expect = """Type mismatch in Variable Declaration: VarDecl(foo, IntegerType, FuncCall(test, [Id(var)]))"""
        self.assertTrue(TestChecker.test(input,expect,434))