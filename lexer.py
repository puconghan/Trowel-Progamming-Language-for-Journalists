import ply.yacc as yacc
import ply.lex as lex

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
   'LEFTSQAREBRACKET',
   #Identifier captures everything else
   'IDENTIFIER',
)

#Arithmetic Operators (* / + -)
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
t_LEFTSQAREBRACKET   = r'\['

#Comment (#)
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

#Functions (PRINT READ SAVE APPEND INSERT FINDURL FINDTEXT COMBINE)
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

#Control Operators (IF ELSE FOR)
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

# Build the lexer
lexer = lex.lex()

# Give the lexer some input
lexer.input("define _filter_result001 is findURL in stotries else elseif with term1 and term2 intothis into ' \" , [ ] * / + - == =/= #this")

while True:
    tok = lexer.token()
    if not tok: break
    print tok