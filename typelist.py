################
# PROGRAM:      Trowel Typelist
# DESCRIPTION:  The typelist.py manages a list of declared variables and types.
# 
# LICENSE:      ---OPTIONAL---
# REFERENCES:   Python Lex-Yacc Documentation (http://www.dabeaz.com/ply/)
# OUTPUT:       List of variables and types
# 
# AUTHOR(S):
#               Pucong Han (ph2369@columbia.edu)
# MODIFICATIONS:
#               Created by Pucong Han on April 6, 2013
#				Modified by Pucong Han on April 7, 2013
#				Modified by Pucong Han on April 8, 2013
#				Modified by Pucong Han on Aprial 9, 2013
#				Modified by Pucong on April 10, 2013.
################

#Typelist is a hashtable storing variables and types.
typelist = {}
#Valuelist is a hashtable storing variables and values.
vallist = {}
#Variablelist is a list storing variables
variablelist = []

indentationValue = []
indentationValue.append(0)

# #indenttypelist is a hashtable storing variables and types for indented declarations and assignments.
# indenttypelist = {}
# #indentvaluelist is a hashtable storing variables and values for indented declarations and assignments.
# indentvallist = {}

#Locallist is a list contains local variables.
locallist = []

##Function addNewType associates variable with variable type in the hashtable.
# Implemented by Pucong Han on April 6, 2013.
def addNewType(variablename, typename, indentlevel):
	typelist[(variablename, indentlevel)] = typename
	variablelist.append((variablename, indentlevel))

##Function addNewValue associates variable with variable type in the hashtable.
# Implemented by Pucong Han on April 8, 2013.
def addNewValue(variablename, value, indentlevel):
	vallist[(variablename, indentlevel)] = value

##Function addNewVariable add variable in parameter to the locallist.
# Implemented by Pucong Han on April 6, 2013.
def addNewVariable(variablename):
	locallist.append(variablename)

# ##Function addNewIndentType associates variable with variable type in the indenttypelist hashtable.
# # Implemented by Pucong Han on April 9, 2013.
# def addNewIndentType(variablename, typename, indentlevel):
# 	indenttypelist[(variablename, indentlevel)] = typename
# 	variablelist.append((variablename, indentlevel))

# ##Function addNewIndentValue associates variable with variable type in the indentvallist hashtable.
# # Implemented by Pucong Han on April 9, 2013.
# def addNewIndentValue(variablename, value, indentlevel):
# 	indentvallist[(variablename, indentlevel)] = value

##Function returnType returns the type of the passed variable.
# Implemented by Pucong Han on April 6, 2013.
# Updated by Pucong Han on April 7, 2013.
def returnType(variablename, indentlevel):
	if (variablename, indentlevel) in variablelist:
		return typelist[(variablename, indentlevel)]
	else:
		return "Not in typelist"

##Function returnType returns the type of the passed variable.
# Implemented by Pucong Han on April 8, 2013.
def returnValue(variablename, indentlevel):
	if (variablename, indentlevel) in variablelist:
		return vallist[(variablename, indentlevel)]
	else:
		return "Not in vallist"

##Function indentationCheck check for indentations and pop variables in local scope.
# Implemented by Pucong Han on April 10, 2013.
def indentationCheck(indentlevel):
	if indentlevel >= indentationValue[0]:
		indentationValue[0] = indentlevel
	else:
		templist = []
		while indentationValue[0] != indentlevel:
			for item in variablelist:
				if item[1] == indentationValue[0]:
					del typelist[(item[0], indentationValue[0])]
					templist.append(item)
			indentationValue[0] -= 1
		for removeditem in templist:
			if (removeditem[0], removeditem[1]) in vallist.keys():
				del vallist[(removeditem[0], removeditem[1])]
			variablelist.remove(removeditem)

def indentationDisplay():
	print indentationValue[0]
	print typelist
	print vallist
	print variablelist


##Function printHash prints the typelist (for testing purpose).
# Implemented by Pucong Han on April 6, 2013.
def printTypeList():
	print ""
	print "Note: Variables in local scope will be removed from these lists once found expression in unindented or decreased indented newline."
	print "Note: Global variables will remain in these lists"
	print ""
	print "-------Type list-------"
	print typelist
	print "-----Variable list-----"
	print variablelist
	print "-----------------------"
	print ""

##Function printValList prints the vallist (for testing purpose).
# Implemented by Pucong Han on April 9, 2013.
def printValList():
	print ""
	print "-------Value list-------"
	print vallist
	print "------------------------"
	print ""