"""
Price, Lydia, 20004521, Assignment 1, 159.341
This is the Lexer implemented with the Ply.lex module
"""

from ply import lex


class Lexer:
    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # simple token names
    tokens = [
        "constant",
        "id",
        "literal",
        "plus",
        "end",
    ]
    # reserved token names
    reserved = {
        'append': 'append',
        'list': 'list',
        'exit': 'exit',
        'print': 'print',
        'printlength': 'printlength',
        'printwords': 'printwords',
        'printwordcount': 'printwordcount',
        'set': 'set',
        'reverse': 'reverse',
    }
    # Total tokens
    tokens = tokens + list(reserved.values())

    # Regular expression rules for simple tokens
    t_literal = r'(["])([^\\]*?(?:\\.[^\\]*?)*)(["])'
    t_plus = r'\+'
    t_end = r';'

    # Ignored charcters in given input - space, tab and new line
    t_ignore_space = r'[ ]'
    t_ignore_newline = r'[\n]'
    t_ignore_tab = r'[\t]'

    # Regular expression rule function for constants
    def t_constant(self, t):
        r'SPACE|TAB|NEWLINE'
        if t.value == 'SPACE':
            t.value = ' '
        elif t.value == 'TAB':
            t.value = '\t'
        elif t.value == 'NEWLINE':
            t.value = '\n'
            t.lexer.lineno += len(t.value)
        return t

    # Regular expression rule function for id's
    def t_id(self, t):
        r'[a-zA-Z][a-zA-Z0-9]*'
        t.type = self.reserved.get(t.value, 'id')  # Makes sure the id isn't a reserved keyword
        return t

    # Error handling function
    def t_error(self, t):
        char_pos = self.find_column(self.lexer.lexdata, t)
        next_space = self.find_next_space(self.lexer.lexdata, t)
        if next_space > char_pos:
            print("Error: Invalid token \"" + t.value[0:next_space - char_pos] + "\" in statement")
            t.lexer.skip(next_space - char_pos)
        else:
            t.lexer.skip(1)

    # Computes the column
    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

    # Finds next space in an input
    def find_next_space(self, text, token):
        next_space = text.rfind(' ', token.lexpos) + 1
        return next_space
