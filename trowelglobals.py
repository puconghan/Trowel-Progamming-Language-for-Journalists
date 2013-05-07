###################################################################################################
# PROGRAM:      Trowel
# DESCRIPTION:  This trowelglobal.py program stores variables, error messages, default functions.
#				This program also has an error handler function.
# LICENSE:      PLY
# REFERENCES:   Python Lex-Yacc Documentation (http://www.dabeaz.com/ply/)
###################################################################################################

import sys

indentlevel = 0
linenumber = 0
errorlist = []
errorflag = False
varlist = [dict()]
funclist = dict()
reservedlist = dict()

#functionname : [returntype(s)]
prebuiltfunctions = {
	'print' : [None],
	'read' : ['urllist','textlist'],
	'save' : [None],
	'append' : [None],
	'insert' : [None],
	'findurl' : ['urllist'],
	'findtext' : ['textlist'],
	'combine' : ['url'],
}

funclist = prebuiltfunctions

def returnError(error_type, error_message, terminator):
	errorflag = True
	errorlist.append([linenumber, error_type, error_message])
	print error_type
	print error_message
	if terminator == True:
		for erroritem in errorlist:
			print "--------------------------------"
			print "Line Number --> " + str(erroritem[0])
			print "Error Type  --> " + erroritem[1]
			print "Message     --> " + erroritem[2]
		sys.exit()

def printErrorMessages():
	if not errorlist:
		print "Targeted language does not have error messages"
	else:
		print "----------Error-Messages----------"
		for erroritem in errorlist:
			print "----------------------------------"
			print "Line Number --> " + str(erroritem[0])
			print "Error Type  --> " + erroritem[1]
			print "Message     --> " + erroritem[2]

def typeChecking(ast):
	if ast[0][0] == "indentlevel":
		indentationlevel = ast[0][1]
	else:
		returnError("Type Checking", "Abstract Syntax Tree invalid. It does not contain indentation info", True)
	if ast[1][0] == "declaration":
		if ast[1][1][0] == "datatype":
			vartype = ast[1][1][1]
			varname = ast[1][2][0][0]
			if varlist[indentationlevel].get(varname) != vartype:
				returnError("Type Checking", "Abstract Syntax Tree variable" + varname + "type mismatch", False)
	if ast[1][0] == "assignment":
		if ast[1][1][0] == "variable":
			varname = ast[1][1][1]
			if ast[1][2][0] == "expression":
				if ast[1][2][1][0] == "functioncall":
					if ast[1][2][1][1][0] == "functionname":
						if ast[1][2][1][1][1] == "findtext":
							vartype = "textlist"
						if ast[1][2][1][1][1] == "findurl":
							vartype = "urllist"
				elif ast[1][2][1][0] == "variable":
					vartype = varlist[indentationlevel].get(ast[1][2][1][1])
				if varlist[indentationlevel].get(varname) != vartype:
					returnError("Type Checking", "Abstract Syntax Tree variable" + varname + "type mismatch", False)

# temp1 = [['indentlevel', 0], ['declaration', ['datatype', 'textlist'], [['flighttime']]]]
# temp2 = [['indentlevel', 0], ['declaration', ['datatype', 'url'], [['spacearticle', ['expression', ['value', ['url', 'http://www.bbc.co.uk/news/science-environment-22344398']]]]]]]
# temp3 = [['indentlevel', 0], ['assignment', ['variable', 'flighttime'], ['expression', ['functioncall', ['functionname', 'findtext'], 'arguments', [['expression', ['insertword', 'in']], ['expression', ['variable', 'spacearticle']], ['expression', ['insertword', 'with']], ['expression', ['value', ['text', 'time']]]]]]]]
# temp4 = [['indentlevel', 0], ['expression', ['functioncall', ['functionname', 'print'], 'arguments', [['expression', ['variable', 'flighttime']]]]]]
# temp5 = [['indentlevel', 0], ['assignment', ['variable', 'newlist'], ['expression', ['variable', 'flighttime']]]]
# typeChecking(temp5)