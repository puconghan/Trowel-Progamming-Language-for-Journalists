import ply.yacc as yacc
import ply.lex as lex

tokens = (
   'AND',
   'OR',
   'NOT',
   'WITH',
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
t_MINUS   = r'-'

def t_AND(t):
    r'(and) | (AND)'   
    return t

def t_OR(t):
    r'(or) | (OR)'   
    return t

def t_NOT(t):
    r'(not) | (NOT)'   
    return t

def t_WITH(t):
    r'(with) | (WITH)'
    return t

def t_LEFTSQAREBRACKET(t):
    r'\['
    return t

def t_RIGHTSQUAREBRACKET(t):
    r'\]'
    return t

def t_URL(t):
    r'(url) | (URL)'   
    return t

def t_TEXT(t):
    r'(text) | (TEXT)'   
    return t

def t_NUMBER(t):
    r'(number) | (NUMBER)'   
    return t

def t_URLLIST(t):
    r'(urllist) | (URLLIST) | (urlList)'   
    return t

def t_TEXTLIST(t):
    r'(textlist) | (TEXTLIST) | (textList)'   
    return t

def t_NUMLIST(t):
    r'(numlist) | (NUMLIST) | (numList)'   
    return t

def t_PRINT(t):
    r'(print) | (PRINT)'   
    return t

def t_READ(t):
    r'(read) | (READ)'   
    return t

def t_SAVE(t):
    r'(save) | (SAVE)'   
    return t

def t_APPEND(t):
    r'(append) | (APPEND)'   
    return t

def t_ADD(t):
    r'(add) | (ADD)'   
    return t

def t_FINDURL(t):
    r'(findurl) | (FINDURL) | (findURL)'   
    return t

def t_COMBINE(t):
    r'(combine) | (COMBINE)'   
    return t

def t_IF(t):
    r'(if) | (IF)'   
    return t

def t_ELSE(t):
    r'(else) | (ELSE)'   
    return t

def t_FOR(t):
    r'(for) | (FOR)'   
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
lexer.input("filterresult is findURL in stotries with term1 and term2")

while True:
    tok = lexer.token()
    if not tok: break
    print tok