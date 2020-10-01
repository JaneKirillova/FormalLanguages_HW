from parser import parse

def test_correct_1():
	is_correct, msg, l = parse('test/correct_1.txt')
	assert(is_correct)
	assert(msg == "All relations are correct:")
	right_list = ["( f )", "(( f ) :- ( g ))", "(( f ) :- ((( g ) , ( h )) ; ( t )))", "(( f ) :- (( g ) , (( h ) ; ( t ))))"]
	assert(l == right_list)


def test_correct_2():
	is_correct, msg, l = parse('test/correct_2.txt')
	assert(is_correct)
	assert(msg == "All relations are correct:")
	right_list = ["( f )", "(( f ) :- (( a ) , (( h ) , ( k ))))", "(( f ) :- (((( h ) , ( k )) , ( l )) ; ( m )))"]
	assert(l == right_list)

def test_correct_3():
	is_correct, msg, l = parse('test/correct_3.txt')
	assert(is_correct)
	assert(msg == "All relations are correct:")
	right_list = ["(( abc ) :- ( fgh ))", "(( f ) :- (((( gh ) , ( kl )) ; ((( qw ) , ( po )) ; ( k ))) ; ( p )))"]
	assert(l == right_list)

def test_incorrect_1():
	is_correct, msg, l = parse('test/incorrect_1.txt')
	assert(not is_correct)
	assert(msg == "Syntax error: at line 2, colon 6")
	assert(l == None)

def test_incorrect_2():
	is_correct, msg, l = parse('test/incorrect_2.txt')
	assert(not is_correct)
	assert(msg == "Syntax error: at line 1, colon 1")
	assert(l == None)

def test_incorrect_3():
	is_correct, msg, l = parse('test/incorrect_3.txt')
	assert(not is_correct)
	assert(msg == "Syntax error: at line 2, colon 12")
	assert(l == None)

def test_incorrect_4():
	is_correct, msg, l = parse('test/incorrect_4.txt')
	assert(not is_correct)
	assert(msg == "Syntax error: at line 1, colon 12")
	assert(l == None)

def test_incorrect_5():
	is_correct, msg, l = parse('test/incorrect_5.txt')
	assert(not is_correct)
	assert(msg == "Syntax error: illegal character '=' at position 2")
	assert(l == None)


if __name__ == "__main__":
	test_correct_1()
	test_correct_2()
	test_correct_3()
	test_incorrect_1()
	test_incorrect_2()
	test_incorrect_3()
	test_incorrect_4()
	test_incorrect_5()
	print("All tests pass!")
