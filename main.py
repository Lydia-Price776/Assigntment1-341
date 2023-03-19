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
    usr_input = input()

    while True:
        result = parser.parse(usr_input)
        interpreter.interpret(result)
        usr_input = input()


if __name__ == '__main__':
    begin()
