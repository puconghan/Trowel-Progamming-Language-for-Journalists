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
import typelist

def p_expression_urllist(p):
    'expression : URLLIST IDENTIFIER additionalurl'
    # Adding variable name and type to the typelist.
    typelist.addNewType(p[2], "URLLIST")
    # Building the sementic list
    temp = typelist.returnLocalVariables()
    listofURLLIST = []
    for item in temp:
        listofURLLIST.append((item, ("urllist", "[]")))
    p[0] = ("dec", "urllist", listofURLLIST)
    typelist.locallist = []

def p_additionalurl(p):
    'additionalurl : COMMA IDENTIFIER additionalurl'
    # Adding variable name and type to the typelist.
    typelist.addNewType(p[2], "URLLIST")

def p_additional(p):
    'additionalurl : empty'
    pass

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

# def p_expression_printlist(p):
#     'expression : PRINT LIST'
#     print "Found a list print statement"
#     p[0] = ("print", p[2])

def p_expression_printvals(p):
    'expression : PRINT VALS'
    p[0] = ("func", "printvals", p[2])

# def p_expression_list(p):
#     'LIST : LEFTSQUAREBRACKET LISTITEMS RIGHTSQUAREBRACKET'
#     p[0] = ("list", p[2:-1])

# def p_expression_listitems(p):
#     '''LISTITEMS : IDENTIFIER EXTRALIST
#                  | empty'''
#     p[0] = p[1:]

# def p_expression_extralist(p):
#     '''EXTRALIST : COMMA IDENTIFIER EXTRALIST
#                  | empty'''
#     p[0] = p[1:]


def p_expression_vals(p):
    '''VALS : URL VALS
            | TEXT VALS
            | NUM VALS'''
    p[0] = [p[1]] + p[2]

def p_expression_vals_last(p):
    '''VALS : URL
            | TEXT
            | NUM'''
    p[0] = [p[1]]

def p_expression_text(p):
    'NUM : TEXTVAL'
    p[0] = ('text', p[1])

def p_expression_url(p):
    'NUM : URLVAL'
    p[0] = ('url', p[1])

def p_expression_number(p):
    'NUM : NUMVAL'
    p[0] = ('number', p[1])

def p_empty(p):
    'empty :'
    pass

# def p_exp_print(p):
#     'exp : print optargs'
#     p[0] = ("func", p[1], p[2])

# def p_exp_number(p):
#     'exp : NUMVAL'
#     p[0] = ("number", p[1])

# def p_optargs(p):
#     'optargs : args'
#     p[0] = p[1] # the work happens in "args"

# def p_optargsempty(p):
#     'optargs : '
#     p[0] = [] # no arguments -> return the empy list

# def p_args(p):
#     'args : exp COMMA args'
#     p[0] = [p[1]] + p[3]

# def p_args_last(p): # one argument
#     'args : exp'
#     p[0] = [p[1]]


parser = yacc.yacc()
    
