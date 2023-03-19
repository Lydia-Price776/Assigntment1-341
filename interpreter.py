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
                    self.append(statement[1], self.clean_statement(statement[2]))
                case 'print':
                    self.print(self.clean_statement(statement[1]))
                case 'printlength':
                    self.printlength(self.clean_statement(statement[1]))
                case 'printwords':
                    self.printwords(self.clean_statement(statement[1]))
                case 'printwordcount':
                    self.printwordcount(self.clean_statement(statement[1]))
                case 'set':
                    self.set(statement[1], self.clean_statement(statement[2]))
                case 'reverse':
                    self.reverse(self.clean_statement(statement[1]))

    def append(self, id_, expression):
        if self.variables[id_][0] == '"':
            self.variables[id_] = self.variables[id_][1:-1]
        if expression[0] == '"':
            expression = expression[1:-1]

        if expression in self.variables:
            if self.variables[expression][0] == '"':
                self.variables[expression] = self.variables[expression][1:-1]

            self.variables[id_] = '"' + self.variables[id_] + self.variables[expression] + '"'
        else:
            self.variables[id_] = '"' + self.variables[id_] + expression + '"'

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
        expressions = statement.split('+')
        print(expressions)
        i = 0
        while i < len(expressions):
            if expressions[i][0] == '"':
                print("first is double quote")
                expressions[i] = expressions[i].replace('/"', '##')
                expressions[i] = expressions[i].replace('"', '')
                expressions[i] = expressions[i].replace('##', '"')
            else:
                print("first is not double quote")
                if expressions[i] == ' ' or expressions[i] == '\t' or expressions[i] == '\n\r':
                    print("Expression is a constant")
                else:
                    expressions[i] = self.variables[expressions[i]]
                    if expressions[i][0] == '"':
                        expressions[i] = expressions[i][1:-1]

            i += 1
        return '"' + ''.join(expressions) + '"'

# # Create a list called expression from splitting the statement by the plus character.
#
# Run loop that checks if the first character is a “, otherwise get the valid ID from the dictionary.
#
# then, if each expression contains /“ replace this with a placeholder. And remove all other “ characters.
#
# Replace the placeholders with “ . Concatenate all expressions and add “ “ around the whole expression to create the new literal.
