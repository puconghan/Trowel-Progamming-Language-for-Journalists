#!/usr/bin/python
###################################################################################################
# PROGRAM:      Trowel
# DESCRIPTION:  This epicparser.py program is the main function for trowel.
#				This program handles the process of program language translation.
# LICENSE:      PLY
# REFERENCES:   Python Lex-Yacc Documentation (http://www.dabeaz.com/ply/)
# OUTPUT:		Targeted Python Language
###################################################################################################

import trowelglobals as tgl
#import trowelfunctions as tfl
import ply.lex as lex, ply.yacc as yacc
import lexingrules, parsingrules
from copy import copy
import sys

def main():
	inputfile = file(sys.argv[1],'r')
	tokenfile = file('tokens.twl','w')
	aslfile = file('asl.twl','w')
	pythonfile = file(sys.argv[1][:-3]+'py','w')
	
	parsebox = parsewrapper()
	pythonbox = pythonwrapper()
	
	pythonfile.write(pythonbox.headblock())

	inputline = parsebox.getline(inputfile)
	while inputline:
		tokenline = parsebox.gettokens(inputline)
		aslline = parsebox.getabstractlist(inputline)
		#Type checking function from the trowlglobal.py
		tgl.typeChecking(aslline)
		pythonblock = pythonbox.buildpython(aslline)

		tokenfile.write(str(tokenline) + '\n')
		aslfile.write(str(aslline) + '\n')
		pythonfile.write(pythonblock)
		inputline = parsebox.getline(inputfile)

	inputfile.close()
	tokenfile.close()
	aslfile.close()
	pythonfile.close()
	print "--------------------------Trowel Compiler--------------------------"
	print "--Trowel source code has been compiled to Python targeted program--"
	print "-------------------------------------------------------------------"

# Preprocessor of Trowel
class parsewrapper:
	def __init__(self):
		self.lexer = lex.lex(module = lexingrules)
		self.parser = yacc.yacc(module = parsingrules)
		self.lastindentlevel = 0
	
	def gettokens(self, inputline):
		self.lexer.input(inputline)
		tokenlist = []
		for token in self.lexer:
			tokenlist = tokenlist + [[token.type,token.value,token.lineno]]
		return tokenlist
	
	def getabstractlist(self, inputline):
		return self.parser.parse(input = inputline, lexer = self.lexer)

	def getline(self, inputfile):
		line = inputfile.readline()
		tgl.linenumber = tgl.linenumber + 1
		while line == "\n":
			line = inputfile.readline()
		if line:
			line = line.rstrip()
			line = line.lower()
			line = self.filterindentation(line)
		return line
		
	def filterindentation(self, inputline):
		indentlevel = 0
		while inputline[0] == '\t':
			inputline = inputline[1:]
			indentlevel = indentlevel + 1
		if len(inputline) > 6 and inputline[0:6] == 'define':
			indentlevel = indentlevel + 1
		tgl.indentlevel = indentlevel
		if indentlevel < self.lastindentlevel:
			tgl.varlist = tgl.varlist[0:indentlevel+1]
		elif indentlevel == self.lastindentlevel + 1:
			tgl.varlist.append(copy(tgl.varlist[self.lastindentlevel]))
		elif indentlevel > self.lastindentlevel + 1:
			#Throw error. Cannot indent forward by more than one level at at time.
			pass
		self.lastindentlevel = indentlevel
		return inputline

# Code Generator for Trowel
class pythonwrapper:
	def __init__(self):
		self.tmpvarcount = 0
	
	# Function adds headers and declarations to the target program.
	def headblock(self):
		block = '#!/usr/bin/python\nimport trowelfunctions as tfl\n'
		return block

	# Function checks for abstract syntax tree structures.
	def checkaslintegrity(self, inputline):
		if inputline[0][0] == "indentlevel":
			if inputline[1][0] == "declaration":
				if (inputline[1][1][0] == "datatype") and (inputline[1][1][1] in ["number", "text", "url", "numlist", "textlist", "urllist"]):
					pass
				else:
					tgl.returnError("Syntax Error", "Declaration syntax mismatch", True)
			elif inputline[1][0] == "assignment":
				if inputline[1][1][0] == "variable":
					pass
				else:
					tgl.returnError("Syntax Error", "Assignment syntax mismatch", True)
			elif inputline[1][0] == "expression":
				if inputline[1][1][0] == "functioncall":
					if inputline[1][1][1][0] == "functionname":
						pass
					else:
						tgl.returnError("Syntax Error", "Expression function name mismatch", True)
				else:
					tgl.returnError("Syntax Error", "Expression function call mismatch", True)
			else:
				tgl.returnError("Syntax Error", "Missing syntax header", True)
			pass
		else:
			tgl.returnError("Syntax Error", "Missing indentation information", True)
	
	# Function generates target python program.
	def buildpython(self, listobject):
		self.checkaslintegrity(listobject)
		indentlevel = listobject[0][1]
		prodobject = listobject[1]
		production = listobject[1][0]
		self.tmpvarcount = 0
		
		block = ''
		tab = ''
		for i in range(indentlevel):
			tab = tab + '\t'
		
		if production == 'declaration':
			block = block + self.prod_declaration(prodobject)
		elif production == 'assignment':
			block = block + self.prod_assignment(prodobject)
		elif production == 'expression':
			[blockval,expval] = self.prod_expression(prodobject)
			block = block + blockval
			
		block = block.strip()
		blocklines = block.split('\n')
		
		block = ''
		for line in blocklines:
			if line != '':
				block = block + tab + line + '\n'
		
		return '\n' + block
	
	# Function translates declaration from the abstract syntax tree.
	def prod_declaration(self, listobject):
		block = ''
		datatype = listobject[1][1]
		for varobject in listobject[2]:
			block = block + varobject[0] + ' = '
			if datatype == 'number':
				block = block + '0'
			elif datatype == 'text' or 'url':
				block = block + '""'
			else:
				block = block + '[]'
			block = block + '\n'
			if  len(varobject) == 2:
				assignobject = ['assignment', ['variable', varobject[0]], varobject[1]]
				block = block + self.prod_assignment(assignobject)
		return block

	# Function translate assignments from the abstract syntax tree.
	def prod_assignment(self, listobject):
		varname = listobject[1][1]
		vartype = tgl.varlist[tgl.indentlevel][varname]
		[block,expval] = self.prod_expression(listobject[2])
		block = block + varname + ' = ' + expval + '\n'
		return block

	# Function translates expressions from the abstract syntax tree.
	def prod_expression(self, listobject):
		exptype  = listobject[1][0]
		block = ''
		expval = ''
		if exptype == 'functioncall':
			[blockval,expval] = self.prod_functioncall(listobject[1])
			block  = block + blockval + expval + '\n'
		elif exptype == 'list':
			tmplist = []
			for item in listobject[1][1]:
				[blockval,expval] = self.prod_expression(item)
				block = block + blockval
				block = block + 'tmp' + str(self.tmpvarcount) + ' = ' + expval + '\n'
				tmplist = tmplist + ['tmp' + str(self.tmpvarcount)]
				self.tmpvarcount = self.tmpvarcount + 1
			expval = '[' + ','.join(tmplist) + ']'
		elif exptype == 'variable':
			expval = str(listobject[1][1])
		elif exptype == 'value':
			expval = str(listobject[1][1][1])
			if not expval.isdigit():
				expval = '\'' + expval + '\''
		elif exptype == 'insertword':
			expval = '\'' + str(listobject[1][1]) + '\''
		return [block,expval]
	
	# Function translates function calls from the abstract syntax tree.
	def prod_functioncall(self, listobject):
		block = ''
		functionname = listobject[1][1]
		argumentlist = listobject[3]	
		tmplist = []
		for item in argumentlist:
			[blockval,expval] = self.prod_expression(item)
			block = block + blockval
			block = block + 'tmp' + str(self.tmpvarcount) + ' = ' + expval + '\n'
			tmplist = tmplist + ['tmp' + str(self.tmpvarcount)]
			self.tmpvarcount = self.tmpvarcount + 1
			
		pythonarglist = '([' + ','.join(tmplist) + '])'
		expval = 'tfl.r_' + functionname + pythonarglist
		return [block,expval]
		
if __name__ == '__main__':
	main()
