import queue

from lexer import Lexer


class Parser:
    def __init__(self):
        self.lexer = Lexer().lexer
        self.statement = queue.Queue()

    def parse(self, usr_input):
        self.lexer.input(usr_input)

        for item in self.lexer:
            self.statement.put(item)

        token = self.statement.get()
        # Token Attributes type, value, lineno, lexpos

        if token.type in list(Lexer().reserved):
            self.yeet(token.type)
        else:
            raise ParserError(f"Expected token of type {list(Lexer().reserved)} but got type {token.type}")



class ParserError(Exception):
    pass
