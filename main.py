from parser import Parser
from lexer import Lexer
from interpreter import Interpreter


def begin():
    print(
        "----------------------------------------- \n" +
        "159.341 2023 Semester 1, Assignment 1\n" +
        "Submitted by Lydia Price, 20004521\n" +
        "----------------------------------------- \n"
    )

    parser = Parser(Lexer())
    interpreter = Interpreter()

    while True:
        lines = []
        while True:
            user_input = input()


            if user_input == '':
                break
            else:
                lines.append(user_input + '\n')

        complete_input = ''.join(lines)

        result = parser.parse(complete_input)
        interpreter.interpret(result)


if __name__ == '__main__':
    begin()
