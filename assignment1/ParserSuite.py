import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test1_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test2_simple_program(self):
        """Simple program: int main() {} """
        input = """double: function int() {return a*a;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test3_simple_program(self):
        """Simple program: int main() {} """
        input = """loop_test: function void() {
            for (a = 5, a <= 10, a + 1) {}
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test4_simple_program(self):
        """Simple program: int main() {} """
        input = """while_test: function int() {
    while (cond != true) {print(a, b, 5);}
    return a;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test5_simple_program(self):
        """Simple program: int main() {} """
        input = """a,b,c,d: int = 1,2,3,4;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test6_simple_program(self):
        """Simple program: int main() {} """
        input = """string_test: function void() {
    tmp: int = 25;
    for (a = 5, a != tmp, a + 1) {
        break;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test7_simple_program(self):
        """Test var_declare with express string"""
        input = """a: string = \"this is a string\";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test8_simple_program(self):
        """Test assign statement string"""
        input = """assign_test: function void() {
            a = \"this is a string\";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test9_simple_program(self):
        """Test assign multiple variables statement"""
        input = """assign_test: function void() {
            a = b = e = arr[5] = \"this is a string\";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test10_simple_program(self):
        """Test assign multiple variables statement"""
        input = """assign_test: function void() {
            a: boolean = false;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test11_simple_program(self):
        """Test assign multiple variables statement"""
        input = """string_test: function int(tmp: int) {
            a: boolean = false;
            return tmp;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))