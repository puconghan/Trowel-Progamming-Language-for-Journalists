###################################################################################################
# PROGRAM:      Trowel
# DESCRIPTION:  This trowelglobal.py program stores variables, error messages, default functions.
#				This program also has an error handler function.
# LICENSE:      PLY
# REFERENCES:   Python Lex-Yacc Documentation (http://www.dabeaz.com/ply/)
###################################################################################################

import sys

indentlevel = 0
indentback = 0
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
	'binop' : ['number'],
	'length' : ['number']
}

customfunctions = []

funclist = prebuiltfunctions

# Error handler function for the compiler.
def returnError(error_type, error_message, terminator):
	errorflag = True
	errorlist.append([linenumber, error_type, error_message])
	print error_type
	print error_message
	if terminator == True:
		printErrorMessages(error_type)
		sys.exit()
	# Set the error list threshold to three. More than three error, the compiler will terminate.
	if len(errorlist) >= 3:
		printErrorMessages(error_type)
		sys.exit()

# Error printing function for the compiler
def printErrorMessages(typeerror):
	if not errorlist:
		print "Targeted language does not have error messages"
	else:
		print "----------Error-Messages----------"
		if typeerror == "Run Time Error":
			for erroritem in errorlist:
				print "----------------------------------"
				print "Error Type  --> " + erroritem[1]
				print "Message     --> " + erroritem[2]
		else:
			for erroritem in errorlist:
				print "----------------------------------"
				print "Line Number --> " + str(erroritem[0])
				print "Error Type  --> " + erroritem[1]
				print "Message     --> " + erroritem[2]

# Type checking function for the compiler. This function will check for type errors.
def typeChecking(ast):
	if ast[0][0] == "indentlevel":
		indentationlevel = ast[0][1]
		if ast[1][0] == "declaration":
			if ast[1][1][0] == "datatype":
				vartype = ast[1][1][1]
				varname = ast[1][2][0][0]
				if varlist[indentationlevel].get(varname) != vartype:
					returnError("Type Error", "Variable" + varname + "in the abstract syntax tree type mismatch", False)
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
							returnError("Type Error", "Variable" + varname + "in the abstract syntax tree type mismatch", False)
	else:
		returnError("Syntax Error", "Indentation is missing in the syntax tree", False)