import ply.lex as lex
import sys

reserved = {
    'module': 'MODULE',
    'sig': 'SIG',
    'type': 'TYPE'
}

tokens = [
             'DISJ',
             'CORCSCREW',
             'ID',
             'DOT',
             'CONJ',
             'LEFTBRACE',
             'RIGHTBRACE'
         ] + list(reserved.values())


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


t_DISJ = r'\;'
t_CORCSCREW = r'\:\-'
t_DOT = r'\.'
t_CONJ = r'\,'
t_LEFTBRACE = r'\('
t_RIGHTBRACE = r'\)'

t_ignore = '" \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    raise Exception ("Syntax error: illegal character '%s' at position %d" % (t.value[0], t.lexpos))

def pos_in_line(text, t):
    line_start_pos = text.rfind('\n', 0, t.lexpos)
    position = t.lexpos - line_start_pos
    return position




def make_list(file_name):
    lexer = lex.lex()
    input_file = open(file_name)
    text = input_file.read()
    lexer.input(text)
    input_file.close()
    l = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        l.append(tok)
    return l, text