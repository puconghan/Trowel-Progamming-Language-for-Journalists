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
################

#Typelist is a hashtable storing variables and types.
typelist = {}
#Valuelist is a hashtable storing variables and values.
vallist = {}
#Variablelist is a list storing variables
variablelist = []

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

##Function printHash prints the typelist (for testing purpose).
# Implemented by Pucong Han on April 6, 2013.
def printTypeList():
	print ""
	print "-----Type list-----"
	print typelist
	print "-------------------"
	print ""

##Function printValList prints the vallist (for testing purpose).
# Implemented by Pucong Han on April 9, 2013.
def printValList():
	print ""
	print "-----Value list-----"
	print vallist
	print variablelist
	print "-------------------"
	print ""