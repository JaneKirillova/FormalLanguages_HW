import ply.lex as lex
import sys

reserved = {
    'module': 'MODULE',
    'sig': 'SIG',
    'type': 'TYPE'
}

tokens = [
             'DISJ',
             'CORC',
             'ID',
             'DOT',
             'CONJ',
             'LBC',
             'RBC'
         ] + list(reserved.values())


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


t_DISJ = r'\;'
t_CORC = r'\:\-'
t_DOT = r'\.'
t_CONJ = r'\,'
t_LBC = r'\('
t_RBC = r'\)'


t_ignore = ' \t'

def t_newline(t): 
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  raise Exception ("Syntax error: illegal character '%s' at position %d" % (t.value[0], t.lexpos))
