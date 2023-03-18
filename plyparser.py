import ply.yacc as yacc
from plylex import *


class MyParser:
    tokens = Lexer.tokens

    def __init__(self, lexer):
        print("Parser constructor called")
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer

    # DESTRUCTOR
    def __del__(self):
        print('Parser destructor called.')

    def p_error(self, p):
        print("Syntax error at token", p.type)

    def p_expression(self, p):
        """expression : id"""
        p[0] = p[1]

    def parse(self, input_string):
        return self.parser.parse(input_string)


# Build the parser
myLex = Lexer()
myPars = MyParser(myLex)
result = myPars.parse("!")
print(result)
