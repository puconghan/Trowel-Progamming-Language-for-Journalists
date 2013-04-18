import trowelglobals as tgl
from lexingrules import *

start = 'STATEMENT'

def p_statement(p):
	'''
	STATEMENT	: EXPRESSION
			| DECLARATION
			| ASSIGNMENT
	'''
	p[0] = [['indentlevel',tgl.indentlevel],p[1]]
		
def p_error(p):
	print "Syntax error at '%s'" % p.value

#-----------------------------------------------------

##Parsing expressions
def p_expression_1(p):
	'EXPRESSION	: IDENTIFIER'
	if tgl.funclist.get(p[1][1]) != None:
		p[0] = ['expression',['functioncall',p[1],'arguments',[]]]
	else:
		p[0] = ['expression',p[1]]
def p_expression_2(p):
	'''
	EXPRESSION	: VALUE
				| LIST
				| LEFTPAREN FUNCTION RIGHTPAREN
				| FUNCTION
	'''
	if len(p) == 2:
		p[0] = ['expression',p[1]]
	else:
		p[0] = ['expression',p[2]]

def p_identifier(p):
	'IDENTIFIER : UNKNOWNWORD'
	if tgl.funclist.get(p[1]) != None:
		p[0] = ['functionname',p[1]]
	elif tgl.varlist[tgl.indentlevel].get(p[1]) != None:
		p[0] = ['variable',p[1]]
	else:
		p[0] = ['insertword',p[1]]

#-----------------------------------------------------

##Parsing functions
def p_function(p):
	'FUNCTION : IDENTIFIER EXPRESSIONSET'
	p[0] = ['functioncall',p[1],'arguments',p[2]]

def p_expressionset(p):
	'''
	EXPRESSIONSET	: EXPRESSIONSET EXPRESSION
				| EXPRESSION
	'''
	if len(p) == 3:
		p[0] = p[1] + [p[2]]
	else:
		p[0] = [p[1]]

#-----------------------------------------------------

##Parsing constants and lists
def p_value(p):
	'''
	VALUE	: _URLVAL
			| _TEXTVAL
			| _NUMVAL
	'''
	p[0] = p[1]
	
def p_urlval(p):
	'_URLVAL : URLVAL'
	p[0] = ['value',['url',p[1][1:-1]]]
	
def p_textval(p):
	'_TEXTVAL : TEXTVAL'
	p[0] = ['value',['text',p[1][1:-1]]]
	
def p_numval(p):
	'_NUMVAL : NUMVAL'
	p[0] = ['value',['number',int(p[1])]]
	
def p_valueset(p):
	'''
	LISTSET	: EXPRESSION COMMA LISTSET
			| EXPRESSION
	'''
	#Add expression here
	if len(p) == 2:
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[3]

def p_valuelist(p):
	'LIST : LEFTSQUAREBRACKET LISTSET RIGHTSQUAREBRACKET'
	list = []
	for item in p[2]:
		list = list + [item[1]]
	p[0] = ['list',list]

#-----------------------------------------------------

##Parsing declarations	
def p_declaration(p):
	'DECLARATION : DATATYPE DECLARATIONSET'
	p[0] = ['declaration',p[1],p[2]]
	for varobj in p[2]:
		if (tgl.reservedlist.get(varobj[0]) == None) and (tgl.funclist.get(varobj[0]) == None) and (tgl.varlist[tgl.indentlevel].get(varobj[0]) == None):
			tgl.varlist[tgl.indentlevel][varobj[0]] = p[1][1]
	
def p_datatype(p):
	'''
	DATATYPE	: URL
			| TEXT
			| NUMBER
			| URLLIST
			| TEXTLIST
			| NUMLIST
	'''
	p[0] = ['datatype',p[1]]
	
def p_declarationset(p):
	'''
	DECLARATIONSET	: DECLAREDVAR COMMA DECLARATIONSET
				| DECLAREDVAR
	'''
	if len(p) == 2:
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[3]
	
def p_declarationassign(p):
	'''
	DECLAREDVAR	: UNKNOWNWORD IS EXPRESSION
				| UNKNOWNWORD
	'''
	if (tgl.funclist.get(p[1]) != None) or (tgl.varlist[tgl.indentlevel].get(p[1]) != None):
		#Error. Variable already defined.		
		pass
	if len(p) == 2:
		p[0] = [p[1]]
	else:
		p[0] = [p[1],p[3]]

#-----------------------------------------------------

##Parsing assignments
def p_assignment(p):
	'ASSIGNMENT : IDENTIFIER IS EXPRESSION'
	p[0] = ['assignment', p[1], p[3]]

#-----------------------------------------------------

##Empty handle
def p_empty(p):
	'EMPTY :'
	pass