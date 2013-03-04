import ply.yacc as yacc
import ply.lex as lex

tokens = (
   'AND',
   'OR',
   'NOT',
   'RIGHTSQUAREBRACKET',
   'LEFTSQAREBRACKET',
   'PLUS',
   'MINUS',
   'URL',
   'TEXT',
   'NUMBER',
   'URLLIST',
   'TEXTLIST',
   'NUMLIST',
   'PRINT',
   'READ',
   'SAVE',
   'APPEND',
   'ADD',
   'FINDURL',
   'FINDTEXR',
   'COMBINE',
   'IF',
   'ELSE',
   'FOR',
)

t_PLUS    = r'\+'
t_MINUS   = r'\-'

def t_AND(t):
    r'and'   
    return t

def t_OR(t):
    r'or'   
    return t

def t_NOT(t):
    r'not'   
    return t

def t_LEFTSQAREBRACKET(t):
    r'\['
    return t

def t_RIGHTSQUAREBRACKET(t):
    r'\]'
    return t

def t_URL(t):
    r'url'   
    return t

def t_TEXT(t):
    r'text'   
    return t

def t_NUMBER(t):
    r'number'   
    return t

def t_URLLIST(t):
    r'urllist'   
    return t

def t_TEXTLIST(t):
    r'textlist'   
    return t

def t_NUMLIST(t):
    r'numlist'   
    return t

def t_PRINT(t):
    r'print'   
    return t

def t_READ(t):
    r'read'   
    return t

def t_SAVE(t):
    r'save'   
    return t

def t_APPEND(t):
    r'append'   
    return t

def t_ADD(t):
    r'add'   
    return t

def t_FINDURL(t):
    r'findurl'   
    return t

def t_COMBINE(t):
    r'combine'   
    return t

def t_IF(t):
    r'if'   
    return t

def t_ELSE(t):
    r'else'   
    return t

def t_FOR(t):
    r'for'   
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
lexer.input("add if for append")

while True:
    tok = lexer.token()
    if not tok: break
    print tok