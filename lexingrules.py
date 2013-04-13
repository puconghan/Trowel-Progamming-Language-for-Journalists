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
	#Arithmetic Operators (* / + -).
	'MULTIPLY',
	'DIVISION',
	'PLUS',
	'MINUS',
	'EQUAL',
	'NOTEQUAL',
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
	#Constants
	'NUMVAL',
	'TEXTVAL',
	'URLVAL',
	#Unknown word captures everything else.
	'UNKNOWNWORD',
]

##Tab (\t)
t_TAB = r'\t'

##Comment (#).
t_COMMENT = r'\#.*'
    
##Logical Operators (AND OR NOT).
t_AND = r'and' 
t_OR = r'or'
t_NOT = r'not'

##Arithmetic Operators (* / + - == =/=).
t_MULTIPLY = r'\*'
t_DIVISION = r'\/'
t_PLUS     = r'\+'
t_MINUS    = r'-'
t_EQUAL    = r'=='
t_NOTEQUAL = r'=/='

##Data Types (URL TEXT NUMBER URLLIST TEXTLIST NUMLIST).
t_URL = r'(url)|(zzzzzzzzzzzzzzzzzzzzzzz)'
t_TEXT = r'(text)|(zzzzzzzzzzzzzzzzzzzzzzz)'
t_NUMBER = r'(number)|(zzzzzzzzzzzzzzzzzzzzzzz)'
t_URLLIST = r'(urllist)|(zzzzzzzzzzzzzzzzzzzzzzz)'   
t_TEXTLIST = r'(textlist)|(zzzzzzzzzzzzzzzzzzzzzzz)'
t_NUMLIST = r'(numlist)|(zzzzzzzzzzzzzzzzzzzzzzz)'

#Control Operators (IF ELSE FOR).
t_IF = r'(if)'
t_ELSE = r'(else)'
t_ELSEIF = r'(elseif)'
t_FOR = r'(for)'

##Assignment Operator (IS).
t_IS = r'(is)|(zzzzzzzzzzzzzzzzzzzzzzz)'

##Reserved Deliminators (, ' " [ ]).
t_COMMA              = r','
t_SINGLECOLON        = r"'"
t_DOUBLECOLON        = r'"'
t_LEFTSQUAREBRACKET   = r'\['
t_RIGHTSQUAREBRACKET = r'\]'
t_LEFTPAREN   = r'\('
t_RIGHTPAREN = r'\)'

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

##Error handling.
def t_error(t):
    print "Lexer illegal character '%s'" % t.value[0]
    t.lexer.skip(1)