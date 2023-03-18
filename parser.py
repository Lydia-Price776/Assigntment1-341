import queue

from lexer import Lexer


class Parser:
    def __init__(self):
        self.lexer = Lexer().lexer
        self.statement = []

    def parse(self, usr_input):
        self.lexer.input(usr_input)

        for item in self.lexer:
            self.statement.append(item)

        token = self.statement
        # Token Attributes type, value, lineno, lexpos
        for item in self.statement:
            print(item)
        if token.type in list(Lexer().reserved):
            self.yeet(token.type)
        else:
            raise ParserError(f"Expected token of type {list(Lexer().reserved)} but got type {token.type}")

    def yeet(self, token):
        match token:
            case "append":
                self.append(),
            case "list" | "exit":
                self.list_exit(),
            case "print":
                self.print(),
            case "printwords":
                self.set(),
            case "printwordcount":
                self.printwordcount(),
            case "set":
                self.set(),
            case "reverse":
                self.reverse(),

    def append(self):
        token = self.statement.get()
        if self.is_id(token):
            id = token

        else:
            raise ParserError(f"Expected id token, but got {token.type}")

        #if self.is_expr(self.statement.get())

    def is_id(self, token):
        if token.type == 'id':
            return True
        else:
            return False

    def is_expr(self,token):
        print(token)
        if self.is_value(token):
            return True
        else:
            return False


    def is_value(self, token):
        if token.type == 'id' or token.type == 'constant' or token.type == 'literal':
            return True
        else:
            return False


class ParserError(Exception):
    pass
