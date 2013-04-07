################
# PROGRAM:      Trowel Parser
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

##Parser for variable declaration.
# Implemented by Pucong on April 6, 2013.
def p_expression_declaration(p):
    'expression : vartype IDENTIFIER additional'
    # Adding the identifier variable to the locallist.
    typelist.addNewVariable(p[2])
    # Add all variables in the localist to the typelist hashtable with approprate variable types.
    for item in typelist.locallist:
        typelist.addNewType(item, p[1])
    # Building a parser list.
    listofVariable = []
    for item in typelist.locallist:
        listofVariable.append((item, (p[1], "[]")))
    p[0] = ("dec", p[1], listofVariable)
    # Reset the locallist for future declaration tokens.
    typelist.locallist = []

##Parser for variable types.
# Implemented by Pucong on April 6, 2013.
def p_expression_vartype(p):
    '''vartype : URL
               | TEXT
               | NUMBER
               | URLLIST
               | TEXTLIST
               | NUMLIST'''
    p[0] = p[1]

##Parser for additional variable tokens in variable declaration block.
# Implemented by Pucong on April 6, 2013.
def p_additional(p):
    'additional : COMMA IDENTIFIER additional'
    # Adding additional variables to the locallist.
    typelist.addNewVariable(p[2])

##Parser for empty additional variable tokens in variable declaration block.
# Implemented by Pucong on April 6, 2013
def p_additionalempty(p):
    'additional : empty'
    pass

def p_expression_printlist(p):
    'expression : PRINT LIST'
    print "Found a list print statement"
    p[0] = ("func", "printlist", p[2])

def p_expression_printvals(p):
    'expression : PRINT VALS'
    p[0] = ("func", "printvals", p[2])

def p_expression_list(p):
    'LIST : LEFTSQUAREBRACKET LISTITEMS RIGHTSQUAREBRACKET'
    p[0] = ("list", p[2])

def p_expression_listitems(p):
    'LISTITEMS : LISTVALS COMMA LISTITEMS'
    p[0] = p[1] + p[3]

def p_expression_extralist(p):
    'LISTITEMS : LISTVALS'
    p[0] = p[1]

def p_expression_listvals(p):
    '''LISTVALS : URL LISTVALS
                | TEXT LISTVALS'''
    p[0] = [p[1]] + p[2]

def p_expression_listvals_last(p):
    '''LISTVALS : URL
                | TEXT
                | NUM'''
    p[0] = [p[1]]

def p_expression_vals(p):
    '''VALS : URL VALS
            | TEXT VALS
            | NUM VALS'''
    print p[0]
    print p[1:]
    print "This line"
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

parser = yacc.yacc()
    
