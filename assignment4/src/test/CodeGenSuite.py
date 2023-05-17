import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
    def test_0(self):
        input = """a:auto = 3;

main: function void() {
    
}"""
        expect = ""
        self.assertTrue(TestCodeGen().test(input, expect, 600))
