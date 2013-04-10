#! /usr/bin/python

################
# PROGRAM:      Trowel
# DESCRIPTION:  The Trowel programming language is intended to aid in the web scraping that we all do on a daily basis,
#               but it is especially targeted to the needs and technical capacities of journalists. This program read and
#        		translate the abstract syntax tree to targeted programs
# 
# LICENSE:      ---OPTIONAL---
# REFERENCES:   Python Lex-Yacc Documentation (http://www.dabeaz.com/ply/)
# OUTPUT:       Targeted programs
# 
# AUTHOR(S):
#               Pucong Han (ph2369@columbia.edu)
#               Victoria Mo (vm2355@columbia.edu)
#               Hareesh Radhakrishnan (hr2318@columbia.edu)
#               David Tagatac (dtagatac@cs.columbia.edu)
#               Robert Walport (robertwalport@gmail.com)
# MODIFICATIONS:
#               Created and Modified by Pucong Han, Robert Walport and Victoria Mo on April 6, 2013
#				Modified by Pucong Han and Robert Walport on April 7, 2013
#				Modified by Pucong Han, Robert Walport, Victoria Mo and David Tagatac on April 8, 2013
################

import sys
from Parser import parser
import typelist

def printvals(i):
	item = []
	global program
	for val in i:
		item.append(operationChecker(val))
	list_to_print = "print \""
	for entry in item:
		if entry[0] == "text" or entry[0] == "url":
			list_to_print = list_to_print + str(entry[1])
		else: #print number
			list_to_print = list_to_print + str(entry[1])
	list_to_print = list_to_print + "\""
	program.append(list_to_print)
	
def printList(item):
	global program
	operationChecker(item)
	printlist = ""
	for entry in item:
		printlist = printlist + "print " + str(entry[1] + "\n")
	program.append(printlist[:-1])

#Recursive definitions of functions allowing for functions within functions
def operationChecker(item):
	printlist = ""
	if type(item) is list:
		item = item[0]

	if item == "emptyline":
		print "Empty Line Captured"
		program.append("\n")

	elif item[0] == "func":
		if item[1] == "printvals":
			printvals(item[2])
		elif item[1] == "printlist":
			printList(item[2])
		elif item[1] == "combine":
			return item[2]
		else:
			print "Not yet implemented/error"
	
	elif item[0] == "dec":
		item[2].reverse()
		for entry in item[2]:
			if entry[1][0] == "number":
				printlist = printlist + str(entry[0]) + " = 0"
			elif entry[1][0] == "url":
				printlist = printlist + str(entry[0]) + " = ''"
			elif entry[1][0] == "text":
				printlist = printlist + str(entry[0]) + ' = ""'
			else:
				printlist = printlist + str(entry[0]) + " = " + str(entry[1][1])
		program.append(printlist)
	
	elif item[0] == "assign":
		if item[1] == "number":
			printlist = item[2] + " = " + item[3][0][1]
			program.append(printlist)
		elif item[1] == "text":
			printlist = item[2] + ' = "' + item[3][0][1] + '"'
			program.append(printlist)
		elif item[1] == "url":
			printlist = item[2] + " = '" + item[3][0][1] + "'"
			program.append(printlist)
		elif item[1] == "textlist" or item[1] == "urllist" or item[1] == "numlist":
			templist = []
			for subitem in item[3]:
				if subitem[0] == "number":
					templist.append(int(subitem[1]))
				else:
					templist.append(str(subitem[1]))
			printlist = item[2] + " = " + str(templist)
			program.append(printlist)
		elif item[1] == "variable":
			printlist = item[2] + " = " + item[3]
			program.append(printlist)
		else:
			print "Unrecognized assignment tokens."
	else:
		return item

def main(argv):
	global program 
	program = []
	inputs = str(argv[1])
	try:
		f = open(inputs,"rb+").readlines()
	except:
		f = inputs.split(r'\n')
	for line in f:
		line = line.rstrip('\n')
		output = parser.parse(line)

		#Calling operation checker when output is not null (not empty line).
		operationChecker(output)

		# print output
	typelist.printTypeList()
	typelist.printValList()

		

	for entry in program:
		print entry
	return program
        
if __name__ == "__main__":
	main(sys.argv)
