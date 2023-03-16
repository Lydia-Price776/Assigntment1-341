

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
t_literal = r'["][a-zA-Z0-9 ]*["]'
t_end = r';'
t_ignore_space = r'[ ]'


def t_constant(t):
    r'SPACE|TAB|NEWLINE'
    return t


def t_id(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'id') or t_constant(t.value)  # Check for reserved words and Constants
    return t


def t_error(t):
    print(f"Illegal character {t.value[0]!r} on line {t.lexer.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()
lexer.input('SPACE NEWLINE TAB YEET')

for token in lexer:
    print(token)

