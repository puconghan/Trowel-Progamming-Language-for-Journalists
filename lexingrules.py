###################################################################################################
# PROGRAM:      Trowel
# DESCRIPTION:  This lexingrule.py program is the lexer of Trowel used to break inputs into tokens.
# LICENSE:      PLY
# REFERENCES:   Python Lex-Yacc Documentation (http://www.dabeaz.com/ply/)
# OUTPUT:       Tokens
###################################################################################################

import trowelglobals as tgl

tokens = [
	#Tab (TAB)
	'TAB',
	#Comment (#)
	'COMMENT',
	#Logical Operators (AND OR NOT).
	'AND',
	'OR',
	'NOT',
	#Relational Operators
	'GREATER',
	'LESS',
	'EQUAL',
	'NOTEQUAL',
	#Arithmetic Operators (* / + -).
	'MULTIPLY',
	'DIVISION',
	'PLUS',
	'MINUS',
	#Data Types (URL TEXT NUMBER URLLIST TEXTLIST NUMLIST).
	'URL',
	'TEXT',
	'NUMBER',
	'URLLIST',
	'TEXTLIST',
	'NUMLIST',
	#Control Operators (IF ELSE FOR).
	'IF',
	'ELSE',
	'ELSEIF',
	'FOR',
	#Assignment Operator (IS).
	'IS',
	#Reserved Delimiters (, ' " [ ] ( )).
	'COMMA',
	'SINGLECOLON',
	'DOUBLECOLON',
	'RIGHTSQUAREBRACKET',
	'LEFTSQUAREBRACKET',
	'LEFTPAREN',
	'RIGHTPAREN',
	'COLON',
	#Constants
	'NUMVAL',
	'TEXTVAL',
	'URLVAL',
	#Custom Function
	'DEFINE',
	#Unknown word captures everything else.
	'UNKNOWNWORD',

]

##Custom function
def t_DEFINE(t):
	r'(define)'
	return t

##Tab (\t)
t_TAB = r'\t'

##Comment (#).
t_COMMENT = r'\#.*'
    
##Logical Operators (AND OR NOT).
def t_AND(t):
	r'(and)'
	return t

def t_OR(t):
	r'(or)'
	return t

def t_NOT(t):
	r'(not)'
	return t

##Relational Operators
t_GREATER = r'>'
t_LESS = r'<'
t_EQUAL    = r'=='
t_NOTEQUAL = r'=/='

##Arithmetic Operators (* / + - == =/=).
t_MULTIPLY = r'\*'
t_DIVISION = r'\/'
t_PLUS     = r'\+'
t_MINUS    = r'-'

##Data Types (URL TEXT NUMBER URLLIST TEXTLIST NUMLIST).
def t_URLLIST(t):
	r'(urllist)'
	return t

def t_TEXTLIST(t):
	r'(textlist)'
	return t

def t_URL(t):
	r'(url)'
	return t

def t_TEXT(t):
	r'(text)'
	return t

def t_NUMBER(t):
	r'(number)'
	return t

def t_NUMLIST(t):
	r'(numlist)'
	return t

#Control Operators (IF ELSE FOR).
def t_IF(t):
	r'(if)'
	return t

def t_ELSE(t):
	r'(else)'
	return t

def t_ELSEIF(t):
	r'(elseif)'
	return t

def t_FOR(t):
	r'(for)'
	return t

##Assignment Operator (IS).
def t_IS(t):
	r'(is)'
	return t

##Reserved Deliminators (, ' " [ ]).
t_COMMA              = r','
t_SINGLECOLON        = r"'"
t_DOUBLECOLON        = r'"'
t_LEFTSQUAREBRACKET   = r'\['
t_RIGHTSQUAREBRACKET = r'\]'
t_LEFTPAREN   = r'\('
t_RIGHTPAREN = r'\)'
t_COLON = r':'

##Constants
def t_TEXTVAL(t):
  r'"[^"]+"'
  return t

def t_URLVAL(t):
  r'\'[^\']+\''
  return t

def t_NUMVAL(t):
  r'[0-9]+'
  return t

##Unknown Word
t_UNKNOWNWORD = r'[a-z_][a-z0-9_]*'

##Ignored characters
t_ignore  = ' '

##Error handling for illegal characters.
def t_error(t):
    tgl.returnError("Lexing Error", "Encounter illegal character '%s'" % t.value[0], False)
    t.lexer.skip(1)
