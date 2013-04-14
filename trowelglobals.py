################
# PROGRAM: Trowel Variable Lists
# DESCRIPTION: The trowelglobals.py manages a list of declared variables and types.
#
# LICENSE: ---OPTIONAL---
# REFERENCES: Python Lex-Yacc Documentation (http://www.dabeaz.com/ply/)
# OUTPUT: List of variables and types
#
# AUTHOR(S):
# Pucong Han (ph2369@columbia.edu)
# Victoria Mo (vm2355@columbia.edu)
# Hareesh Radhakrishnan (hr2318@columbia.edu)
# David Tagatac (dtagatac@cs.columbia.edu)
# Robert Walport (robertwalport@gmail.com)
# 
# MODIFICATIONS:
# Created on April 6, 2013
# Modified by Pucong Han on April 7, 2013
# Modified by Pucong Han on April 8, 2013
# Modified by Pucong Han on Aprial 9, 2013
# Modified by Pucong on April 10, 2013.
# Modified by Hareesh Radhakrishnan on April 13, 2013
# Modified by Pucong Han on April 14, 2013
################

#Indentlevel is a global variable keeps track of indented levels.
indentlevel = 0
#Valuelist is a hashtable storing variables and values.
varlist = dict()
#Typelist is a hashtable storing variables and types.
typelist = dict()
#Function list is a hashtable storing functions.
funclist = dict()
#Variablelist is a list storing variables
# variablelist = []

reservedlist = dict()

#functionname : [returntype(s)]
prebuiltfunctions = {
	'print' : ['number'],
	'combine' : ['url'],
	'length' : ['number'],
	'insert' : ['urllist','textlist'],
	'read' : ['urllist','textlist'],
	'save' : [None],
	'append' : [None],
	'findurl' : ['urllist'],
	'findtext' : ['textlist']
}

funclist = prebuiltfunctions

##Function indentationCheck check for indentations and pop variables in local scope.
# Implemented by Pucong Han on April 10, 2013.
# def indentationCheck(indentation):
# 	global indentlevel
# 	if indentation >= indentlevel:
# 		indentlevel = indentation
# 	else:
# 		templist = []
# 		while indentlevel != indentation:
# 			print variablelist
# 			for item in variablelist:
# 				if item[0] == indentlevel:
# 					del typelist[(indentlevel, item[1])]
# 					templist.append(item)
# 			indentlevel -= 1
# 		for removeditem in templist:
# 			if (removeditem[0], removeditem[1]) in varlist.keys():
# 				del varlist[(removeditem[0], removeditem[1])]
# 				variablelist.remove(removeditem)