
import os, sys
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener

if not './main/mt22/parser/' in sys.path:
    sys.path.append('./main/mt22/parser/')
if not './main/mt22/astgen/' in sys.path:
    sys.path.append('./main/mt22/astgen/')
if not './main/mt22/checker/' in sys.path:
    sys.path.append('./main/mt22/checker/')
if os.path.isdir('../target/main/mt22/parser') and not '../target/main/mt22/parser/' in sys.path:
    sys.path.append('../target/main/mt22/parser/')
from MT22Lexer import MT22Lexer
from MT22Parser import MT22Parser

from ASTGeneration import ASTGeneration
from lexererr import *

Lexer = MT22Lexer
Parser = MT22Parser

class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)




def compileCode(src: str):
    lstFile = os.listdir(src)
    lstFile.sort(key=lambda x: int(x.split('.')[0]))
    path = './test/CodeGenSuite.py'
    counter = 1
    # while os.path.exists(path):
    #     path = f'./test/CheckerSuite_{counter}.py'
    #     counter +=1
    with open(path, 'w') as f:
        f.write(
"""import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):"""

        )
    default_counter = 600
  
    for file in lstFile:
        with open(os.path.join(src, file),'r') as s:
            content = s.read()
        try:
            with open(os.path.join("./test/solutions", str(default_counter)+".txt"),'r') as s:
                expect = s.read()
        except:
            expect = ""
        
        with open(path, 'a') as f:
            f.write(
f"""
    def test_{default_counter%100}(self):
        input = \"\"\"{str(content)}\"\"\"
        expect = "{expect}"
        self.assertTrue(TestCodeGen().test(input, expect, {default_counter}))
"""
            )
        default_counter +=1

