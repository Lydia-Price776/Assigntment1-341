from ply import lex

tokens = [
    "constant",
    "id",
    "literal",
    "plus",
    "end",
    "space",
    "newline",
    "tab"
]

reserved = {
    'append': 'append',
    'exit': 'exit',
    'list': 'list',
    'print': 'print',
    'printlength': 'printlength',
    'printwords': 'printwords',
    'printwordcount': 'printwordcount',
    'reverse': 'reverse',
    'set': 'set'
}

tokens = tokens + list(reserved.values())

t_plus = r'\+'
t_literal = r'["][a-zA-Z0-9 \W]*["]'  # TODO may not handle /"?
t_end = r';'
t_ignore_space = r'[ ]'


def t_constant(t):
    r'SPACE|TAB|NEWLINE'
    return t


def t_id(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'id')
    return t


def t_error(t):
    raise IllegalCharacter(f"Illegal character {t.value[0]!r} in statement")


def get_tokens(self):
    return self.tokens


class IllegalCharacter(Exception):
    pass
