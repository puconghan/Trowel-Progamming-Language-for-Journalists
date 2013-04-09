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
#               Modified by Pucong Han on April 9, 2013
################

import sys
import ply.yacc as yacc
from lexer import tokens
import typelist

##Parser for variable declaration.
# Implemented by Pucong on April 6, 2013.
def p_expression_declaration(p):
    'EXPRESSION : INDENTATION VARTYPE IDENTIFIER ADDITIONAL'
    # Adding the identifier variable to the locallist.
    typelist.addNewVariable(p[3])
    # Add all variables in the localist to the typelist hashtable with approprate variable types.
    for item in typelist.locallist:
        typelist.addNewType(item, p[2])
    # Building a parser list.
    listofVariable = []
    for item in typelist.locallist:
        listofVariable.append((item, (p[2], "[]")))
    p[0] = ("dec", p[2], listofVariable)
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
    'EXPRESSION : INDENTATION IDENTIFIER IS VALS'
    if typelist.returnType(p[2]) == p[4][0][0]:
        typelist.addNewValue(p[2], p[4])
        p[0] = ("assign", typelist.returnType(p[2]), p[2], p[4])
    elif typelist.returnType(p[2]) == "Not in typelist":
        #Print error message if type is not declared
        print "Variable: " + str(p[2]) + " is not declared."
        sys.exit()
    else:
        #Print error message if type is miss-matched
        print "Variable: " + str(p[2]) + " assigning type miss matching."
        sys.exit()

##Parser for assigning values to list variables.
# Implemented by Pucong on April 7, 2013
def p_expression_value_list_assignment(p):
    'EXPRESSION : INDENTATION IDENTIFIER IS LIST'
    #This variable stores and checks types in the list.
    typecheck = p[4][0][0]
    #This variable stores predicted list type.
    listtype = ""
    #Checking type consistency. Print error message if type is inconsistent
    for item in p[4]:
        if typecheck == item[0]:
            typecheck = item[0]
        else:
            #Print error message if type is miss-matched.
            print "List item: " + item[2] + " type miss matching."
            sys.exit()
    #Code for predicting list type using list item types.
    if typecheck == "url":
        listtype = "urllist"
    elif typecheck == "text":
        listtype = "textlist"
    elif typecheck == "number":
        listtype = "numlist"
    else:
        print "List: " + p[2] + " item type unrecognized."
        sys.exit()
    if typelist.returnType(p[2]) == listtype:
        typelist.addNewValue(p[2], p[4])
        p[0] = ("assign", listtype, p[2], p[4])
    elif typelist.returnType(p[2]) == "Not in typelist":
        #Print error message if type is not declared.
        print "Variable: " + str(p[2]) + " is not declared."
        sys.exit()
    else:
        #Print error message if type is miss-matched.
        print "Variable: " + str(p[2]) + " assigning type miss matching."
        sys.exit()

##Parser for declaring varibale and assigning values from another variable.
# Implemented by Pucong on April 8, 2013.
def p_expression_value_assignment_between_variables(p):
    'EXPRESSION : INDENTATION IDENTIFIER IS EXISTINGVAR'
    if p[4][0] == "existingvar":
        if len(p[4][2]) == 1:
            if typelist.returnType(p[2]) != p[4][2][0][0]:
                #Print error message if variable is miss-matched.
                print "Type miss-matched of variable: " + p[2]
                sys.exit()
        else:
            typecheck = p[4][2][0][0]
            listtype = ""
            for subitem in p[4][2]:
                if subitem[0] == typecheck:
                    typecheck = subitem[0]
                else:
                    #Print error message if list contains inconsistant types.
                    print "List contains illegal or inconsistant types or values."
                    sys.exit()
            #Code for predicting list type using list item types.
            if typecheck == "url":
                listtype = "urllist"
            elif typecheck == "text":
                listtype = "textlist"
            elif typecheck == "number":
                listtype = "numlist"
            else:
                print "List: " + p[2] + " item type unrecognized."
                sys.exit()
            if typelist.returnType(p[2]) != listtype:
                #Print error message if variable is miss-matched.
                print "Type miss-matched of variable: " + p[2]
                sys.exit()

        typelist.addNewValue(p[2], p[4][2])
        p[0] = ("assign", "variable", p[2], p[4][1])
    else:
        print "Wrong assignment." + "Variable: " + p[4] + " does not contain values."

##Parser for declaring varibale and assigning values.
# Implemented by Pucong on April 7, 2013.
def p_expression_value_declaration_and_assignment(p):
    'EXPRESSION : INDENTATION VARTYPE IDENTIFIER IS VALS'
    if p[2] == p[5][0][0]:
        typelist.addNewType(p[3], p[2])
        typelist.addNewValue(p[3], p[5])
        p[0] = ("assign", p[2], p[3], p[5])
    else:
        #Print error message if type is miss-matched.
        print "Variable: " + str(p[3]) + " declaration type and assigning type miss matching."
        sys.exit()

##Parser for declaring list of varibale and assigning values.
# Implemented by Pucong on April 7, 2013.
def p_expression_value_list_declaration_and_assignment(p):
    'EXPRESSION : INDENTATION VARTYPE IDENTIFIER IS LIST'
    typecheck = p[5][0][0]
    listtype = ""
    for item in p[5]:
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
        print "List: " + p[3] + " item type unrecognized."
        sys.exit()
    if p[2] == listtype:
        typelist.addNewType(p[3], p[2])
        typelist.addNewValue(p[3], p[5])
        p[0] = ("assign", listtype, p[3], p[5])
    else:
        #Print error message if type is miss-matched.
        print "Variable: " + str(p[3]) + " declaration type and assigning type miss matching."
        sys.exit()

##Parser for declaring varibale and assigning values from another variable.
# Implemented by Pucong on April 8, 2013.
def p_expression_value_declaration_and_assignment_between_variables(p):
    'EXPRESSION : INDENTATION VARTYPE IDENTIFIER IS EXISTINGVAR'
    if p[5][0] == "existingvar":
        if len(p[5][2]) == 1:
            if typelist.returnType(p[3]) != p[5][2][0][0]:
                #Print error message if variable is miss-matched.
                print "Type miss-matched of variable: " + p[3]
                sys.exit()
        else:
            typecheck = p[5][2][0][0]
            listtype = ""
            for subitem in p[5][2]:
                if subitem[0] == typecheck:
                    typecheck = subitem[0]
                else:
                    #Print error message if list contains inconsistant types.
                    print "List contains illegal or inconsistant types or values."
                    sys.exit()
            #Code for predicting list type using list item types.
            if typecheck == "url":
                listtype = "urllist"
            elif typecheck == "text":
                listtype = "textlist"
            elif typecheck == "number":
                listtype = "numlist"
            else:
                print "List: " + p[3] + " item type unrecognized."
                sys.exit()
            if listtype != p[2]:
                #Print error message if variable is miss-matched.
                print "Type miss-matched of variable: " + p[2]
                sys.exit()
        typelist.addNewType(p[3], p[2])
        typelist.addNewValue(p[3], p[5][2])
        p[0] = ("assign", "variable", p[3], p[5][1])
    else:
        print "Wrong assignment." + "Variable: " + p[5] + " does not contain values."

##Parser for printing a list.
# Implemented by Victoria Mo and Robert Walport on April 6, 2013.
def p_expression_printlist(p):
    'EXPRESSION : INDENTATION PRINT LIST'
    print "Found a list print statement"
    p[0] = ("func", "printlist", p[3])

##Parser for printing values.
# Implemented by Victoria Mo and Robert Walport on April 6, 2013.
def p_expression_printvals(p):
    'EXPRESSION : INDENTATION PRINT VALS'
    p[0] = ("func", "printvals", p[3])

def p_expression_empty_line(p):
    'EXPRESSION : INDENTATION EMPTY'
    p[0] = ("emptyline")

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

##Parser for tab input.
# Implemented by Pucong on April 9, 2013
# TODO: Need to implement local scope of indentation.
def p_expression_tab(p):
    'INDENTATION : TAB INDENTATION'
    pass

def p_expression_tab_empty(p):
    'INDENTATION : EMPTY'
    pass

def p_empty(p):
    'EMPTY :'
    pass
    
parser = yacc.yacc()
