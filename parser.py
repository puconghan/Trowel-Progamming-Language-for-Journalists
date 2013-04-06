################
# PROGRAM:      Trowel
# DESCRIPTION:  The Trowel programming language is intended to aid in the web scraping that we all do on a daily basis,
#               but it is especially targeted to the needs and technical capacities of journalists. This program is the
#               parser of Trowel used to build the abstract syntax tree using tokens
# 
# LICENSE:      ---OPTIONAL---
# REFERENCES:   Python Lex-Yacc Documentation (http://www.dabeaz.com/ply/)
# OUTPUT:       Abstract syntax tree
# 
# AUTHOR(S):
#               Pucong Han (ph2369@columbia.edu)
#               Victoria Mo (vm2355@columbia.edu)
#               Hareesh Radhakrishnan (hr2318@columbia.edu)
#               David Tagatac (dtagatac@cs.columbia.edu)
#               Robert Walport (robertwalport@gmail.com)
# MODIFICATIONS:
#               Created by Robert Walport on April 1, 2013
#               Modified by all team authors on April 1, 2013
#               Modified by all team authors on April 6, 2013
################

import yacc
from lexer import tokens

# class Node:
#     def __init__(self,type,children=None,value=None):
#          self.type = type
#          if children:
#               self.children = children
#          else:
#               self.children = [ ]
#          self.value = value

#     def printrec(self):
#         for child in self.children:
#             child.printrec()
#         print self.type, self.value

def p_expression_printlist(p):
    'expression : PRINT LIST'
    print "Found a list print statement"
    p[0] = ("print", p[2])

def p_expression_printvals(p):
    'expression : PRINT VALS'
    print "Found a val print statement"
    p[0] = ("print", p[2])

def p_expression_list(p):
    'LIST : LEFTSQUAREBRACKET LISTITEMS RIGHTSQUAREBRACKET'
    p[0] = ("list", p[2:-1])

def p_expression_listitems(p):
    '''LISTITEMS : IDENTIFIER EXTRALIST
                 | empty'''
    p[0] = p[1:]

def p_expression_extralist(p):
    '''EXTRALIST : COMMA IDENTIFIER EXTRALIST
                 | empty'''
    p[0] = p[1:]

def p_expression_vals(p):
    '''VALS : URL VALS
            | TEXT VALS
            | NUMBER VALS
            | empty'''
    p[0] = ("vals", p[])

def p_empty(p):
    'empty :'
    pass

trparser = yacc.yacc()
output = trparser.parse("print [5, 3]")
print output