import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test1_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test2_float(self):
        """test float"""
        self.assertTrue(TestLexer.test("7.10E-5", "7.10E-5,<EOF>", 102))

    def test3_unclose_string1(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"this is an unclosed string", "Unclosed String: this is an unclosed string", 103))

    def test4_unclose_string2(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"this is an unclosed string \\f", "Unclosed String: this is an unclosed string \\f", 104))

    def test5_comment(self):
        """test string"""
        self.assertTrue(TestLexer.test("/*comment test test*/", "<EOF>", 105))

    def test6_illegal_string1(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"illegally escapsed\\a", "Illegal Escape In String: illegally escapsed\\a", 106))

    def test7_test_errorfloat(self):
        """test string"""
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 107))

    def test8_test_int(self):
        """test string"""
        self.assertTrue(TestLexer.test("1234_23333_222_2", "1234233332222,<EOF>", 108))

    # def test9_int_array(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("{1, 2, 3, 4, 5}", "{1, 2, 3, 4, 5},<EOF>", 109))

    def test10_type_auto(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("auto", "auto,<EOF>", 110))

    def test11_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"He asked me: \\\"Where is John?\\\"\"", "He asked me: \\\"Where is John?\\\",<EOF>", 111))    

    def test12_int(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("01234", "0,1234,<EOF>", 112))    

    def test13_errortoken(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("@#", "Error Token @", 113))    

    def test14_float(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("7e++3", "7,e,+,+,3,<EOF>", 114))

    def test15_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"test string\\\"", "Unclosed String: test string\\\"", 115))
    
    def test16_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"this is a string \\b\"", "this is a string \\b,<EOF>", 116))

    def test17_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"this is a string \\r\"", "this is a string \\r,<EOF>", 117))

    def test18_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"this is a string \\f\"", "this is a string \\f,<EOF>", 118))    
    
    def test19_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"this is a string \\'\"", "this is a string \\',<EOF>", 119))

    def test20_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"this is a string \\\\\"", "this is a string \\\\,<EOF>", 120))

    def test21_float(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("2_3.12E-231", "23.12E-231,<EOF>", 121))