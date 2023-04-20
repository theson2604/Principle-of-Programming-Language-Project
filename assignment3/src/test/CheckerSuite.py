import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test0(self):
        input = """
        main: function void () {
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test1(self):
        input = """x, y, z: integer = 1, 2, 3;
        main: function void () {
        }  
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test2(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;
        main: function void () {
        }  
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test3(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test4(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test5(self):
        input = """
a, B, c: array [5,1000] of boolean ;
        main: function void () {
        printBoolean(false);
        }
"""
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test6(self):
        input = """
        a: integer;
        main: function void() {
                    for (a=1, a<10, a+1) {
                        printInteger(a);
                    }
                   }"""
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,406))

    def test7(self):
        input = """main: function void() {
                    while(true) {
                        a: boolean = false;
                        c: float = 2.333333;
                        continue;}
                   }"""
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,407))

    def test8(self):
        input = """test: function boolean() {
        a: array[23,5,3] of integer;
        b: boolean;
        while(true) {
            test();
            break;}
        return b;
}
        main: function void() {
            a: integer = 3;
        }
"""
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,408))

    def test9(self):
        input = """
        var: boolean;
        a: array [3] of integer = [1,2,3];
        test: function boolean(a: array[3] of integer) {
test(a);
return true;
}
    main: function void() {
        printBoolean(var);
    }
"""
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,409))