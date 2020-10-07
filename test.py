from parser import parse

def test_correct():
	is_correct, res = parse('test/correct')
	assert(is_correct)

def test_incorrect_1():
	is_correct, res = parse('test/incorrect_1')
	assert(not is_correct)
	assert(res == 'Syntax error at line 1')

def test_incorrect_2():
	is_correct, res = parse('test/incorrect_2')
	assert(not is_correct)
	assert(res == 'Syntax error at line 3')

def test_incorrect_3():
	is_correct, res = parse('test/incorrect_3')
	assert(not is_correct)
	assert(res == 'Syntax error at line 5')

def test_incorrect_4():
	is_correct, res = parse('test/incorrect_4')
	assert(not is_correct)
	assert(res == 'Syntax error at line 2')

def test_incorrect_5():
	is_correct, res = parse('test/incorrect_5')
	assert(not is_correct)
	assert(res == 'Syntax error at line 2')

def test_incorrect_6():
	is_correct, res = parse('test/incorrect_6')
	assert(not is_correct)
	assert(res == 'Syntax error at line 1')




if __name__ == '__main__':
	test_correct()
	test_incorrect_1()
	test_incorrect_2()
	test_incorrect_3()
	test_incorrect_4()
	test_incorrect_5()
	test_incorrect_6()
	print("All tests pass!")
