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
#               Modified by Pucong Han on April 7, 2013
#               Modified by Pucong Han, Robert Walport and Victoria Mo on April 8, 2013
################

import sys
import ply.yacc as yacc
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
def p_expression_value_assignment(p):
    'EXPRESSION : IDENTIFIER IS VALS'
    if typelist.returnType(p[1]) == p[3][0][0]:
        typelist.addNewValue(p[1], p[3])
        p[0] = ("assign", typelist.returnType(p[1]), p[1], p[3])
    elif typelist.returnType(p[1]) == "Not in typelist":
        #Print error message if type is not declared
        print "Variable: " + str(p[1]) + " is not declared."
        sys.exit()
    else:
        #Print error message if type is miss-matched
        print "Variable: " + str(p[1]) + " assigning type miss matching."
        sys.exit()

##Parser for assigning values to list variables.
# Implemented by Pucong on April 7, 2013
def p_expression_value_list_assignment(p):
    'EXPRESSION : IDENTIFIER IS LIST'
    #This variable stores and checks types in the list.
    typecheck = p[3][0][0]
    #This variable stores predicted list type.
    listtype = ""
    #Checking type consistency. Print error message if type is inconsistent
    for item in p[3]:
        if typecheck == item[0]:
            typecheck = item[0]
        else:
            #Print error message if type is miss-matched.
            print "List item: " + item[1] + " type miss matching."
            sys.exit()
    #Code for predicting list type using list item types.
    if typecheck == "url":
        listtype = "urllist"
    elif typecheck == "text":
        listtype = "textlist"
    elif typecheck == "number":
        listtype = "numlist"
    else:
        print "List: " + p[1] + " item type unrecognized."
        sys.exit()
    if typelist.returnType(p[1]) == listtype:
        typelist.addNewValue(p[1], p[3])
        p[0] = ("assign", listtype, p[1], p[3])
    elif typelist.returnType(p[1]) == "Not in typelist":
        #Print error message if type is not declared.
        print "Variable: " + str(p[1]) + " is not declared."
        sys.exit()
    else:
        #Print error message if type is miss-matched.
        print "Variable: " + str(p[1]) + " assigning type miss matching."
        sys.exit()

##Parser for declaring varibale and assigning values.
# Implemented by Pucong on April 7, 2013.
def p_expression_value_declaration_and_assignment(p):
    'EXPRESSION : VARTYPE IDENTIFIER IS VALS'
    if p[1] == p[4][0][0]:
        typelist.addNewType(p[2], p[1])
        typelist.addNewValue(p[2], p[4])
        p[0] = ("assign", p[1], p[2], p[4])
    else:
        #Print error message if type is miss-matched.
        print "Variable: " + str(p[2]) + " declaration type and assigning type miss matching."
        sys.exit()

##Parser for declaring varibale and assigning values.
# Implemented by Pucong on April 8, 2013.
def p_expression_value_declaration_and_assignment_between_variables(p):
    'EXPRESSION : IDENTIFIER IS EXISTINGVAR'
    if p[3][0] == "existingvar":
        typelist.addNewValue(p[1], p[3][2])
        p[0] = ("assign", typelist.returnType(p[1]), p[1], typelist.returnValue(p[1]))
    else:
        print "Wrong assignment." + "Variable: " + p[3] + " does not contain values."

##Parser for declaring list of varibale and assigning values.
# Implemented by Pucong on April 7, 2013.
def p_expression_value_list_declaration_and_assignment(p):
    'EXPRESSION : VARTYPE IDENTIFIER IS LIST'
    typecheck = p[4][0][0]
    listtype = ""
    for item in p[4]:
        if typecheck == item[0]:
            typecheck = item[0]
        else:
            #Print error message if type is miss-matched.
            print "List item: " + item[1] + " type miss matching."
            sys.exit()
    #Code for predicting list type using list item types.
    if typecheck == "url":
        listtype = "urllist"
    elif typecheck == "text":
        listtype = "textlist"
    elif typecheck == "number":
        listtype = "numlist"
    else:
        #Print error message if type is unrecognized (unpredictable from the list elements).
        print "List: " + p[2] + " item type unrecognized."
        sys.exit()
    if p[1] == listtype:
        typelist.addNewType(
            p[2], p[1])
        typelist.addNewValue(p[2], p[4])
        p[0] = ("assign", listtype, p[2], p[4])
    else:
        #Print error message if type is miss-matched.
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

##Basic building blocks
# Created by Victoria Mo and Robert Walport on April 6, 2013.
# Modified by Pucong Han on April 8, 2013
def p_expression_check_variable(p):
    'EXISTINGVAR : IDENTIFIER'
    if typelist.returnType(p[1]) == "Not in typelist":
        print "Not a variable"
    else:
        print "Find variable: " + str(p[1]) + " in the typelist."
        p[0] = ("existingvar", p[1], typelist.returnValue(p[1]))

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
                | TEXTEXP LISTVALS
                | NUMEXP LISTVALS'''
    p[0] = [p[1]] + p[2]

def p_expression_listvals_last(p):
    '''LISTVALS : URLEXP
                | TEXTEXP
                | NUMEXP'''
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
