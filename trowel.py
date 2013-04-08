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
################

import sys
from Parser import parser
import typelist

def main(argv):
	program = []
	inputs = str(argv[1])
	try:
		f = open(inputs,"rb+").readlines()
	except:
		f = [inputs]
	for line in f:
		line = line.rstrip('\n')
		print "this is a line"
		print line
		output = parser.parse(line)
		typelist.printHash()
		
		if output[0] == "func":
			if output[1] == "printvals":
				list_to_print = "print \""
				for entry in output[2]:
					if entry[0] == "text" or entry[0] == "url":
						list_to_print = list_to_print + str(entry[1][1:-1]) + "\""
					else: #print number
						print "number!"
						list_to_print = list_to_print + str(entry[1]) + "\""
				program.append(list_to_print)
			elif output[1] == "printlist":
				printlist = "print "
				for entry in output[2]:
					if entry[0] is "text" or entry[0] is "url":
						printlist = printlist + str(entry[1] + "\n")
				program.append(printlist)
		
		if output[0] == "dec":
			printlist = ""
			output[2].reverse()
			for entry in output[2]:
				if entry[1][0] == "number":
					printlist = printlist + str(entry[0]) + " = 0"
				elif entry[1][0] == "url":
					printlist = printlist + str(entry[0]) + " = ''"
				elif entry[1][0] == "text":
					printlist = printlist + str(entry[0]) + ' = ""'
				else:
					printlist = printlist + str(entry[0]) + " = " + str(entry[1][1])
			program.append(printlist)
		
		if output[0] == "assign":
			if output[1] == "text" or output[1] == "url" or output[1] == "number":
				printlist = output[2] + " = " + output[3][0][1]
				program.append(printlist)
			elif output[1] == "textlist" or output[1] == "urllist" or output[1] == "numlist":
				templist = []
				for item in output[3]:
					if output[1] == "numlist":
						templist.append(int(item[1].replace("'", "").replace('"', "")))
					else:
						templist.append(str(item[1].replace("'", "").replace('"', "")))
				printlist = ""
				printlist = output[2] + " = " + str(templist)
				program.append(printlist)
	for entry in program:
		print entry
	print program
        
if __name__ == "__main__":
	main(sys.argv)
