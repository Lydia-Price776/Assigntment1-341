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
            statements = self.get_user_input()

            for statement in statements:
                try:
                    result = self.parser.parse(statement)
                    self.interpret(result)
                except:
                    pass

    def get_user_input(self):

        total_input = ""
        in_literal = False
        statements = []
        start_pos = 0
        while True:
            usr_input = input()
            for current_pos in range(len(usr_input)):
                if usr_input[current_pos] == '"' and usr_input[current_pos - 1] != "\\":
                    in_literal = not in_literal
                elif usr_input[current_pos] == ';' and not in_literal:
                    if len(statements) == 0:
                        statements.append(usr_input[start_pos:current_pos + 1])
                    else:
                        last_state = statements[len(statements) - 1]
                        if last_state[len(last_state) - 1] != ';':
                            statements[len(statements) - 1] += usr_input
                        else:
                            statements.append(usr_input[start_pos:current_pos + 1])
                    start_pos = current_pos + 1

            if usr_input[len(usr_input) - 1] != ';':
                if len(statements) == 0:
                    statements.append(usr_input + "\n")
                else:
                    statements[len(statements) - 1] += usr_input + "\n"
                continue
            else:
                last_state = statements[len(statements) - 1]
                if last_state[len(last_state) - 1] != ';':
                    statements[len(statements) - 1] += usr_input + "\n"

            break

        return statements

    def interpret(self, statement):
        if statement is None:
            pass
        elif isinstance(statement, str):
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
        if expression == 'ERROR':
            pass
        elif expression in self.variables:
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
        if expression == 'ERROR':
            pass
        else:
            self.variables[id_] = expression

    def reverse(self, id_):
        try:
            words = self.variables[id_].split(' ')
            self.variables[id_] = ' '.join(reversed(words))
        except:
            print(f"ID: {id_} has not been defined")

    def print(self, expression):
        expression = self.clean_expression(expression)
        if expression == 'ERROR':
            pass
        elif expression in self.variables:
            print(self.variables[expression])
        else:
            print(expression)

    def printlength(self, expression):
        if expression in self.variables:
            print("Length: ", len(self.variables[expression]))
        else:
            expression = self.clean_expression(expression)
            if expression == 'ERROR':
                pass
            else:
                print("Length: ", len(expression))

    def printwords(self, expression):
        words = []
        if expression in self.variables:
            words = re.split(r'\n|\s', self.variables[expression])
        else:
            expression = self.clean_expression(expression)
            if expression == 'ERROR':
                pass
            else:
                words = re.split(r'\n|\s', expression)
        if len(words) != 0:
            print("Words:")
            for word in words:
                if re.search('[a-zA-Z]', word) is not None:
                    print(f"{word}")

    def printwordcount(self, expression):
        words = []
        if expression in self.variables:
            words = re.split(r'\n|\s', self.variables[expression])
        else:
            expression = self.clean_expression(expression)
            if expression == 'ERROR':
                pass
            else:
                words = re.split(r'\n|\s', expression)
        if len(words) != 0:
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
                try:
                    expressions[i] = self.variables[expression]
                except Exception:
                    print(f"Error: ID - {expression} has not been defined")
                    return 'ERROR'

            i += 1
        return ''.join(expressions)
