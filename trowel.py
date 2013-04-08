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

def printvals(item):
	global program
	operationChecker(item)
	list_to_print = "print \""
	for entry in item:
		if entry[0] == "text" or entry[0] == "url":
			list_to_print = list_to_print + str(entry[1][1:-1]) + "\""
		else: #print number
			print "number!"
			list_to_print = list_to_print + str(entry[1]) + "\""
	program.append(list_to_print)
	
def printList(item):
	global program
	operationChecker(item)
	printlist = ""
	for entry in item:
		if entry[0] is "text" or entry[0] is "url":
			printlist = printlist + "print" + str(entry[1] + "\n")
	program.append(printlist[:-2])

#Recursive definitions of functions allowing for functions within functions
def operationChecker(item):
	if item[0] == "func":
		if item[1] == "printvals":
			printvals(item[2])
		elif item[1] == "printlist":
			printList(item[2])
		else:
			print "Not yet implemented/error"
	
	elif item[0] == "dec":
		printlist = ""
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
		if item[1] == "text" or item[1] == "url" or item[1] == "number":
			printlist = item[2] + " = " + item[3][0][1]
			program.append(printlist)
		elif item[1] == "textlist" or item[1] == "urllist" or item[1] == "numlist":
			templist = []
			for item in item[3]:
				if item[1] == "numlist":
					templist.append(int(item[1].replace("'", "").replace('"', "")))
				else:
					templist.append(str(item[1].replace("'", "").replace('"', "")))
			printlist = ""
			printlist = item[2] + " = " + str(templist)
			program.append(printlist)
	else:
		return item

def main(argv):
	global program 
	program = []
	inputs = str(argv[1])
	try:
		f = open(inputs,"rb+").readlines()
	except:
		f = [inputs]
	for line in f:
		line = line.rstrip('\n')
		output = parser.parse(line)
		print output
		# typelist.printHash()
		operationChecker(output)
		

	for entry in program:
		print entry
	return program
        
if __name__ == "__main__":
	main(sys.argv)
