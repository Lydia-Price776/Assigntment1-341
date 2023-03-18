import ply.yacc as yacc
from lexer import *


class Parser:
    tokens = Lexer.tokens

    def __init__(self, lexer):
        print("Parser constructor called")
        self.parser = yacc.yacc(module=self, tabmodule=None, debug=False, write_tables=False)
        self.lexer = lexer

    # DESTRUCTOR
    def __del__(self):
        print('Parser destructor called.')

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

    def p_append_statement(self, p):
        """
        append_statement : append id expression end
        """
        p[0] = ('append', p[2], p[3])

    def p_list_statement(self, p):
        """
        list_statement : list end
        """
        p[0] = "list"

    def p_exit_statement(self, p):
        """
        exit_statement : exit end
        """
        p[0] = "exit"

    def p_print_statement(self, p):
        """
        print_statement : print expression end
        """
        p[0] = ('print', p[2])

    def p_printlength_statement(self, p):
        """
        printlength_statement : printlength expression end
        """
        p[0] = ('printlength', p[2])

    def p_printwords_statement(self, p):
        """
        printwords_statement : printwords expression end
        """
        p[0] = ('printwords', p[2])

    def p_printwordcount_statement(self, p):
        """
        printwordcount_statement : printwordcount expression end
        """
        p[0] = ('printwordcount', p[2])

    def p_set_statement(self, p):
        """
        set_statement : set id expression end
        """
        p[0] = ('set', p[2], p[3])

    def p_reverse_statement(self, p):
        """
        reverse_statement : reverse id end
        """
        p[0] = ('reverse', p[2])

    def p_expression(self, p):
        """
        expression : value
                   | value plus value
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            if p[2] == '+':
                p[0] = p[1] + p[3]
            else:
                p[0] = None  # error handling

    def p_value(self, p):
        """
        value : id
              | constant
              | literal
        """
        p[0] = p[1]

    def p_error(self, p):
        print("Syntax error at", p.value)

    def parse(self, input_string):
        return self.parser.parse(input_string)


# Build the parser
myLex = Lexer()
myPars = Parser(myLex)
text = input("Type input: ")
result = myPars.parse(text)
print(result)
