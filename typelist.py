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
################

#Typelist is a hashtable. It is used for checking variable types.
typelist = {}
#Locallist is a list contains local variables.
locallist = []

##Function addNewType associates variable with variable type in the hashtable.
# Implemented by Pucong Han on April 6, 2013
def addNewType(variablename, typename):
	typelist[variablename] = typename

##Function addNewVariable add variable in parameter to the locallist.
# Implemented by Pucong Han on April 6, 2013
def addNewVariable(variablename):
	locallist.append(variablename)

##Function returnType returns the type of the passed variable.
# Implemented by Pucong Han on April 6, 2013
def returnType(variablename):
	return typelist[variablename]

##Function printHash prints the typelist (for testing purpose).
# Implemented by Pucong Han on April 6, 2013
def printHash():
	print "Type list"
	print typelist

##Function printLocal prints locallist (for testing purpose).
# Implemented by Pucong Han on April 6, 2013
def printLocal():
	print "Local list"
	print locallist