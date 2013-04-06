################
# PROGRAM:      Typelist
# DESCRIPTION:  The typelist.py manages a list of declared variables and types.
# 
# LICENSE:      ---OPTIONAL---
# REFERENCES:   Python Lex-Yacc Documentation (http://www.dabeaz.com/ply/)
# OUTPUT:       List of variables and types
# 
# AUTHOR(S):
#               Pucong Han (ph2369@columbia.edu)
#               Victoria Mo (vm2355@columbia.edu)
#               Hareesh Radhakrishnan (hr2318@columbia.edu)
#               David Tagatac (dtagatac@cs.columbia.edu)
#               Robert Walport (robertwalport@gmail.com)
# MODIFICATIONS:
#               Created by Pucong Han on April 6, 2013
################

#Typelist is a hashtable. It is used for checking variable types
typelist = {}
#Locallist is a list contains local variables. It is used for tracking declared variables.
locallist = []

# Function addNewType associates variable with variable type using the hashtable.
def addNewType(variablename, typename):
	typelist[variablename] = typename
	locallist.append([typename, variablename])
	print "added"

# Function cleanLocalList resets locallist.
def cleanLocalList():
	locallist = []

# Function printHash prints typelist.
def printHash():
	print "Type list"
	print typelist

# Function printLocal prints locallist.
def printLocal():
	print "Local list"
	print locallist