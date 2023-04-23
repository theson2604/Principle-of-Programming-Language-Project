import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    #test simple program
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
        var, b: auto = false, true;
        a: float = 3.0;
        test: function boolean(inherit a: float, b: boolean) {
return true;
}
    main: function void() {
        printBoolean(var);
        test(a, b);
    }
"""
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,409))

    #test redeclare
    def test10(self):
        input = """
        var, b: auto = false, true;
        a: float = 3.0;
        test: function boolean(inherit a: float, b: boolean) {
        b: integer = 999;
return true;
}
"""
        expect = """Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input,expect,410))
        
    def test11(self):
        input = """
        var, b: auto = false, true;
        a: float = 3.0;
        test: function boolean(inherit a: float, b: boolean) {
            var: integer;
            return true;
            printInteger(123);
            a: integer = 123;
}
"""
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input,expect,411))

    def test12(self):
        input = """
        var, b: auto = false, true;
        a: float = 3.0;
        test: function boolean(inherit a: float, b: boolean, var: array [3] of float, a: string) {
            var: integer;
            return true;
            printInteger(123);
            a: integer = 123;
}
"""
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input,expect,412))


    def test13(self):
        input = """
        var, b: auto = false, true;
        a: integer = 3;
        arr: array [3] of integer;
        test: function boolean(inherit a: float, b: boolean, var: array [3] of float) {
            return true;
            printInteger(123);
            test: integer = 123;
}
        b: function array [3] of integer() {
            return arr;
        }
"""
        expect = """Redeclared Function: b"""
        self.assertTrue(TestChecker.test(input,expect,413))

    #test auto type
    def test14(self):
        input = """
        var, b: auto = false, true;
        a: float = 3.0;
        arr: array [3] of integer;
        test: function boolean(inherit a: float, b: auto, var: array [3] of float) {
            return true;
            printInteger(123);
            w: integer = 123;
            func(b, "123");
            b = true;
}
        func: function array [3] of integer(f: boolean, y: string) {
        return {1,2,3};
        }
"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,414))

    def test15(self):
        input = """
        var, b: auto = false, true;
        a: float = 3.0;
        arr: array [3] of integer;
        test: function auto(inherit a: float) {
}
        func: function array [3] of integer(f: boolean, y: string) {
            var = test(a);
            return {1,2,3};
            b = test(a);
        }
"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,415))

    def test16(self):
        input = """
        var, b: auto = false, true;
        a: float = 3.0;
        arr: array [3] of integer;
        test: function auto(inherit a: float) {
            func(true, "aaaa");
}
        func: function array [3] of integer(f: boolean, y: string) {
            var = test(a);
            return {1,2,3};
            b = test(a);
        }
"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,416))

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

    #test Redeclare
    def test20(self):
        input = """
        var, b: auto = false, true;
        i: integer;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (b == var) {
                    printInteger(i);
                }
            }
}
        func: function float(f: boolean, y: float) inherit test{
            super(3.0);
            var = test(a);
            return a;
            a: integer;
            b = test(a);
        }
"""
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input,expect,420))

    def test21(self):
        input = """
        var, b: auto = false, true;
        i: integer;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (b == var) {
                    printInteger(i);
                }
            }
}
        func: function float(f: boolean, y: float){
            a: float;
            var = test(a);
            return a;
            b = test(a);
        }

        b: auto = {1,2,3};
"""
        expect = """Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input,expect,421))

    def test22(self):
        input = """
        var, b: auto = false, true;
        i: integer;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (b == var) {
                    printInteger(i);
                }
            }
}
        var: function float(f: boolean, y: float){
            a: float;
            var = test(a);
            return a;
            b = test(a);
        }

        b: auto = {1,2,3};
"""
        expect = """Redeclared Function: var"""
        self.assertTrue(TestChecker.test(input,expect,422))

    def test23(self):
        input = """
        var, b: auto = false, true;
        i: integer;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (b == var) {
                    printInteger(i);
                }
            }
}
        test1: function float(f: boolean, y: float){
            a: float;
            var = test(a);
            return a;
            b = test(a);
        }

        test: auto = {1,2,3};
"""
        expect = """Redeclared Variable: test"""
        self.assertTrue(TestChecker.test(input,expect,423))

    def test24(self):
        input = """
        var, b: auto = false, true;
        i: integer;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (b == var) {
                    printInteger(i);
                }
            }
}
        test1: function float(f: boolean, y: float, f: string){
            a: float;
            var = test(a);
            return a;
            b = test(a);
        }

        test: auto = {1,2,3};
"""
        expect = """Redeclared Parameter: f"""
        self.assertTrue(TestChecker.test(input,expect,424))

    def test25(self):
        input = """
        var, b: auto = false, true;
        i: integer;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (b == var) {
                    printInteger(i);
                }
            }
}
        test1: function float(f: boolean, y: float){
            a: float;
            var = test(a);
            return a;
            y: array [1,2,3] of boolean;
            b = test(a);
        }

        test: auto = {1,2,3};
"""
        expect = """Redeclared Variable: y"""
        self.assertTrue(TestChecker.test(input,expect,425))

    def test26(self):
        input = """
        var, b: auto = false, true;
        i: integer;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (b == var) {
                    printInteger(i);
                }
            }
}
        func: function float(f: boolean, y: float) inherit test{
            super(3.0);
            var = test(a);
            func: boolean = false;
            return a;
        }

        func: auto = {1,2,3};
"""
        expect = """Redeclared Variable: func"""
        self.assertTrue(TestChecker.test(input,expect,426))

    #test Invalid
    def test27(self):
        input = """
        var: auto;
        i: integer;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (b == var) {
                    printInteger(i);
                }
            }
}
        func: function float(f: boolean, y: float) inherit test{
            super(3.0);
            var = test(a);
            func: boolean = false;
            return a;
        }

        func: auto = {1,2,3};
"""
        expect = """Invalid Variable: var"""
        self.assertTrue(TestChecker.test(input,expect,427))

    def test28(self):
        input = """
        var: auto = 2.0;
        i: integer;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (i == 2) {
                    printInteger(i);
                }
            }
            var= func(true, var);
}
        func: function float(f: boolean, y: float){
            foo: auto;
            func: boolean = false;
            return y;
        }

        func: auto = {1,2,3};
"""
        expect = """Invalid Variable: foo"""
        self.assertTrue(TestChecker.test(input,expect,428))

    def test29(self):
        input = """
        var: auto = 2.0;
        i: integer;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (i == 2) {
                    printInteger(i);
                }
            }
            var= func(true, var);
}
        func: function float(f: boolean, y: float){
            foo: auto;
            func: boolean = false;
            return y;
        }

        func: auto = {1,2,3};
"""
        expect = """Invalid Variable: foo"""
        self.assertTrue(TestChecker.test(input,expect,429))

    def test30(self):
        input = """
        var: auto = 2.0;
        i: integer;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (i == 2) {
                    printInteger(i);
                }
            }
            var= func(true, i);
}
        func: function float(f: boolean, a: integer) inherit test{
            super(var);
            func: boolean = false;
            return y;
        }

        func: auto = {1,2,3};
"""
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test31(self):
        input = """
        var: auto = 2.0;
        i: integer;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (i == 2) {
                    printInteger(i);
                }
            }
            var: auto;
            var= func(true, i);
}
        func: function float(f: boolean, a: integer) inherit test{
            super(var);
            func: boolean = false;
            return y;
        }

        func: auto = {1,2,3};
"""
        expect = """Invalid Variable: var"""
        self.assertTrue(TestChecker.test(input,expect,431))

    #test mismatch in var
    def test32(self):
        input = """
        var: auto = 2.0;
        i: integer = var;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (i == 2) {
                    printInteger(i);
                }
            }
            var: auto;
            var= func(true, i);
}
        func: function float(f: boolean, a: integer) inherit test{
            super(var);
            func: boolean = false;
            return y;
        }

        func: auto = {1,2,3};
"""
        expect = """Type mismatch in Variable Declaration: VarDecl(i, IntegerType, Id(var))"""
        self.assertTrue(TestChecker.test(input,expect,432))

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
            var: integer = test(a);
}
        func: function auto(f: boolean, y: integer) inherit test{
            super(var);
            return y;
        }
        foo : function auto (inherit n: auto, m: auto){
            a: string = n + m;
        }
"""
        expect = """Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(+, Id(n), Id(m)))"""
        self.assertTrue(TestChecker.test(input,expect,434))

    #test mismatch in expr
    #array subscripting
    def test35(self):
        input = """
        var: auto = {1,2,3,4,5};
        i: integer = test(2.0);
        test: function auto(inherit a: float) {
            i = var[a];
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
        expect = """Type mismatch in expression: ArrayCell(var, [Id(a)])"""
        self.assertTrue(TestChecker.test(input,expect,435))

    
    def test36(self):
        input = """
        var: auto = {{32,3,4},{1,2,3},{2,3,3}};
        i: integer = test(2.0);
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (var[i, a] == 2) {
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
        expect = """Type mismatch in expression: ArrayCell(var, [Id(i), Id(a)])"""
        self.assertTrue(TestChecker.test(input,expect,436))

    def test37(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(2.0);
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (var[test(1.3333)] == 2) {
                    printInteger(i);
                }
            }
            o: integer = var[a];
}
        func: function auto(f: boolean, y: integer) inherit test{
            super(var[i]);
            return f;
        }
        new_id: boolean = func(true, 123);
        x: integer = var[func(true, i)];
"""
        expect = """Type mismatch in expression: ArrayCell(var, [Id(a)])"""
        self.assertTrue(TestChecker.test(input,expect,437))

    #binop and unop
    def test38(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(2.0);
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (var[i] == (2 + a)) {
                    printInteger(i);
                }
            }
}
        func: function auto(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in expression: BinExpr(==, ArrayCell(var, [Id(i)]), BinExpr(+, IntegerLit(2), Id(a)))"""
        self.assertTrue(TestChecker.test(input,expect,438))
    
    def test39(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(2.0);
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (var[i] == (2 + i)) {
                    a = a % 3;
                    printInteger(i);
                }
            }
}
        func: function auto(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in expression: BinExpr(%, Id(a), IntegerLit(3))"""
        self.assertTrue(TestChecker.test(input,expect,439))

    def test40(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(2.0);
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (flag == true) {
                    i = var[i] % 3;
                    printInteger(i);
                }
                
            }
            s: string = "hello world";
            s = s :: "!!!!!!!!!!!!!!!";
            if (!s) {
                return ;
            }
}
        func: function auto(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in expression: UnExpr(!, Id(s))"""
        self.assertTrue(TestChecker.test(input,expect,440))


    def test41(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(2.0);
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (flag == true) {
                    i = var[i] % 3;
                    printInteger(i);
                }
                
            }
            s: string = "hello world";
            s = i :: "!!!!!!!!!!!!!!!";
            if (!s) {
                return ;
            }
}
        func: function auto(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in expression: BinExpr(::, Id(i), StringLit(!!!!!!!!!!!!!!!))"""
        self.assertTrue(TestChecker.test(input,expect,441))

    def test42(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(2.0);
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (a == 3.0) {
                    i = var[i] % 3;
                    printInteger(i);
                }
                
            }
            s: string = "hello world";
            s = i :: "!!!!!!!!!!!!!!!";
            if (!s) {
                return ;
            }
}
        func: function auto(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in expression: BinExpr(==, Id(a), FloatLit(3.0))"""
        self.assertTrue(TestChecker.test(input,expect,442))

    #FuncCall
    def test43(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(2.0);
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (flag) {
                    i = var[i] % 3;
                    a = func(flag, i);
                }
                
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in expression: FuncCall(func, [Id(flag), Id(i)])"""
        self.assertTrue(TestChecker.test(input,expect,443))

    def test44(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(2.0);
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (flag) {
                    i = var[i] % 3;
                    a = func(flag, i, var[3], test(3.0));
                }
                
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in expression: FuncCall(func, [Id(flag), Id(i), ArrayCell(var, [IntegerLit(3)]), FuncCall(test, [FloatLit(3.0)])])"""
        self.assertTrue(TestChecker.test(input,expect,444))

    def test45(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(var[3]);
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (flag) {
                    i = var[i] % 3;
                    a = func(var[3], i);
                }
                
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in expression: FuncCall(func, [ArrayCell(var, [IntegerLit(3)]), Id(i)])"""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test46(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test();
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (flag) {
                    i = var[i] % 3;
                    a = func(var[3], i);
                }
                
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in expression: FuncCall(test, [])"""
        self.assertTrue(TestChecker.test(input,expect,446))

    #test mismatch in stmt
    def test47(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=1, i<10, i+1) {
                while (var[3] + i) {
                    i = var[i] % 3;
                    a = func(var[3], i);
                }
                
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in statement: WhileStmt(BinExpr(+, ArrayCell(var, [IntegerLit(3)]), Id(i)), BlockStmt([AssignStmt(Id(i), BinExpr(%, ArrayCell(var, [Id(i)]), IntegerLit(3))), AssignStmt(Id(a), FuncCall(func, [ArrayCell(var, [IntegerLit(3)]), Id(i)]))]))"""
        self.assertTrue(TestChecker.test(input,expect,447))

    def test48(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=1, i%2, i+1) {
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(%, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input,expect,448))

    def test49(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=1, i!=var[0], i+1) {
                var = {1,2,3,4,5,6};
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in statement: AssignStmt(Id(var), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)]))"""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test50(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        e: float = i;
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=1, i!=var[0], i+1) {
                a = var[2];
                var[6] = e; 
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in statement: AssignStmt(ArrayCell(var, [IntegerLit(6)]), Id(e))"""
        self.assertTrue(TestChecker.test(input,expect,450))

    def test51(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        e: float = i;
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i="!!!!!!!!!!!", i!=var[0], i+1) {
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in statement: AssignStmt(Id(i), StringLit(!!!!!!!!!!!))"""
        self.assertTrue(TestChecker.test(input,expect,451))

    def test52(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        e: float = i;
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=2, i!=var[0], i+1) {
                printInteger(a);
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in statement: CallStmt(printInteger, Id(a))"""
        self.assertTrue(TestChecker.test(input,expect,452))

    def test53(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        e: float = i;
        flag: boolean = false;
        test: function auto(inherit a: float) {
            func(test(e), i);
            for (i=2, i!=var[0], i+1) {
                printInteger(a);
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(var);
            return f;
        }
"""
        expect = """Type mismatch in statement: CallStmt(func, FuncCall(test, [Id(e)]), Id(i))"""
        self.assertTrue(TestChecker.test(input,expect,453))

    def test54(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        e: float = i;
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=2, i!=var[0], i+1) {
                printInteger(i);
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(e);
            func(test(e));
        }
"""
        expect = """Type mismatch in statement: CallStmt(func, FuncCall(test, [Id(e)]))"""
        self.assertTrue(TestChecker.test(input,expect,454))

    def test55(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        e: float = i;
        flag: boolean = false;
        test: function auto(inherit a: float) {
            func(test(e), i);
            for (i=2, i!=var[0], i+1) {
                printInteger(a, flag, i, e);
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(e);
            return f;
        }
"""
        expect = """Type mismatch in statement: CallStmt(func, FuncCall(test, [Id(e)]), Id(i))"""
        self.assertTrue(TestChecker.test(input,expect,455))

    def test56(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        e: float = i;
        flag: boolean = false;
        test: function auto(inherit a: float) {
            func(flag, i);
            for (i=2, i!=var[0], i+1) {
                return a;
            }
        }
        func: function void(f: boolean, y: integer) inherit test{
            super(e);
            return f;
        }
"""
        expect = """Type mismatch in statement: ReturnStmt(Id(a))"""
        self.assertTrue(TestChecker.test(input,expect,456))

    def test57(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        e: float = i;
        flag: boolean = false;
        test: function auto(inherit a: float) {
            func(flag, i);
            for (i=2, i!=var[0], i+1) {
                return i;
            }
        }
        func: function string(f: boolean, y: integer) inherit test{
            super(e);
            return f;
        }
"""
        expect = """Type mismatch in statement: ReturnStmt(Id(f))"""
        self.assertTrue(TestChecker.test(input,expect,457))

    #test must in loop
    def test58(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        e: float = i;
        flag: boolean = false;
        test: function auto(inherit a: float) {
            func(flag, i);
            for (i=2, i!=var[0], i+1) {
                break;
                return i;
            }
        }
        func: function string(f: boolean, y: integer) inherit test{
            super(e);
            continue;
            return f;
        }
"""
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test59(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        e: float = i;
        flag: boolean = false;
        test: function auto(inherit a: float) {
            func(flag, i);
            for (i=2, i!=var[0], i+1) {
                break;
                return i;
            }
        }
        func: function string(f: boolean, y: integer) inherit test{
            super(e);
            while(1 != 2) {
                break;
            }
            break;
            return f;
        }
"""
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input,expect,459))

    #test illegal arraylit
    def test60(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        e: float = i;
        flag: boolean = false;
        s: string = "!!!!";
        test: function auto(inherit a: float) {
            func(flag, i);
            for (i=2, i!=var[0], i+1) {
                break;
                return i;
            }
        }
        func: function string(f: boolean, y: integer) inherit test{
            super(e);
            while(1 != 2) {
                break;
            }
            return s;
        }
        arr: array [4] of float = {1.3, 20e-2, 4.2, 5};
"""
        expect = """Illegal array literal: ArrayLit([FloatLit(1.3), FloatLit(0.2), FloatLit(4.2), IntegerLit(5)])"""
        self.assertTrue(TestChecker.test(input,expect,460))

    def test61(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        e: float = i;
        s: string = "!!!!";
        arr: array [4] of string = {"123", "hello", "world", s};
        flag: boolean = false;
        test: function auto(inherit a: float) {
            func(flag, i);
            for (i=2, i!=var[0], i+1) {
                break;
                return i;
                new_arr: array [4] of string = {"123", "hello", e, s};
            }
        }
        func: function string(f: boolean, y: integer) inherit test{
            super(e);
            while(1 != 2) {
                break;
            }
            return s;
        }
        arr: array [4] of float = {1.3, 20e-2, 4.2, 5};
"""
        expect = """Illegal array literal: ArrayLit([StringLit(123), StringLit(hello), Id(e), Id(s)])"""
        self.assertTrue(TestChecker.test(input,expect,461))

    #test invalid first stmt
    def test62(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test(3.2e-1);
        e: float = i;
        flag: boolean = false;
        test: function auto(inherit a: float) {
            for (i=2, i!=var[0], i+1) {
                break;
                return i;
            }
        }
        func: function string(f: boolean, y: integer) inherit test{
            while(1 != 2) {
                break;
            }
            return s;
        }
"""
        expect = """Invalid statement in function: func"""
        self.assertTrue(TestChecker.test(input,expect,462))

    def test63(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test();
        e: float = i;
        flag: boolean = false;
        func: function string(inherit f: boolean, y: integer) inherit test{
            while(1 != 2) {
                break;
            }
            return "owowowowo";
        }
        test: function auto() {
            for (i=2, i!=var[0], i+1) {
                break;
                return i;
            }
        }
        foo: function auto(bar: string, boo: float) inherit func {
            var: integer = 2;
        }
"""
        expect = """Invalid statement in function: foo"""
        self.assertTrue(TestChecker.test(input,expect,463))

    def test64(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test();
        e: float = i;
        flag: boolean = false;
        func: function string(inherit f: boolean, y: integer) inherit test{
            preventDefault();
            while(1 != 2) {
                break;
            }
            return "owowowowo";
        }
        test: function auto() {
            for (i=2, i!=var[0], i+1) {
                break;
                return i;
            }
        }
        foo: function auto(bar: string, boo: float) inherit func {
            test();
            var: integer = 2;
        }
"""
        expect = """Invalid statement in function: foo"""
        self.assertTrue(TestChecker.test(input,expect,464))

    #test no entry
    def test65(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = test();
        e: float = i;
        flag: boolean = false;
        func: function string(inherit f: boolean, y: integer) inherit test{
            preventDefault();
            while(1 != 2) {
                break;
            }
            return "owowowowo";
        }
        test: function auto() {
            for (i=2, i!=var[0], i+1) {
                break;
                return i;
            }
        }
        foo: function auto(bar: string, boo: float) inherit func {
            super(true, i);
            var: boolean = f;
        }
"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test66(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = foo("not", 3.333e9);
        e: float = i;
        flag: boolean = false;
        func: function string(inherit f: boolean, y: integer){
            while(1 != 2) {
                break;
            }
            return "owowowowo";
        }
        main: function boolean() {
            return true;
        }
        foo: function auto(bar: string, boo: float) inherit func {
            super(true, 1);
            var: boolean = f;
        }
"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,466))

    def test67(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = foo("not", 3.333e9);
        e: float = i;
        flag: boolean = false;
        func: function string(inherit f: boolean, y: integer){
            while(1 != 2) {
                break;
            }
            return "owowowowo";
        }
        main: auto = {1,2,3,4,5};
        foo: function auto(bar: string, boo: float) inherit func {
            super(true, var[i]);
            var: boolean = f;
        }
"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,467))

    #test inherit
    def test68(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = foo(3.333e9, var[3]);
        e: float = i;
        flag: boolean = false;
        inc : function void (out n: integer, a:float) inherit foo{}
        foo : function auto (inherit n: float, n: integer){}
"""
        expect = """Invalid Parameter: n"""
        self.assertTrue(TestChecker.test(input,expect,468))

    def test69(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = foo(3.333e9, var[3]);
        e: float = i;
        flag: boolean = false;
        inc : function void (out o: integer, a:float) inherit foo{}
        foo : function auto (inherit n: float, n: integer){}
"""
        expect = """Invalid statement in function: inc"""
        self.assertTrue(TestChecker.test(input,expect,469))

    def test70(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = foo(3.333e9, var[3]);
        e: float = i;
        flag: boolean = false;
        inc : function void (out o: integer, a:float) inherit foo{
            preventDefault();
            a: float = foo(n, 2);
        }
        foo : function auto (inherit n: float, n: integer){}
"""
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input,expect,470))

    def test71(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = foo(3.333e9, var[3]);
        e: float = i;
        flag: boolean = false;
        inc : function void (out o: integer, a:float) inherit foo{
            super(3.2);
            a: float = foo(n, 2);
        }
        foo : function auto (inherit n: float, n: integer){}
"""
        expect = """Type mismatch in expression: """
        self.assertTrue(TestChecker.test(input,expect,471))

    def test72(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = foo(3.333e9, var[3]);
        e: float = i;
        flag: boolean = false;
        inc : function void (out o: integer, a:float) inherit foo{
            super(3.2, i, var[31]);
            a: float = foo(n, 2);
        }
        foo : function auto (inherit n: float, n: integer){}
"""
        expect = """Type mismatch in expression: ArrayCell(var, [IntegerLit(31)])"""
        self.assertTrue(TestChecker.test(input,expect,472))

    def test73(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = foo(3.333e9, var[3]);
        e: float = i;
        flag: boolean = false;
        inc : function void (out o: integer, a:float) inherit foo{
            super(3.2, i, var[31]);
            a: float = foo(n, 2);
        }
        foo : function auto (inherit n: float, n: integer){}
"""
        expect = """Type mismatch in expression: ArrayCell(var, [IntegerLit(31)])"""
        self.assertTrue(TestChecker.test(input,expect,473))

    def test74(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = foo(3.333e9, var[3]);
        e: float = i;
        flag: boolean = false;
        inc : function void (out o: integer, a:float) inherit foo{
            super(3.2, i, var[31]);
            a: float = foo(n, 2);
        }
        foo : function auto (inherit n: float, n: integer){}
"""
        expect = """Type mismatch in expression: ArrayCell(var, [IntegerLit(31)])"""
        self.assertTrue(TestChecker.test(input,expect,474))

    def test75(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = foo(3.333e9, var[3]);
        e: float = i;
        flag: boolean = false;
        inc : function void (out o: integer, a:float) inherit foo{
            super(3.2, e);
            a: float = foo(n, 2);
        }
        foo : function auto (inherit n: float, n: integer){}
"""
        expect = """Type mismatch in expression: Id(e)"""
        self.assertTrue(TestChecker.test(input,expect,475))

    def test76(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = foo();
        e: float = i;
        flag: boolean = false;
        inc : function void (out o: integer, a:float) inherit foo{
            prevenDefault();
            a: float = foo(n, 2);
        }
        foo : function auto (){}
"""
        expect = """Undeclared Function: prevenDefault"""
        self.assertTrue(TestChecker.test(input,expect,476))

    #test random
    def test77(self):
        input = """
        main: function void() {
            a = b; 
        }
"""
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input,expect,477))

    def test78(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = foo();
        e: float = i;
        flag: boolean = false;
        inc : function void (out o: auto, a:auto) inherit foo{
            preventDefault();
            b: string = a + o;
        }
        foo : function auto (){}
"""
        expect = """Type mismatch in Variable Declaration: VarDecl(b, StringType, BinExpr(+, Id(a), Id(o)))"""
        self.assertTrue(TestChecker.test(input,expect,478))

    def test79(self):
        input = """
        var: auto = {32,3,4,1,2,3};
        i: integer = foo();
        e: float = i;
        flag: boolean = false;
        inc : function void (out o: auto, a:auto) inherit foo{
            preventDefault();
            b: string = i != flag;
        }
        foo : function auto (){}
"""
        expect = """Type mismatch in Variable Declaration: VarDecl(b, StringType, BinExpr(!=, Id(i), Id(flag)))"""
        self.assertTrue(TestChecker.test(input,expect,479))

    def test80(self):
        input = """
        var: auto = {{{{1,2,3}}}};
        main: function void() {
            a: integer = var[3,3,3];
        }
"""
        expect = """Type mismatch in expression: ArrayCell(var, [IntegerLit(3), IntegerLit(3), IntegerLit(3)])"""
        self.assertTrue(TestChecker.test(input,expect,480))