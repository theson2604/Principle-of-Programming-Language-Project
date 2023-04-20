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

    #test auto type
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

    #test Undeclare
    def test17(self):
        input = """
        var, b: auto = false, true;
        a: float = 3.0;
        arr: array [3] of integer;
        test: function auto(inherit a: float) {
            var = test(al);
}
        func: function array [3] of integer(f: boolean, y: float) {
            var = test(a);
            return {1,2,3};
            b = test(a);
        }
"""
        expect = """Undeclared Identifier: al"""
        self.assertTrue(TestChecker.test(input,expect,417))

    def test18(self):
        input = """
        var, b: auto = false, true;
        a: float = 3.0;
        arr: array [3] of integer;
        test: function auto(inherit a: float) {
            for (aw=1, a<10, a+1) {
                printInteger(a);
            }
}
        func: function array [3] of integer(f: boolean, y: float) {
            var = test(a);
            return {1,2,3};
            b = test(a);
        }
"""
        expect = """Undeclared Identifier: aw"""
        self.assertTrue(TestChecker.test(input,expect,418))

    def test19(self):
        input = """
        var, b: auto = false, true;
        a: float = 3.0;
        i: integer;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (flag == var) {
                    printInteger(i);
                }
            }
}
        func: function array [3] of integer(f: boolean, y: float) {
            var = test(a);
            return {1,2,3};
            b = test(a);
        }
"""
        expect = """Undeclared Identifier: flag"""
        self.assertTrue(TestChecker.test(input,expect,419))