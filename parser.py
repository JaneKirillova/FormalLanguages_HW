from parsita import *
import sys

class Parser(TextParsers, whitespace=r'[ \t\n\r]*'):
    maybe_id = reg(r'[a-z_][a-zA-Z_0-9]*')
    ID = pred(maybe_id, lambda x: x != "module" and x != "type", "aaaa")
    VAR = reg(r'[A-Z][a-zA-Z_0-9]*')
    DOT = lit('.')
    DISJ = lit(';')
    CONJ = lit(',')
    LBC = lit('(')
    RBC = lit(')')
    CORK = reg(r'\:\-')
    MOD = reg(r'module')


    module = (MOD & ID & DOT) > (lambda xs: "MODULE: " + xs[1] + ".")

    program = ((module & rels) > (lambda xs: xs[0] + "\n" + xs[1])) | rels | module

    rels = ((rel & rels) > (lambda xs: xs[0] + "\n" + xs[1])) | (rel > (lambda x: ''.join(x)))

    rel = ((atom & CORK & disj & DOT) > (lambda xs: ":- (" + xs[0] + ") (" +xs[2] + ")")) | ((atom & DOT) > (lambda xs: xs[0] + "."))

    disj = ((conj & DISJ & disj) > (lambda xs: "DISJ (" + xs[0] + ") (" + xs[2] + ")" )) | conj

    conj = ((expr & CONJ & conj) > (lambda xs: "CONJ (" + xs[0] + ") ("+xs[2] + ")" )) | expr

    expr = ((LBC & disj & RBC) > (lambda xs: " (" + xs[1] + ") ")) | atom

    atom = ((ID & tail) > (lambda xs: "ID(" + xs[0] + ") " +xs[1])) | (ID > (lambda x: "ID(" + x + ")"))

    atom2 = ((ID & tail) > (lambda xs: "ID(" + xs[0] + ") " + xs[1])) | ((VAR & tail) > (lambda xs: "VAR(" + xs[0] + ") " + xs[1])) | (VAR > (lambda x: "VAR(" + x + ")")) | (ID > (lambda x: "ID(" + x + ")"))

    tail = ((braces & tail) > (lambda xs: xs[0] + ' ' + xs[1])) | braces | atom2

    braces = ((LBC & braces & RBC) > (lambda xs: xs[1])) | ((LBC & atom2 & RBC) > (lambda xs: "(" + xs[1] + ")"))


def parser(input_file_name, key):
    input_file = open(input_file_name, 'r')
    text = input_file.read()
    input_file.close()
    output_file_name = input_file_name + '.out'
    output_file = open(output_file_name, 'w')
    if key == "--atom":
        res = Parser.atom.parse(text)
    if key == "--relation":
        res = Parser.rel.parse(text)
    if key == "--relations":
        res = Parser.rels.parse(text)
    if key == "--prog" or key == "":
    	res = Parser.program.parse(text)
    if type(res) == Success:
        output_file.write(res.value)
    else:
    	output_file.write(res.message)
    output_file.close()
    return res


if __name__ == '__main__':
    if len(sys.argv) > 2:
        res = parser(sys.argv[1], sys.argv[2])
    else:
        res = parser(sys.argv[1], "")