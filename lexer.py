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

    t_literal = r'(["])([^\\]*?(?:\\.[^\\]*?)*)(["])'
    t_plus = r'\+'
    t_end = r';'
    t_ignore_space = r'[ ]'
    t_ignore_newline = r'[\n]'

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

    def t_id(self, t):
        r'[a-zA-Z][a-zA-Z0-9]*'
        t.type = self.reserved.get(t.value, 'id')
        return t

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def t_error(self, t):
        print(f"Illegal character {t.value[0]} given in Statement ")
