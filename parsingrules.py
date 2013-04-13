import trowelglobals as tgl
from lexingrules import *

start = 'STATEMENT'

def p_statement(p):
	'''
	STATEMENT : ROOTEXPRESSION
	'''
	p[0] = p[2]
		
def p_error(p):
	print "Syntax error at '%s'" % p.value

#-----------------------------------------------------

##Parsing expressions
def p_rootexpression(p):
	'''
	ROOTEXPRESSION	: EXPRESSION
				| FUNCTION
				| DECLARATION
				| ASSIGNMENT
	'''
	if p[1][0] == 'functioncall':
		p[1] = ['expression',p[1]]
	p[0] = p[1]

def p_expression_1(p):
	'EXPRESSION	: IDENTIFIER'
	if tgl.funclist.get(p[1][1]) != None:
		p[0] = ['expression',['functioncall',p[1],'arguments',[]]]
	else:
		p[0] = ['expression',p[1]]
def p_expression_2(p):
	'''
	EXPRESSION	: VALUE
				| LEFTPAREN FUNCTION RIGHTPAREN
	'''
	if len(p) == 2:
		p[0] = ['expression',p[1]]
	else:
		p[0] = ['expression',p[2]]

def p_identifier(p):
	'IDENTIFIER : UNKNOWNWORD'
	if tgl.funclist.get(p[1]) != None:
		p[0] = ['functionname',p[1]]
	elif tgl.varlist[tgl.intentlevel].get(p[1]) != None:
		p[0] = ['variable',p[1]]
	else:
		p[0] = ['error','variable ' + p[1] + ' not found']

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

##Parsing constants	
def p_value(p):
	'''
	VALUE	: _URLVAL
			| _TEXTVAL
			| _NUMVAL
			| VALUELIST
	'''
	p[0] = p[1]
	
def p_urlval(p):
	'_URLVAL : URLVAL'
	p[0] = ['url',p[1][1:-1]]
	
def p_textval(p):
	'_TEXTVAL : TEXTVAL'
	p[0] = ['text',p[1][1:-1]]
	
def p_numval(p):
	'_NUMVAL : NUMVAL'
	p[0] = ['number',int(p[1])]
	
def p_valueset(p):
	'''
	VALUESET	: VALUE COMMA VALUESET
			| VALUE
	'''
	if len(p) == 2:
		p[0] = [p[1]]
	else:
		if p[1][0] == p[3][0][0]:
			p[0] = [p[1]] + p[3]
		else:
			p[0] = ['error','all values in a list must have the same type']

def p_valuelist(p):
	'VALUELIST : LEFTSQUAREBRACKET VALUESET RIGHTSQUAREBRACKET'
	type = p[2][0][0]
	if type == 'url':
		listtype = 'urllist'
	elif type == 'text':
		listtype = 'textlist'
	else:
		listtype = 'numlist'
	list = []
	for item in p[2]:
		list = list + [item[1]]
	p[0] = [listtype,list]

#-----------------------------------------------------

##Parsing declarations	
def p_declaration(p):
	'DECLARATION : DATATYPE DECLARATIONSET'
	p[0] = ['declaration',p[1],p[2]]
	for varobj in p[2]:
		if (tgl.reservedlist.get(varobj[0]) == None) and (tgl.funclist.get(varobj[0]) == None) and (tgl.varlist[tgl.intentlevel].get(varobj[0]) == None):
			tgl.varlist[tgl.intentlevel][varobj[0]] = p[1][1]
	
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
	DECLAREDVAR	: UNKNOWNWORD IS ROOTEXPRESSION
				| UNKNOWNWORD
	'''
	if len(p) == 2:
		p[0] = [p[1]]
	else:
		p[0] = [p[1],p[3]]

#-----------------------------------------------------

##Parsing assignments
def p_assignment(p):
	'ASSIGNMENT : IDENTIFIER IS ROOTEXPRESSION'
	p[0] = ['assignment', p[1], p[3]]

#-----------------------------------------------------

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

##Empty handle
def p_empty(p):
	'EMPTY :'
	pass