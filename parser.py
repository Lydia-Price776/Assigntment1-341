from lexer import *
import ply.yacc as yacc


class Parser:

    def __init__(self):
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)

    tokens = Lexer.tokens

