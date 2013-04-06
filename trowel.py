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
#               Created by Pucong Han and Robert Walport on April 6, 2013
################
import sys
from parser import parser
import typelist

def main(argv):
	program = []
	inputs = str(argv[1])
	output = parser.parse(inputs)
	print output
	# typelist.printHash()
	# typelist.printLocal()
	
	if output[0] == "func":
		if output[1] == "printvals":
			printlist = "print \""
			for entry in output[2]:
				if entry[0] == "text" or entry[0] == "url":
					printlist = printlist + (str(entry[1][1:-1]))
				else:
					printlist = printlist + (str(entry[1])) + "\""
			program.append(printlist)
		elif output[1] == "printlist":
			printlist = "print \""
			for entry in output[2]:
				if entry[0] is "text" or entry[0] is "url":
					printlist = printlist + str(entry[1][1] + "\n")
			printlist = printlist + "\""
			program.append(printlist)

	if output[0] == "dec":
		if output[1] == "urllist":
			printlist = ""
			output[2].reverse()
			for entry in output[2]:
				printlist = printlist + str(entry[0]) + "=" + str(entry[1][1]) + "\n"
			program.append(printlist)
	print program[0]
        
if __name__ == "__main__":
	main(sys.argv)
