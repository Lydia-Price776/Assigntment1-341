from ply import lex


class Lexer:
    tokens = [
        "constant",
        "id",
        "literal",
        "plus",
        "end"
    ]

    reserved = {
        'append': 'append',
        'list': 'list',
        'exit': 'exit',
        'print': 'print',
        'printlength': 'printlength',
        'printwords': 'printwords',
        'printwordcount': 'printwordcount',
        'set': 'set',
        'reverse': 'reverse'
    }

    tokens = tokens + list(reserved.values())

    t_literal = r'["][a-zA-Z0-9 \W]*["]'  # TODO may not handle /"?
    t_plus = r'\+'
    t_end = r';'
    t_ignore_space = r'[ ]'

    def t_constant(self, t):
        r'SPACE|TAB|NEWLINE'
        return t

    def t_id(self, t):
        r'[a-zA-Z][a-zA-Z0-9]*'
        t.type = self.reserved.get(t.value, 'id')
        return t

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def t_error(self, t):
        raise IllegalCharacter(f"Illegal character {t.value[0]!r} in statement")

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)


class IllegalCharacter(Exception):
    pass
