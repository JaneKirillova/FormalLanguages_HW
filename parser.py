'''
input ----> relation. | relation . input
relation -> atom      | atom :- disj
disj -----> conj      | conj ; disj
conj -----> expr      | expr , conj
expr -----> atom      | ( disj )
atom -----> ID        | ID tail
tail -----> atom      | braces       | braces tail
braces ---> ( atom )  | ( braces )


'''


import ply.yacc as yacc

from lex import*

import sys


def p_input_relation(p):
	'input : relation DOT'
	p[0] = p[1]

def p_input_input(p):
	'input : relation DOT input'
	p[0] = p[1] + '\n' + p[3]


def p_relation_corc(p):
	'relation : atom CORC disj'
	p[0] = ':- (' + p[1] + ') (' + p[3] + ')'

def p_relation_dot(p):
	'relation : atom'
	p[0] = p[1]


def p_disj_disj(p):
	'disj : conj DISJ disj'
	p[0] = ' DISJ (' + p[1] + ') (' + p[3] + ')'


def p_disj_conj(p):
	'disj : conj'
	p[0] = p[1]


def p_conj_conj(p): 
	'conj : expr CONJ conj'
	p[0] = ' CONJ (' + p[1] + ') (' + p[3] + ')'

def p_conj_expr(p):
	'conj : expr'
	p[0] = p[1]


def p_expr_disj(p):
	'expr : LBC disj RBC'
	p[0] = '( ' + p[2] + ' )'

def p_expr_atom(p):
	'expr : atom'
	p[0] = p[1]


def p_atom_id(p):
	'atom : ID'
	p[0] = '( ' + p[1] + ' )'

def p_atom_tail(p):
	'atom : ID tail'
	p[0] = '( ' + p[1] + ' ) ' + p[2]


def p_tail_atom(p):
	'tail : atom'
	p[0] = p[1]


def p_tail_braces(p):
	'tail : braces'
	p[0] = '(' + p[1] + ')'


def p_tail_braces_tail(p):
	'tail : braces tail'
	p[0] = '(' + p[1] + ')' + p[2]

def p_braces_atom(p):
	'braces : LBC atom RBC'
	p[0] = '( ' + p[2] + ' )'

def p_braces_braces(p):
	'braces : LBC braces RBC'
	p[0] = '(' + p[2] + ')'

def p_error(p):
	if p is not None:
		raise Exception("Syntax error at line %s" % p.lineno)
	else:
		raise Exception("Syntax error at last line")




def parse(input_file_name):
    lexer = lex.lex()
    parser = yacc.yacc()
    input_file = open(input_file_name, 'r')
    text = input_file.read()
    input_file.close()
    output_file_name = input_file_name + '.out'
    output_file = open(output_file_name, 'w')
    try:
        result=parser.parse(text)
        output_file.write(result)
        output_file.close()
        return True, result
    except Exception as msg:
        output_file.write(str(msg))
        output_file.close()
        return False, str(msg)

if __name__ == '__main__':
	is_c, res = parse(sys.argv[1])
