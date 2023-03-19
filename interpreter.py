import re


class Interpreter:

    def __init__(self):
        self.variables = {}

    def interpret(self, statement):
        print(f"Interpretting Statement: {statement}")
        print(type(statement))

        if isinstance(statement, str):
            match statement:
                case 'list':
                    self.list()
                case 'exit':
                    self.exit()
        else:
            match statement[0]:
                case 'append':
                    self.append(statement[1], statement[2])
                case 'print':
                    self.print(statement[1])
                case 'printlength':
                    self.printlength(statement[1])
                case 'printwords':
                    self.printwords(statement[1])
                case 'printwordcount':
                    self.printwordcount(statement[1])
                case 'set':
                    self.set(statement[1], statement[2])
                case 'reverse':
                    self.reverse(statement[1])

    def append(self, id_, expression):
        if expression in self.variables:
            self.variables[id_] = self.variables[id_] + self.variables[expression]
        else:
            self.variables[id_] = self.variables[id_] + expression

    def exit(self):
        exit()

    def list(self):
        print(f"Identifier list ({len(self.variables)}):\n")
        for key in self.variables:
            print(f"{key}: {self.variables[key]}")

    def set(self, id_, expression):

        self.variables[id_] = expression
        print()

    def reverse(self, id_):
        words = self.variables[id_].split(' ')
        self.variables[id_] = ' '.join(reversed(words))

    def print(self, expression):
        if expression in self.variables:
            print(self.variables[expression])
        else:
            print(expression)

    def printlength(self, expression):
        if expression in self.variables:
            print(len(self.variables[expression]))
        else:
            print(len(expression))

    def printwords(self, expression):
        if expression in self.variables:
            words = self.variables[expression].split(' ')
        else:
            words = expression.split(' ')
        print("Words are:\n\r")
        for word in words:
            print(f"{word}\n\r")

    def printwordcount(self, expression):
        if expression in self.variables:
            words = self.variables[expression].split(' ')
        else:
            words = expression.split(' ')

        print(f"Word count: {len(words)}")

    def clean_statement(self, statement):
        if '"' not in statement:
            return

        # TODO: Need to replace the string with a cleaned string with only " at the beginning and end, and only those with \"


text = input()
Interpreter().clean_statement(text)
