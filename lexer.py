################
# PROGRAM:      Trowel
# DESCRIPTION:  The Trowel programming language is intended to aid in the web scraping that we all do on a daily basis,
#               but it is especially targeted to the needs and technical capacities of journalists.
# 
# LICENSE:      ---OPTIONAL---
# REFERENCES:   additional used information goes here
# ALGORITHM:    Pseudocode describing the algorithm goes here
# OUTPUT:       Trowel automagickally creates: (any print statements, files created, etc.)
# RETURN:       Returns values go here
# 
# AUTHOR(S):
#               Pucong Han (ph2369@columbia.edu)
#               Victoria Mo (vm2355@columbia.edu)
#               Hareesh Radhakrishnan (hr2318@columbia.edu)
#               David Tagatac (dtagatac@cs.columbia.edu)
#               Robert Walport (robertwalport@gmail.com)
# MODIFICATIONS:
#               Created by Pucong Han on Mar 11, 2013
#               Modified by all team authors on April 1, 2013
#               Modified by all team authors on April 6, 2013
################

import lex

#This is the list of lexer tokens for Trowel
tokens = (
   #Comment (#)
   'COMMENTS',
   #Logical Operators (AND OR NOT)
   'AND',
   'OR',
   'NOT',
   #Arithmetic Operators (* / + -)
   'MULTIPLY',
   'DIVISION',
   'PLUS',
   'MINUS',
   'EQUAL',
   'NOTEQUAL',
   #Data Types (URL TEXT NUMBER URLLIST TEXTLIST NUMLIST)
   'URL',
   'TEXT',
   'NUMBER',
   'URLLIST',
   'TEXTLIST',
   'NUMLIST',
   #Functions (PRINT READ SAVE APPEND INSERT FINDURL FINDTEXT COMBINE)
   'PRINT',
   'READ',
   'SAVE',
   'APPEND',
   'INSERT',
   'FINDURL',
   'FINDTEXR',
   'COMBINE',
   'DEFINE',
   #Control Operators (IF ELSE FOR)
   'IF',
   'ELSE',
   'ELSEIF',
   'FOR',
   #Reserved Keywords (IS WITH INTO IN)
   'IS',
   'WITH',
   'INTO',
   'IN',
   #Reserved Deliminators (, ' " [ ])
   'COMMA',
   'SINGLECOLON',
   'DOUBLECOLON',
   'RIGHTSQUAREBRACKET',
   'LEFTSQUAREBRACKET',
   #Identifier captures everything else
   'IDENTIFIER',
)

#Arithmetic Operators (* / + - == =/=)
t_MULTIPLY = r'\*'
t_DIVISION = r'\/'
t_PLUS     = r'\+'
t_MINUS    = r'-'
t_EQUAL    = r'=='
t_NOTEQUAL = r'=/='

#Reserved Deliminators (, ' " [ ])
t_COMMA              = r','
t_SINGLECOLON        = r'"'
t_DOUBLECOLON        = r"'"
t_RIGHTSQUAREBRACKET = r'\]'
t_LEFTSQUAREBRACKET   = r'\['

#Comments (#)
def t_COMMENTS(t):
    r'\#.*'
    return t

#Logical Operators (AND OR NOT)
def t_AND(t):
    r'(?<=\s)((and) | (AND))(?=\s)'   
    return t

def t_OR(t):
    r'(?<=\s)((or) | (OR))(?=\s)'   
    return t

def t_NOT(t):
    r'(?<=\s)((not) | (NOT))(?=\s)'   
    return t

#Data Types (URL TEXT NUMBER URLLIST TEXTLIST NUMLIST)
def t_URL(t):
    r'((url) | (URL))(?=\s)'   
    return t

def t_TEXT(t):
    r'((text) | (TEXT))(?=\s)'   
    return t

def t_NUMBER(t):
    r'((number) | (NUMBER))(?=\s)'   
    return t

def t_URLLIST(t):
    r'((urllist) | (URLLIST) | (urlList))(?=\s)'   
    return t

def t_TEXTLIST(t):
    r'((textlist) | (TEXTLIST) | (textList))(?=\s)'   
    return t

def t_NUMLIST(t):
    r'((numlist) | (NUMLIST) | (numList))(?=\s)'   
    return t

#Functions (PRINT READ SAVE APPEND ADD FINDURL COMBINE DEFINE)
def t_PRINT(t):
    r'((print) | (PRINT))(?=\s)'   
    return t

def t_READ(t):
    r'((read) | (READ))(?=\s)'   
    return t

def t_SAVE(t):
    r'((save) | (SAVE))(?=\s)'   
    return t

def t_APPEND(t):
    r'((append) | (APPEND))(?=\s)'   
    return t

def t_INSERT(t):
    r'((insert) | (ADD))(?=\s)'   
    return t

def t_FINDURL(t):
    r'((findurl) | (FINDURL) | (findURL))(?=\s)'   
    return t

def t_COMBINE(t):
    r'((combine) | (COMBINE))(?=\s)'   
    return t

def t_DEFINE(t):
    r'((define) | (DEFINE))(?=\s)'   
    return t

#Control Operators (IF ELSE ELSEIF FOR)
def t_IF(t):
    r'((if) | (IF))(?=\s)'   
    return t

def t_ELSE(t):
    r'((else) | (ELSE))(?=\s)'   
    return t

def t_ELSEIF(t):
    r'((elseif) | (ELSEIF))(?=\s)'   
    return t

def t_FOR(t):
    r'((for) | (FOR))(?=\s)'   
    return t

#Reserved Keywords (IS WITH INTO IN)
def t_IS(t):
    r'(?<=\s)((is) | (IS))(?=\s)'
    return t

def t_WITH(t):
    r'(?<=\s)((with) | (WITH))(?=\s)'
    return t

def t_INTO(t):
    r'(?<=\s)((into) | (INTO))(?=\s)'
    return t

def t_IN(t):
    r'(?<=\s)((in) | (IN))(?=\s)'
    return t

#Identifier captures everything else

def t_IDENTIFIER(t):
    r'[a-zA-Z0-9_]+'
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

lex.lex()


import yacc

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
