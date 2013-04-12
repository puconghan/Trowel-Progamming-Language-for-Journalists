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
#               Modified by Pucong Han, Robert Walport and Victoria Mo on April 10, 2013
#               Modified by Pucong on April 11, 2013.
################

import sys
import ply.yacc as yacc
from lexer import tokens
import typelist

##Parser for variable declaration.
# Implemented by Pucong on April 6, 2013.
# Modified by Pucong on April 9, 2013.
# Modified by Pucong on April 10, 2013.
def p_expression_declaration(p):
    'EXPRESSION : INDENTATION VARTYPE IDENTIFIER ADDITIONAL'
    typelist.indentationCheck(p[1][1])
    # Adding the identifier variable to the locallist.
    typelist.addNewVariable(p[3])
    # Add all variables in the localist to the typelist hashtable with approprate variable types.
    for item in typelist.locallist:
        typelist.addNewType(item, p[2], p[1][1])
    # Building a parser list.
    listofVariable = []
    for item in typelist.locallist:
        listofVariable.append((item, (p[2], "[]")))
    p[0] = ("dec", p[2], p[1][1], listofVariable)
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
# Modified by Pucong on April 9, 2013.
# Modified by Pucong on April 10, 2013.
def p_expression_value_assignment(p):
    'EXPRESSION : INDENTATION IDENTIFIER IS VALS'
    typelist.indentationCheck(p[1][1])
    if typelist.returnType(p[2], p[1][1]) == p[4][0][0]:
        typelist.addNewValue(p[2], p[4], p[1][1])
        p[0] = ("assign", typelist.returnType(p[2], p[1][1]), p[1][1], p[2], p[4])
    elif typelist.returnType(p[2], p[1][1]) == "Not in typelist":
        #Print error message if type is not declared
        print "Variable: " + str(p[2]) + " is not declared."
        sys.exit()
    else:
        #Print error message if type is miss-matched
        print "Variable: " + str(p[2]) + " assigning type miss matching."
        sys.exit()

##Parser for assigning values to list variables.
# Implemented by Pucong on April 7, 2013
# Modified by Pucong on April 9, 2013.
# Modified by Pucong on April 10, 2013.
def p_expression_value_list_assignment(p):
    'EXPRESSION : INDENTATION IDENTIFIER IS LIST'
    typelist.indentationCheck(p[1][1])
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
    if typelist.returnType(p[2], p[1][1]) == listtype:
        typelist.addNewValue(p[2], p[4], p[1][1])
        p[0] = ("assign", listtype, p[1][1], p[2], p[4])
    elif typelist.returnType(p[2], p[1][1]) == "Not in typelist":
        #Print error message if type is not declared.
        print "Variable: " + str(p[2]) + " is not declared."
        sys.exit()
    else:
        #Print error message if type is miss-matched.
        print "Variable: " + str(p[2]) + " assigning type miss matching."
        sys.exit()

##Parser for assigning values from another variable.
# Implemented by Pucong on April 8, 2013.
# Modified by Pucong on April 9, 2013.
# Modified by Pucong on April 10, 2013.
# Modified by Pucong on April 11, 2013.
def p_expression_value_assignment_between_variables(p):
    'EXPRESSION : INDENTATION IDENTIFIER IS EXISTINGVAR'
    typelist.indentationCheck(p[1][1])
    if p[4][0] == "existingvar":
        indentationUp = p[1][1]
        while typelist.returnValue(p[4][1], indentationUp) == "Not in vallist" and indentationUp >= 0:
            indentationUp -= 1
        if typelist.returnValue(p[4][1], indentationUp) == "Not in vallist":
            print "Variable: " + str(p[4][1]) + " is not not accessible. Could not find it from local and global scope."
            sys.exit()
        typelist.addNewValue(p[2], typelist.returnValue(p[4][1], indentationUp), p[1][1])
        p[0] = ("assign", "variable", p[1][1], p[2], p[4][1])
    else:
        print "Wrong assignment." + "Variable: " + p[4] + " does not contain values."

##Parser for assigning values from the read function.
# Implemented by Pucong on April 10, 2013.
def p_expression_value_assignment_from_read_function(p):
    'EXPRESSION : INDENTATION IDENTIFIER IS READ FILENAME'
    typelist.indentationCheck(p[1][1])
    if typelist.returnType(p[2], p[1][1]) != "urllist":
        print "Variable: " + p[2] + " must be an urllist. Read function return a list."
        sys.exit()
    else:
        try:
            read_url_list = []
            with open(p[5], "r") as inputfile:
                for item in inputfile:
                    read_url_list.append(("url", item.rstrip('\r\n')))
            typelist.addNewValue(p[2], read_url_list, p[1][1])
            p[0] = ("assign", "urllist", p[1][1], p[2], read_url_list)
        except IOError:
            print "Error: can\'t find file or read data"
            sys.exit()

##Parser for declaring varibale and assigning values.
# Implemented by Pucong on April 7, 2013.
# Modified by Pucong on April 9, 2013.
# Modified by Pucong on April 10, 2013.
def p_expression_value_declaration_and_assignment(p):
    'EXPRESSION : INDENTATION VARTYPE IDENTIFIER IS VALS'
    typelist.indentationCheck(p[1][1])
    if p[2] == p[5][0][0]:
        typelist.addNewType(p[3], p[2], p[1][1])
        typelist.addNewValue(p[3], p[5], p[1][1])
        p[0] = ("assign", p[2], p[1][1], p[3], p[5])
    else:
        #Print error message if type is miss-matched.
        print "Variable: " + str(p[3]) + " declaration type and assigning type miss matching."
        sys.exit()

##Parser for declaring list of varibale and assigning values.
# Implemented by Pucong on April 7, 2013.
# Modified by Pucong on April 9, 2013.
# Modified by Pucong on April 10, 2013.
def p_expression_value_list_declaration_and_assignment(p):
    'EXPRESSION : INDENTATION VARTYPE IDENTIFIER IS LIST'
    typelist.indentationCheck(p[1][1])
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
        typelist.addNewType(p[3], p[2], p[1][1])
        typelist.addNewValue(p[3], p[5], p[1][1])
        p[0] = ("assign", listtype, p[1][1], p[3], p[5])
    else:
        #Print error message if type is miss-matched.
        print "Variable: " + str(p[3]) + " declaration type and assigning type miss matching."
        sys.exit()

##Parser for declaring varibale and assigning values from another variable.
# Implemented by Pucong on April 8, 2013.
# Modified by Pucong on April 9, 2013.
# Modified by Pucong on April 10, 2013.
# Modified by Pucong on April 11, 2013.
def p_expression_value_declaration_and_assignment_between_variables(p):
    'EXPRESSION : INDENTATION VARTYPE IDENTIFIER IS EXISTINGVAR'
    typelist.indentationCheck(p[1][1])
    if p[5][0] == "existingvar":
        typelist.addNewType(p[3], p[2], p[1][1])
        indentationUp = p[1][1]
        while typelist.returnValue(p[5][1], indentationUp) == "Not in vallist" and indentationUp > 0:
            indentationUp -= 1
        if typelist.returnValue(p[5][1], indentationUp) == "Not in vallist":
            print "Variable: " + str(p[5][1]) + " is not not accessible. Could not find it from local and global scope."
            sys.exit()
        typelist.addNewValue(p[3], typelist.returnValue(p[5][1], indentationUp), p[1][1])
        p[0] = ("assign", "variable", p[1][1], p[3], p[5][1])
    else:
        print "Wrong assignment." + "Variable: " + p[5] + " does not contain values."

##Parser for declaring and assigning values from the read function.
# Implemented by Pucong on April 10, 2013.
def p_expression_value_assignment_from_read_function(p):
    'EXPRESSION : INDENTATION VARTYPE IDENTIFIER IS READ FILENAME'
    typelist.indentationCheck(p[1][1])
    if p[2] != "urllist":
        print "Variable: " + p[3] + " must be a urllist. Read function returns a urllist."
        sys.exit()
    else:
        typelist.addNewType(p[3], p[2], p[1][1])
        try:
            read_url_list = []
            with open(p[6], "r") as inputfile:
                for item in inputfile:
                    read_url_list.append(("url", item.rstrip('\r\n')))
            typelist.addNewValue(p[3], read_url_list, p[1][1])
            p[0] = ("assign", "urllist", p[1][1], p[3], read_url_list)
        except IOError:
            print "Error: can\'t find file or read data"
            sys.exit()

##Parser for saving urllist to a file.
# Implemented by Pucong on April 10, 2013.
def p_expression_save_to_file(p):
    'EXPRESSION : INDENTATION SAVE IDENTIFIER INTO FILENAME'
    typelist.indentationCheck(p[1][1])
    if typelist.returnType(p[3], p[1][1]) != "urllist":
        print "Variable: " + p[3] + " must be a urllist. Save function must save a urllist to an external txt file."
        sys.exit()
    else:
        p[0] = ("save", "urllist", p[1][1], p[3], p[5])


##Parser for appending an url into a file.
# Implemented by Pucong Han on April 10, 2013.
def p_expression_append_url_to_file(p):
    'EXPRESSION : INDENTATION APPEND URLVAL INTO FILENAME'
    typelist.indentationCheck(p[1][1])
    p[0] = ("append", "url", p[1][1], p[3].replace("'", ""), p[5])

##Parser for appending an url variable into a file.
# Implemented by Pucong Han on April 10, 2013.
def p_expression_append_urlvariable_to_file(p):
    'EXPRESSION : INDENTATION APPEND EXISTINGVAR INTO FILENAME'
    typelist.indentationCheck(p[1][1])
    indentationUp = p[1][1]
    while typelist.returnValue(p[3][1], indentationUp) == "Not in vallist" and indentationUp > 0:
        indentationUp -= 1
    if typelist.returnValue(p[3][1], indentationUp) == "Not in vallist":
        print "Variable: " + str(p[3][1]) + " is not not accessible. Could not find it from local and global scope."
        sys.exit()
    if typelist.returnType(p[3][1], indentationUp) != "url":
        print "Variable: " + str(p[3][1]) + " must be a urllist. Must append a url variable to an existing txt file."
        sys.exit()
    p[0] = ("append", "url", p[1][1], typelist.returnValue(p[3][1], indentationUp)[0][1], p[5])
    print p[0]

def p_expression_function(p):
    'EXPRESSION : INDENTATION FUNCTION'
    typelist.indentationCheck(p[1][1])
    p[0] = p[2]

##Parser for combining a url and text or number
# need to be able to do combine combine urlexp and textexp and numexp
# embedded functions are in parentheses
def p_expression_combine(p):
    '''FUNCTION : COMBINE URLEXP AND TEXTEXP
                | COMBINE URLEXP AND NUMEXP'''
    p[0] = ("func", "combine", 0, ('url', str(p[2][1]) + str(p[4][1])))

##Parser for printing a list.
# Implemented by Victoria Mo and Robert Walport on April 6, 2013.
# Modified by Pucong on April 9, 2013.
def p_expression_printlist(p):
    'EXPRESSION : INDENTATION PRINT LIST'
    typelist.indentationCheck(p[1][1])
    print "Found a list print statement"
    p[0] = ("func", "printlist", p[1][1], p[3])

##Parser for printing values.
# Implemented by Victoria Mo and Robert Walport on April 6, 2013.
# Modified by Pucong on April 9, 2013.
def p_expression_printvals(p):
    'EXPRESSION : INDENTATION PRINT VALS'
    typelist.indentationCheck(p[1][1])
    p[0] = ("func", "printvals", p[1][1], p[3])

def p_expression_empty_line(p):
    'EXPRESSION : INDENTATION EMPTY'
    typelist.indentationCheck(p[1][1])
    p[0] = ("emptyline")

##Basic building blocks
# Created by Victoria Mo and Robert Walport on April 6, 2013.
# Modified by Pucong Han on April 8, 2013
# Modified by Pucong Han on April 9, 2013.
def p_expression_check_variable(p):
    'EXISTINGVAR : IDENTIFIER'
    p[0] = ("existingvar", p[1])

##Parser for variable types.
# Implemented by Pucong Han on April 6, 2013.
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

def p_expression_vals_func(p):
    'VALS : LEFTPAREN FUNCTION RIGHTPAREN VALS'
    p[0] = [p[2]] + p[4]

def p_expression_vals_last(p):
    '''VALS : URLEXP
            | TEXTEXP
            | NUMEXP'''
    p[0] = [p[1]]

def p_expression_vals_last_func(p):
    'VALS : LEFTPAREN FUNCTION RIGHTPAREN'
    p[0] = [p[2]]

def p_expression_text(p):
    'TEXTEXP : TEXTVAL'
    p[0] = ('text', p[1].replace("'", "").replace('"', ""))

def p_expression_url(p):
    'URLEXP : URLVAL'
    p[0] = ('url', p[1].replace("'", "").replace('"', ""))

def p_expression_number(p):
    'NUMEXP : NUMVAL'
    p[0] = ('number', int(p[1].replace("'", "").replace('"', "")))

##Parser for tab input (indentation).
# Implemented by Pucong Han on April 9, 2013
def p_expression_tab(p):
    'INDENTATION : TAB INDENTATION'
    p[0] = ("indented", p[2][1] + 1)
    pass

def p_expression_tab_empty(p):
    'INDENTATION : EMPTY'
    p[0] = ("empty", 0)
    pass

def p_empty(p):
    'EMPTY :'
    pass
    
parser = yacc.yacc()
