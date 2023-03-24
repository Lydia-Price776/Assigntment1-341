# Remove " before setting to variable

class Interpreter:

    def __init__(self):
        self.variables = {}

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
            print("Length: ",len(self.clean_expression(expression)))

    def printwords(self, expression):
        if expression in self.variables:
            words = self.variables[expression].split(' ')
        else:
            words = self.clean_expression(expression).split(' ')
        print("Words:")
        for word in words:
            print(f"{word}")

    def printwordcount(self, expression):
        if expression in self.variables:
            words = self.variables[expression].split(' ')
        else:
            words = self.clean_expression(expression).split(' ')

        print(f"Word count: {len(words)}")

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
