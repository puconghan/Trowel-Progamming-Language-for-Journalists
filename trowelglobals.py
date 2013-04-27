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
			print "Line Number --> " + erroritem[0]
			print "Error Type  --> " + erroritem[1]
			print "Message     --> " + erroritem[2]
		sys.exit()

def printErrorMessages():
	if not errorlist:
		print "Targeted language does not have error messages"
	else:
		print "----------Error-Messages----------"
		for item in errorlist:
			print "LINE NUMBER: " + str(item[0]) + " ERROR TYPE: " + item[1] + " ERROR MESSAGE: " + item[2]