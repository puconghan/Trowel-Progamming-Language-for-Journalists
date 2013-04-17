import sys

indentlevel = 0
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
	print error_type
	print error_message
	if terminator == True:
		sys.exit()