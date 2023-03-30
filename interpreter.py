"""
Price, Lydia, 20004521, Assignment 1, 159.341
This is the Interpreter which actions and implements the language
"""

import re
from lexer import Lexer
from parser import Parser


class Interpreter:

    # Constructor
    def __init__(self):
        self.variables = {}
        self.parser = Parser(Lexer())

    # Will continue to run and get input from the user until the exit; command is entered
    def start_program(self):
        while True:
            statements = self.get_user_input()
            for statement in statements:
                result = self.parser.parse(statement)
                self.interpret(result)

    # Gets the user input and checks validity
    def get_user_input(self):
        in_literal = False  # Tracks if a ; is in a literal or not
        statements = []
        start_pos = 0
        while True:
            usr_input = input()
            if len(usr_input) == 0:  # Accounts for the user accidentally pressing enter
                break
            # Handles input per line to account for multiline statements and multiple statements in a single input
            for current_pos in range(len(usr_input)):
                if usr_input[current_pos] == '"' and usr_input[current_pos - 1] != "\\":
                    in_literal = not in_literal
                elif usr_input[current_pos] == ';' and not in_literal:
                    if len(statements) == 0:  # Handles the first given statement
                        statements.append(usr_input[start_pos:current_pos + 1])
                    else:  # Handles the subsequent statements
                        last_state = statements[len(statements) - 1]
                        if last_state[len(last_state) - 1] != ';':
                            statements[len(statements) - 1] += usr_input
                        else:
                            statements.append(usr_input[start_pos:current_pos + 1])
                    start_pos = current_pos + 1
            # Appends statement based on previous statement input if any
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

    # Interprets the given statement from the parsar and handles it on a case by case basis
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

    # Function to append expressions or Identifiers
    def append(self, _id, expression):
        expression = self.clean_expression(expression)
        if expression == 'ERROR':  # Doesn't carry out operation if the expression is invalid
            pass
        elif expression in self.variables:
            self.variables[_id] = self.variables[_id] + self.variables[expression]
        else:
            self.variables[_id] = self.variables[_id] + expression

    # Function to exit program
    def exit(self):
        exit()

    # Function to list all variables stored
    def list(self):
        print(f"Identifier list ({len(self.variables)}):")
        for key in self.variables:
            print(f"{key}: {self.variables[key]}")

    # Function to set ID or override if previously defined
    def set(self, id_, expression):
        expression = self.clean_expression(expression)
        if expression == 'ERROR':  # Doesn't carry out operation if the expression is invalid
            pass
        else:
            self.variables[id_] = expression

    # Function to reverse contents of an ID
    def reverse(self, id_):
        try:
            words = self.variables[id_].split(' ')
            self.variables[id_] = ' '.join(reversed(words))
        except:
            print(f"ID: {id_} has not been defined")

    # Function to print contents of expression
    def print(self, expression):
        expression = self.clean_expression(expression)
        if expression == 'ERROR':  # Doesn't carry out operation if the expression is invalid
            pass
        elif expression in self.variables:
            print(self.variables[expression])
        else:
            print(expression)

    # Function to print total length of expression
    def printlength(self, expression):
        if expression in self.variables:
            print("Length: ", len(self.variables[expression]))
        else:
            expression = self.clean_expression(expression)
            if expression == 'ERROR':  # Doesn't carry out operation if the expression is invalid
                pass
            else:
                print("Length: ", len(expression))

    # Function to print the all words excluding punctuation
    def printwords(self, expression):
        words = []
        if expression in self.variables:
            # Only gets words, not punctuation
            words = re.findall(r"('?\b\S+\b)", self.variables[expression])
        else:
            expression = self.clean_expression(expression)
            if expression == 'ERROR':  # Doesn't carry out operation if the expression is invalid
                pass
            else:
                # Only gets words, not punctuation
                words = re.findall(r"('?\b\S+\b)", expression)
        if len(words) != 0:
            print("Words:")
            for word in words:
                print(f"{word}")

    # Function to print the total word count excluding punctuation
    def printwordcount(self, expression):
        words = []
        if expression in self.variables:
            # Only gets words, not punctuation
            words = re.findall(r"('?\b\S+\b)", self.variables[expression])
        else:
            expression = self.clean_expression(expression)
            if expression == 'ERROR':  # Doesn't carry out operation if the expression is invalid
                pass
            else:
                # Only gets words, not punctuation
                words = re.findall(r"('?\b\S+\b)", expression)
        if len(words) != 0:
            print(f"Word count is: {len(words)}")

    # Validates the expression and tidies the literals
    def clean_expression(self, statement):
        expressions = statement.split('+')
        for i, expression in enumerate(expressions):
            if expression[0] == '"':
                # Placeholder ## replaces /" in the literal in order to remove enclosing "
                expression = expression.replace('/"', '##')
                expression = expression.replace('"', '')
                expressions[i] = expression.replace('##', '"')
            elif expression == ' ' or expression == '\t' or expression == '\n':
                continue  # Ignore constants
            else:
                try:
                    expressions[i] = self.variables[expression]
                except:
                    print(f"Error: ID - {expression} has not been defined")
                    # Returns string 'ERROR' in order to prevent operations being carried out if the expression is invalid
                    return 'ERROR'

            i += 1
        return ''.join(expressions)
