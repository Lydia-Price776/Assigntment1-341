# Remove " before setting to variable
import re

from lexer import Lexer
from parser import Parser


class Interpreter:

    def __init__(self):
        self.variables = {}
        self.parser = Parser(Lexer())

    def start_program(self):
        print(
            "----------------------------------------- \n" +
            "159.341 2023 Semester 1, Assignment 1\n" +
            "Submitted by Lydia Price, 20004521\n" +
            "----------------------------------------- \n"
        )

        while True:
            total_input = self.get_user_input()
            result = self.parser.parse(total_input)
            self.interpret(result)

    def get_user_input(self):
        total_input = ""
        in_literal = False
        while True:
            line = input()
            for i in range(len(line)):
                if line[i] == '"' and line[i - 1] != "\\":
                    in_literal = not in_literal
                elif line[i] == ';' and not in_literal:
                    total_input += line[:i + 1]
                    if i < len(line) - 1:
                        raise InterpreterError(f"Invalid input {line[i + 1:]} entered after statement termination ")
                    break
            else:
                total_input += line + "\n"
                continue
            break
        return total_input

    def interpret(self, statement):
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

    def append(self, _id, expression):
        expression = self.clean_expression(expression)

        if expression in self.variables:
            self.variables[_id] = self.variables[_id] + self.variables[expression]
        else:
            self.variables[_id] = self.variables[_id] + expression

    def exit(self):
        exit()

    def list(self):
        print(f"Identifier list ({len(self.variables)}):")
        for key in self.variables:
            print(f"{key}: {self.variables[key]}")

    def set(self, id_, expression):
        expression = self.clean_expression(expression)
        self.variables[id_] = expression

    def reverse(self, id_):
        if id_ in self.variables:
            words = self.variables[id_].split(' ')
            self.variables[id_] = ' '.join(reversed(words))
        else:
            raise InterpreterError(f"ID: {id_} has not been defined")

    def print(self, expression):
        if expression in self.variables:
            print(self.variables[expression])
        else:
            print(self.clean_expression(expression))

    def printlength(self, expression):
        if expression in self.variables:
            print("Length: ", len(self.variables[expression]))
        else:
            print("Length: ", len(self.clean_expression(expression)))

    def printwords(self, expression):
        if expression in self.variables:
            words = re.split(r'\n|\s', self.variables[expression])
        else:
            words = re.split(r'\n|\s', self.clean_expression(expression))
        print("Words:")
        for word in words:
            if re.search('[a-zA-Z]', word) is not None:
                print(f"{word}")

    def printwordcount(self, expression):
        if expression in self.variables:
            words = re.split(r'\n|\s', self.variables[expression])

        else:

            words = re.split(r'\n|\s', self.clean_expression(expression))
        word_count = 0
        for word in words:
            if re.search('[a-zA-Z]', word) is not None:
                word_count += 1

        print(f"Word count: {word_count}")

    def clean_expression(self, statement):
        expressions = statement.split('+')
        for i, expression in enumerate(expressions):
            if expression[0] == '"':
                expression = expression.replace('/"', '##')
                expression = expression.replace('"', '')
                expressions[i] = expression.replace('##', '"')
            elif expression == ' ' or expression == '\t' or expression == '\n':
                continue
            else:
                if expression in self.variables:
                    expressions[i] = self.variables[expression]
                else:
                    raise InterpreterError(f"ID: {expression} has not been defined")

            i += 1
        return ''.join(expressions)


class InterpreterError(Exception):
    pass
