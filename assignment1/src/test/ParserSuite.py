import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test1(self):
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test2(self):
        input = """double: function integer() {return a*a;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test3(self):
        input = """loop_test: function void() {
            for (a = 5, a <= 10, a + 1) {}
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test4(self):
        """Simple program: integer main() {} """
        input = """while_test: function integer() {
    while (cond != true) {printeger(a, b, 5);}
    return a;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test5(self):
        input = """a,b,c,d: integer = 1,2,3,4;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test6(self):
        input = """string_test: function void() {
    tmp: integer = 25;
    for (a = 5, a != tmp, a + 1) {
        break;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test7(self):
        input = """a: string = \"this is a string\";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test8(self):
        input = """assign_test: function void() {
            a = \"this is a string\";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test9(self):
        input = """assign_test: function void() {
            a = b = e = arr[5] = \"this is a string\";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test10(self):
        input = """assign_test: function void() {
            a: boolean = false;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test11(self):
        input = """string_test: function integer(tmp: integer) {
            a: boolean = false;
            return tmp;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test12(self):
        """test param"""
        input = """
            main: function boolean(inherit out a: auto) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test13(self):
        """test param"""
        input = """
            main: function boolean(inherit a: array[1,1] of float) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test14(self):
        """test param"""
        input = """
            main: function string(out a: array[0,1] of boolean, b: integer, inherit c: boolean) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test15(self):
        """test param"""
        input = """
            main: function string(out a: array[1,1] of string, b: void, inherit c: boolean) {}
        """
        expect = "Error on line 2 col 66: void"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test16(self):
        """test variable declaration"""
        input = """
            var1, var2, var3 : array = 1, 2, 3;
        """
        expect = "Error on line 2 col 37: ="
        self.assertTrue(TestParser.test(input, expect, 216))

    def test17(self):
        """test variable declaration"""
        input = """
            var1 : array [1] of auto;
        """
        expect = "Error on line 2 col 32: auto"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test18(self):
        """test variable declaration"""
        input = """
            var1 : array [1] of void;
        """
        expect = "Error on line 2 col 32: void"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test19(self):
        """test variable declaration"""
        input = """
            string: function void(){}
        """
        expect = "Error on line 2 col 12: string"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test20(self):
        """test declaration"""
        input = """"""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test21(self):
        """test declaration"""
        input = """
            main: function void(){}
            a[1,1,1] = 123; 
        """
        expect = "Error on line 3 col 13: ["
        self.assertTrue(TestParser.test(input, expect, 221))

    def test22(self):
        """test declaration"""
        input = """
            test(123,123,"string");
            main: function void(){}
        """
        expect = "Error on line 2 col 16: ("
        self.assertTrue(TestParser.test(input, expect, 222))

    def test23(self):
        input = """
            a, B, c: array [5,1000] of boolean ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
        

    def test24(self):
        input = """
            a, B, c: integer;
            x, Y, Z: boolean ;
            g: array [2,3] of float={{2,1,6},{4,2,1}};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test25(self):
        input = """
        main: function array [3,2] of boolean (
            a : integer,
            b : float) {
            a = 3;    
            a = ! - F * G / 5 + (I - !L && N + Y || Q *  !-P) && 6 * 5 + O / !(5 % T) ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
        

    def test26(self):
        input = """
        main: function array [3,2] of boolean (
            a : integer,
            b : integer) {
            a = b = c = d;    
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
        

    def test27(self):
        input = """
        main: function array [3,2] of boolean (
            a : integer,
            b : float) {
            a = 3;    
            a = (((5 > 6) <> (6 == 5)) >= (4 + 5 > 1)) <= 1 ;
        }
        """
        expect = "Error on line 6 col 27: >"
        self.assertTrue(TestParser.test(input, expect, 227))
        

    def test28(self):
        input = """
        main: function array [3,2] of boolean (
            a : integer,
            b : float) {
            a = true && !3 || ----b;    
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test29(self):
        input = """
            main: string() {}
        """
        expect = "Error on line 2 col 24: ("
        self.assertTrue(TestParser.test(input, expect, 229))

    def test30(self):
        input = """
            main: function array[1,1] of string() {
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test31(self):
        input = """
            main: function array[1,1] of string()
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test32(self):
        input = """
            main: function(){}
        """
        expect = "Error on line 2 col 26: ("
        self.assertTrue(TestParser.test(input, expect, 232))

    def test33(self):
        input = """
            main: function void() {
                continue;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test34(self):
        input = """
            main: function void() {
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test35(self):
        input = """
            main: function void() {
                return 1233;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test36(self):
        input = """
            main: function void() {
                return goo();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test37(self):
        input = """
            main: function void() {
                do {
                    do {

                    } while(true);
                } while (true);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test38(self):
        input = """
            main: function void() {
                do 
                    a = 1;
                while (true);
            }
        """
        expect = "Error on line 4 col 20: a"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test39(self):
        input = """
            main: function void() {
                do {a = 1;}
            }
        """
        expect = "Error on line 4 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test40(self):
        input = """
            main: function void() {
                do {a = 1;}
                while(a==b){
                    printInteger(123);
                }
            }
        """
        expect = "Error on line 4 col 27: {"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test41(self):
        input = """
            main: function void() {
                {
                    {
                        {
                            a: string = "string";
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test42(self):
        input = """
            main: function void() {
                {{{}}
            }
        """
        expect = "Error on line 5 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test43(self):
        input = """
            main: function void() {
                {}}}}
            }
        """
        expect = "Error on line 3 col 19: }"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test44(self):
        input = """
            main: function void() {
                {
                    sum: function integer(){}
                }
            }
        """
        expect = "Error on line 4 col 25: function"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test45(self):
        input = """
            main: function void() {
                a: boolean = !!!b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test46(self):
        input = """
            main: function void() {
                a: boolean = -!b;
            }
        """
        expect = "Error on line 3 col 30: !"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test47(self):
        input = """
            main: function void() {
                a: boolean = c&&d&&d;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test48(self):
        input = """
            main: function void() {
                a: boolean = c||(d||g);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test49(self):
        input = """
            main: function void() {
                a: boolean = c==d;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test50(self):
        input = """
            main: function string() {
                x: boolean = !!!z;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test51(self):
        input = """
            main: function void() {
                a: boolean = a==b==c;
            }
        """
        expect = "Error on line 3 col 33: =="
        self.assertTrue(TestParser.test(input, expect, 251))

    def test52(self):
        input = """
            main: function void() {
                a: boolean = a!=w!=c;
            }
        """
        expect = "Error on line 3 col 33: !="
        self.assertTrue(TestParser.test(input, expect, 252))

    def test53(self):
        input = """
            main: function void() {
                ol: boolean = e&&f||c&&d;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test54(self):
        input = """
            main: function void() {
                a: boolean = a&&t == var[1]||fwo(129,452,123);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test55(self):
        input = """
            main: function void() {
                a: auto = "string"::a&&c+2*3==b-2*!-b[1,2,3]||d;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test56(self):
        input = """
            main: function void() {
                a: auto = -var[a||3==b*!-g[12]];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test57(self):
        input = """
            main: function void() {
                a: auto = a::h==b::w;
            }
        """
        expect = "Error on line 3 col 33: ::"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test58(self):
        input = """
            main: function void() {
                a = ol > jh;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test59(self):
        input = """
            a, b, c: boolean;
            ts, y, ss: float ;
            g, eh, bi: array[0 , 5] boolean ;
        """
        expect = "Error on line 4 col 36: boolean"
        self.assertTrue(TestParser.test(input, expect, 259))
        

    def test60(self):
        input = """
            a, w, c: boolean;
            x, l, z: float ;
            g, k, i: array[4 , 6] of string = {a,w,"10"};
        """
        expect = "Error on line 4 col 56: ;"
        self.assertTrue(TestParser.test(input, expect, 260))
        

    def test61(self):
        input = """
            a, b, c: boolean;
            x, y, z: float ;
            g, h, i: array[0 , 5] with boolean ;
        """
        expect = "Error on line 4 col 34: with"
        self.assertTrue(TestParser.test(input, expect, 261))
        

    def test62(self):
        input = """
            a, b, w: boolean;
            x, u, z: float ;
            n, q, i: array[3 , 1] in boolean;
        """
        expect = "Error on line 4 col 34: in"
        self.assertTrue(TestParser.test(input, expect, 262))
        

    def test63(self):
        input = """
            a, v, c: boolean;
            x, y, s: float ;
            fg, f, i: array(3 , 5) of boolean ;
        """
        expect = "Error on line 4 col 27: ("
        self.assertTrue(TestParser.test(input, expect, 263))
        

    def test64(self):
        input = """
            a, b, l: boolean;
            e, y, z: float ;
            g, t, i: arr[0 , 8] of boolean ;
        """
        expect = "Error on line 4 col 21: arr"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test65(self):
        input = """
            test: function void (){
                while 1<3<5<8 ok();
                
            }
        """
        expect = "Error on line 3 col 22: 1"
        self.assertTrue(TestParser.test(input, expect, 265))
                
    def test66(self):
        input = """
        test: function void (){

            for (i = 1 , i< 11, i+1) {
                for (j = i, j > 1, j/2)
                    if ((i + j) % 2 == 1) 
                        continue; 
                    break;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
        
    def test67(self):
        input = """
        main: function integer ()
        {
            // Test line comment
            /* test block comment */
            return 264;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test68(self):
        input = """
            true: function boolean()
        """
        expect = "Error on line 2 col 12: true"
        self.assertTrue(TestParser.test(input, expect, 268))
        

    def test69(self):
        input = """
            function test();
        """
        expect = "Error on line 2 col 12: function"
        self.assertTrue(TestParser.test(input, expect, 269))
        

    def test70(self):
        input = """
            test: function boolean(a: integer)
        {
            
        """
        expect = "Error on line 5 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 270))