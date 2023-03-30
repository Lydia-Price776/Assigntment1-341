from ply import lex


class Lexer:
    tokens = [
        "constant",
        "id",
        "literal",
        "plus",
        "end",
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
        'reverse': 'reverse',
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
        pos = self.find_column(self.lexer.lexdata, t)
        next_space = self.find_next_space(self.lexer.lexdata, t)
        print("Invalid command or identifier \"" + t.value[0:next_space - pos] + "\"")
        t.lexer.skip(next_space - pos)

    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

    def find_next_space(self, text, token):
        next_space = text.rfind(' ', token.lexpos) + 1
        return next_space
