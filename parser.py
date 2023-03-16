import re


class Parser:

    def __init__(self):
        self.tokens = {
            "CONSTANT": r'\bSPACE\b|\bTAB\b|\bNEWLINE\b'
        }
        self.user_input = ""

    def begin(self):
        # TODO some user input shit here
        self.user_input = "yeeet hello;"
        #self.lexer()

    def lexer(self):
        counter = 0
        pos = 0
        while counter < len(self.user_input):
            if self.user_input[counter] == ';' or self.user_input[counter] == ' ':
                token = self.user_input[pos:counter]
                print(token, counter)
                pos = counter

            counter += 1


"""
        match (statement[0]):
            case "append":
                self.append(statement[0],statement)
            case "exit":
                self.exit(statement)
            case "list":
                self.list(statement)
            case "print":
                self.print(statement)
            case "printlength":
                self.printlength(statement)
            case "printwords":
                self.printwords(statement)
            case "printwordcount":
                self.printwordscount(statement)
            case "reverse":
                self.reverse(statement)
            case "set":
                self.set(statement)
            case _:
                raise ParserError("Expected one of %s but got %s" % (self.tokens, statement[0]))

    def append(self, token, statement):
        print(self.user_input)

    def exit(self, token, statement):
        if token == ';':
            exit()
        else:
            raise ParserError("Expected one of %s but got %s" % (self.tokens, statement[0]))

    def list(self):
        print()

    def print(self):
        print()

    def printlength(self):
        print()

    def printwords(self):
        print()

    def printwordscount(self):
        print()

    def reverse(self):
        print()

    def set(self):
        print()

    def expression(self):
        print()

    def value (self):
        print()
    def literal(self):
        print()

    def constant(self):
        print()

    def end(self):
        print()

    def plus(self):
        print()


"""


class ParserError(Exception):
    pass
