from ply import lex


class Lexer:
    tokens = [
        "id",
        "integer"
    ]

    t_integer = r'[0-9]+'
    t_id = r'[a-zA-Z][a-zA-Z0-9]*'

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
