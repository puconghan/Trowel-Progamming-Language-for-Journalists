import yacc
from lexer import tokens

class Node:
    def __init__(self,type,children=None,value=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.value = value

    def printrec(self):
        for child in self.children:
            child.printrec()
        print self.type, self.value

def p_expression_print(p):
    'expression : PRINT LIST'
    print "Found a print statement"
    p[0] = Node(p[1], [p[2]],'list')
    return p[0]

def p_expression_list(p):
    'LIST : LEFTSQUAREBRACKET LISTITEMS RIGHTSQUAREBRACKET'
    p[0] = Node("list", [], p[2:-1])
    for item in p:
        print item

def p_expression_listitems(p):
    '''LISTITEMS : IDENTIFIER EXTRALIST
                 | empty'''
    p[0] = p[1:]

def p_expression_extralist(p):
    '''EXTRALIST : COMMA IDENTIFIER EXTRALIST
                 | empty'''
    p[0] = p[1:]

def p_empty(p):
    'empty :'
    pass

yacc.yacc()
output = yacc.parse("print [5, 3]")
output.printrec()