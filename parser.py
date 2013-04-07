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
import sys
import yacc
from lexer import tokens
import typelist

##Parser for variable declaration.
# Implemented by Pucong on April 6, 2013.
def p_expression_declaration(p):
    'EXPRESSION : VARTYPE IDENTIFIER ADDITIONAL'
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

#Parser for additional variable tokens.
def p_expression_additional(p):
    'ADDITIONAL : COMMA IDENTIFIER ADDITIONAL'
    # Adding additional variables to the locallist.
    typelist.addNewVariable(p[2])

#Printing error messages for missing comma between variables.
def p_expression_additional_error(p):
    'ADDITIONAL : COMMA IDENTIFIER IDENTIFIER ADDITIONAL'
    print "Missing comma between: " + p[2] + " and " + p[3]
    sys.exit()

#Parser for empty additional variable tokens.
def p_expression_additional_empty(p):
    'ADDITIONAL : EMPTY'
    pass

##Parser for assigning values to variables.
# Implemented by Pucong on April 7, 2013
# TODO: 1. Assignment error messages (type miss-matching).
#       2. Assignment for all variable types (right now only capture three variable types).
def p_expression_value_assignment(p):
    'EXPRESSION : IDENTIFIER IS VALS'
    if typelist.returnType(p[1]) == p[3][0][0]:
        p[0] = ("assign", p[1], p[3])
    else:
        print "Variable: " + str(p[1]) + " assigning type miss matching."
        sys.exit()

##Parser for declaring varibale and assigning values.
# Implemented by Pucong on April 7, 2013
def p_expression_value_declaration_and_assignment(p):
    'EXPRESSION : VARTYPE IDENTIFIER IS VALS'
    if p[1] == p[4][0][0]:
        typelist.addNewType(p[2], p[1])
        p[0] = ("assign", p[2], p[4])
    else:
        print "Variable: " + str(p[2]) + " declaration type and assigning type miss matching."
        sys.exit()

##Parser for variable types.
# Implemented by Pucong on April 6, 2013.
def p_expression_vartype(p):
    '''VARTYPE : URL
               | TEXT
               | NUMBER
               | URLLIST
               | TEXTLIST
               | NUMLIST'''
    p[0] = p[1]


##Parser for printing a list.
# Implemented by Victoria Mo and Robert Walport on April 6, 2013.
def p_expression_printlist(p):
    'EXPRESSION : PRINT LIST'
    print "Found a list print statement"
    p[0] = ("func", "printlist", p[2])

def p_expression_list(p):
    'LIST : LEFTSQUAREBRACKET LISTITEMS RIGHTSQUAREBRACKET'
    p[0] = p[2]

def p_expression_listitems(p):
    'LISTITEMS : LISTVALS COMMA LISTITEMS'
    p[0] = p[1] + p[3]

def p_expression_extralist(p):
    'LISTITEMS : LISTVALS'
    p[0] = p[1]

def p_expression_listvals(p):
    '''LISTVALS : URLEXP LISTVALS
                | TEXTEXP LISTVALS'''
    p[0] = [p[1]] + p[2]

def p_expression_listvals_last(p):
    '''LISTVALS : URLEXP
                | TEXTEXP'''
    p[0] = [p[1]]

##Parser for printing values.
# Implemented by Victoria Mo and Robert Walport on April 6, 2013.
def p_expression_printvals(p):
    'EXPRESSION : PRINT VALS'
    p[0] = ("func", "printvals", p[2])

def p_expression_vals(p):
    '''VALS : URLEXP VALS
            | TEXTEXP VALS
            | NUMEXP VALS'''
    p[0] = [p[1]] + p[2]

def p_expression_vals_last(p):
    '''VALS : URLEXP
            | TEXTEXP
            | NUMEXP'''
    p[0] = [p[1]]

def p_expression_text(p):
    'TEXTEXP : TEXTVAL'
    p[0] = ('text', p[1])

def p_expression_url(p):
    'URLEXP : URLVAL'
    p[0] = ('url', p[1])

def p_expression_number(p):
    'NUMEXP : NUMVAL'
    p[0] = ('number', p[1])

def p_empty(p):
    'EMPTY :'
    pass
    
parser = yacc.yacc()
    
