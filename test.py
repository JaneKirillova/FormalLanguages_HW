from parser import *

def test_id_and_var():
	assert type(Parser.ID.parse('aghewebdwej')) == Success
	assert type(Parser.ID.parse('a123sued')) == Success
	assert type(Parser.VAR.parse('A')) == Success
	assert type(Parser.VAR.parse('XyZ')) == Success
	assert type(Parser.ID.parse('A22')) == Failure
	assert type(Parser.VAR.parse('abc')) == Failure


def test_atom():
	assert type(Parser.atom.parse('a')) == Success
	assert type(Parser.atom.parse('a (b c)')) == Success
	assert type(Parser.atom.parse('a ((b c))')) == Success
	assert type(Parser.atom.parse('a ((b c)) d')) == Success
	assert type(Parser.atom.parse('a ((b    c)) (d)')) == Success
	assert type(Parser.atom.parse('a    (   (b   c)  )   d')) == Success
	assert type(Parser.atom.parse('a (a')) == Failure
	assert type(Parser.atom.parse('X a')) == Failure
	assert type(Parser.atom.parse('(a)')) == Failure


def test_relation():
	assert type(Parser.rel.parse('a.')) == Success
	assert type(Parser.rel.parse('a b.')) == Success
	assert type(Parser.rel.parse('a :- a.')) == Success
	assert type(Parser.rel.parse('a  :- a.')) == Success
	assert type(Parser.rel.parse('a :- a b.')) == Success
	assert type(Parser.rel.parse('a b :- a;b,c.')) == Success
	assert type(Parser.rel.parse('a b :- a;(b, c).')) == Success
	assert type(Parser.rel.parse('a b :- (a;b), c.')) == Success
	assert type(Parser.rel.parse('a b c :- a, b, c.')) == Success
	assert type(Parser.rel.parse('a b :- a;b;c.')) == Success
	assert type(Parser.rel.parse('a (b (c)) :- (a b).')) == Success
	assert type(Parser.rel.parse('a :-.')) == Failure
	assert type(Parser.rel.parse('a ((b) c).')) == Failure
	assert type(Parser.rel.parse('a :- a, b; .')) == Failure
	assert type(Parser.rel.parse('a :- (a, (f, g) o.')) == Failure
	assert type(Parser.rel.parse('a')) == Failure

def test_module():
	assert type(Parser.module.parse('module name.')) == Success
	assert type(Parser.module.parse('module     \n\n\t name     \n\n\n.')) == Success
	assert type(Parser.module.parse('modulemodule.')) == Failure
	assert type(Parser.module.parse('modulo module.')) == Failure
	assert type(Parser.module.parse('mod ule module.')) == Failure
	assert type(Parser.module.parse('module module!')) == Failure


def test_relations():
	assert type(Parser.rels.parse('a. b. c. d.')) == Success
	assert type(Parser.rels.parse('a :- (a , k). \n\n\n\n\t\t t \t\t Y :- a \t\t\t\t\n.')) == Success
	assert type(Parser.rels.parse('a. b')) == Failure


def test_program():
	assert type(Parser.program.parse('module a. \n a :- a. \n a D f :- f R t Rty,  n g; l K; p.')) == Success



if __name__ == "__main__":
	test_id_and_var()
	test_atom()
	test_relation()
	test_module()
	test_relations()
	test_program()
	print("All tests pass!")