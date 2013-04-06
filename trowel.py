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

def main(argv):
	inputs = str(argv[1])
	output = parser.parse(inputs)
	output.printrec()

if __name__ == "__main__":
	main(sys.argv)