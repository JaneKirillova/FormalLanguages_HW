from lex import *

class Node:
    def __init__(self, left, right, name):
        self.left = left
        self.right = right
        self.name = name


class Parser:
    def __init__(self, s):
        self.lex = lexerr(s)
        self.current = next(self.lex)
        self.last_correct = None

    def accept(self, c):
        if self.current == '\0':
            return False
        if self.current.type == c:
            self.last_correct = self.current
            self.current = next(self.lex)
            return True
        return False

    def expr(self):
        if self.current == '\0':
            return None
        l = self.current
        if self.accept('LEFTBRACE'):
            r = self.disj()
            if self.accept('RIGHTBRACE'):
                return r
            return None
        self.last_correct = l
        self.current = next(self.lex)
        if l.type != 'ID':
            return None
        return Node(None, None, l.value)

    def head(self):
        if self.current == '\0':
            return -1
        l = self.current
        self.last_correct = l
        self.current = next(self.lex)
        if l.type != 'ID':
            return None
        return Node(None, None, l.value)


    def disj(self):
        l = self.conj()
        if self.accept('DISJ'):
            r = self.disj()
            if r == None:
                return None
            return Node(l, r, ";")
        return l


    def conj(self):
        l = self.expr()
        if self.accept('CONJ'):
            r = self.conj()
            if r == None:
                return None
            return Node(l, r, ",")
        return l


    def corkscrew (self):
        if self.accept('CORCSCREW'):
            r = self.disj()
            return r
        return None

    def relation(self):
        l = self.head()
        if l == None or l == -1:
            return l
        if self.accept('DOT'):
            return l
        r = self.corkscrew()
        if r == None:
            return None
        if not self.accept('DOT'):
            return None
        return Node(l, r, ':-')


def lexerr(s):
    for c in s:
        yield c
    while True:
        yield '\0'


def pr(node):
    a = "("
    if node.left != None:
        a += pr(node.left)
    a += " " + node.name + " "
    if node.right != None:
        a += pr(node.right)
    a += ')'
    return a


def parse(file_name):
    try:
        l, text = make_list(file_name)
        relations_list = []
        p = Parser(l)
        while p.current:
            tree = p.relation()
            if tree == None:
                if p.last_correct == None:
                    msg = "Syntax error: at line 1, colon 0"
                else:
                    msg = "Syntax error: at line %d, colon %d" % (p.last_correct.lineno, pos_in_line(text, p.last_correct))   
                return False, msg, None             
            elif tree == -1:
                return True, "All relations are correct:", relations_list
            else:
                relations_list.append(pr(tree))
    except Exception as msg:
        return False, str(msg), None


if __name__ == "__main__":
    is_correct, msg, l = parse(sys.argv[1])
    print(msg)
    if is_correct:
        for r in l:
            print(r)