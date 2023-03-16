"""
PLAN:
Check the first word of the statement. Then use a match statement to match the first token.

Then for each of the first token in the statement have a function, which then checks the rest
of the token to see if that’s valid. If a token is not valid an exception will be thrown with a relevant message

Each of the tokens will have their own functions to check validity, including identifiers, constant literal and
correct operators such as plus and end.

Each of the first tokens well then have a do method in an interpreter to simulate what needs to be done.
"""

from LexerNoClass import Parser


def begin_parser():
    print(
        "----------------------------------------- \n" +
        "159.341 2023 Semester 1, Assignment 1\n" +
        "Submitted by Lydia Price, 20004521\n" +
        "----------------------------------------- \n"
    )

    Parser().begin()


if __name__ == '__main__':
    begin_parser()
