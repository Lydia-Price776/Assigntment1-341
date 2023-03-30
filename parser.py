"""
Price, Lydia, 20004521, Assignment 1, 159.341
This is the Parser implemented with the Ply.yacc module
"""

import ply.yacc as yacc
from lexer import *


class Parser:
    tokens = Lexer.tokens

    # Constructor
    def __init__(self, lexer):
        self.parser = yacc.yacc(module=self, tabmodule=None, debug=False, write_tables=False)
        self.lexer = lexer

    # Destructor
    def __del__(self):
        pass

    # Statement function definition
    def p_statement(self, p):
        """
        statement : append_statement
                  | list_statement
                  | exit_statement
                  | print_statement
                  | printlength_statement
                  | printwords_statement
                  | printwordcount_statement
                  | set_statement
                  | reverse_statement
        """
        p[0] = p[1]

    # Append function definition
    def p_append_statement(self, p):
        """
        append_statement : append id expression end
        """
        p[0] = ['append', p[2], p[3]]

    # List function definition
    def p_list_statement(self, p):
        """
        list_statement : list end
        """
        p[0] = "list"

    # Exit function definition
    def p_exit_statement(self, p):
        """
        exit_statement : exit end
        """
        p[0] = "exit"

    # Print function definition
    def p_print_statement(self, p):
        """
        print_statement : print expression end
        """
        p[0] = ['print', p[2]]

    # Printlength function definition
    def p_printlength_statement(self, p):
        """
        printlength_statement : printlength expression end
        """
        p[0] = ['printlength', p[2]]

    # Printwords function definition
    def p_printwords_statement(self, p):
        """
        printwords_statement : printwords expression end
        """
        p[0] = ['printwords', p[2]]

    # Printwordcount function definition
    def p_printwordcount_statement(self, p):
        """
        printwordcount_statement : printwordcount expression end
        """
        p[0] = ['printwordcount', p[2]]

    # Set function definition
    def p_set_statement(self, p):
        """
        set_statement : set id expression end
        """
        p[0] = ['set', p[2], p[3]]

    # reverse function definition
    def p_reverse_statement(self, p):
        """
        reverse_statement : reverse id end
        """
        p[0] = ['reverse', p[2]]

    # Expression function definition
    def p_expression(self, p):
        """
        expression : value
                   | value plus expression
                   | expression plus expression

        """

        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[1] + '+' + p[3]

    # Value function definition
    def p_value(self, p):
        """
        value : id
              | constant
              | literal
        """
        p[0] = p[1]

    # Error handling function
    def p_error(self, p):
        if p is None:
            print("Error: Missing token in statement. Check statement ends with a semicolon ;")
        else:
            print(f"Error: Invalid token {p.value!r} in statement")

    # Parse function to begin parser
    def parse(self, input_string):
        return self.parser.parse(input_string)
