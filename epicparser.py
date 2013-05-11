#!/usr/bin/python

import sys, os
from copy import copy
import ply.lex as lex, ply.yacc as yacc
import lexingrules, parsingrules, trowelglobals as tgl

def main():
	if len(sys.argv) != 2 or sys.argv[1][-4:] != '.twl':
		sys.exit('The input argument provided is not a .twl file')
	infilename = sys.argv[1]
	outfilename = sys.argv[1][:-4]+'.py'
	
	inputfile = file(infilename,'r')
	tokenfile = file('tokens.twl','w')
	aslfile = file('asl.twl','w')
	pythonfile = file(outfilename,'w')
	
	parsebox = parsewrapper()
	pythonbox = pythonwrapper()
	pythonfile.write(pythonbox.headblock())

	inputline = parsebox.getline(inputfile)
	while inputline:
		tokenline = parsebox.gettokens(inputline)
		aslline = parsebox.getabstractlist(inputline)

		aslfile.write(str(aslline) + '\n')
		tokenfile.write(str(tokenline) + '\n')		

		if aslline:
			tgl.typeChecking(aslline)

			pythonblock = pythonbox.buildpython(aslline)
			pythonfile.write(pythonblock)
			
		inputline = parsebox.getline(inputfile)

	inputfile.close()
	tokenfile.close()
	aslfile.close()
	pythonfile.close()




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
		tgl.indentback = 0
		while inputline[0] == '\t':
			inputline = inputline[1:]
			indentlevel = indentlevel + 1
		if indentlevel < self.lastindentlevel:
			tgl.varlist = tgl.varlist[0:indentlevel+1]
			
		if len(inputline) > 6 and (inputline[0:6] == 'define' or inputline[0:3] == 'for' or inputline[0:2] == 'if'):
			indentlevel = indentlevel + 1
			tgl.indentback = -1
		tgl.indentlevel = indentlevel

		if indentlevel == self.lastindentlevel + 1:
			tgl.varlist.append(copy(tgl.varlist[self.lastindentlevel]))
		elif indentlevel > self.lastindentlevel + 1:
			tgl.returnError("Syntax Error", "Cannot indent forward by more than one level at at time", False)
			pass
		self.lastindentlevel = indentlevel
		return inputline




class pythonwrapper:
	def __init__(self):
		self.tmpvarcount = 0

	def headblock(self):
		block = '#!/usr/bin/python\nimport os, sys\nsys.path.append("'+os.getcwd()+'")\nimport trowelfunctions as tfl\n'
		return block

	def buildpython(self, listobject):
		self.checkaslintegrity(listobject)
		indentlevel = listobject[0][1]
		prodobject = listobject[1]
		production = listobject[1][0]
		self.tmpvarcount = 0
		
		block = ''
		tab = ''
		for i in range(indentlevel + tgl.indentback):
			tab = tab + '\t'
		
		if production == 'declaration':
			block = block + self.prod_declaration(prodobject)
		elif production == 'assignment':
			block = block + self.prod_assignment(prodobject)
		elif production == 'expression':
			[blockval,expval] = self.prod_expression(prodobject)
			block = block + blockval + expval + '\n'
		elif production == 'forstatement':
			block = block + self.prod_forstatement(prodobject)
		elif production == 'custom':
			block = block + self.prod_custom(prodobject)
		elif production == 'conditional':
			block += self.prod_conditional(prodobject)
			
		block = block.strip()
		blocklines = block.split('\n')
		
		block = ''
		for line in blocklines:
			if line != '':
				block = block + tab + line + '\n'
		#return '\n' + block
		return block

	def prod_declaration(self, listobject):
		block = ''
		datatype = listobject[1][1]
		for varobject in listobject[2]:
			if  len(varobject) == 2:
				assignobject = ['assignment', ['variable', varobject[0]], varobject[1]]
				block = block + self.prod_assignment(assignobject)
			else:
				block = block + varobject[0] + ' = '
				if datatype == 'number':
					block = block + '0\n'
				elif datatype == 'text' or 'url':
					block = block + '""\n'
				else:
					block = block + '[]\n'
		return block

	def prod_assignment(self, listobject):
		varname = listobject[1][1]
		vartype = tgl.varlist[tgl.indentlevel][varname]
		[block,expval] = self.prod_expression(listobject[2])
		block = block + varname + ' = ' + expval + '\n'
		return block

	def prod_expression(self, listobject):
		exptype  = listobject[1][0]
		block = ''
		expval = ''
		if exptype == 'functioncall':
			[blockval,expval] = self.prod_functioncall(listobject[1])
			block  = block + blockval
		elif exptype == 'list':
			tmplist = []
			for item in listobject[1][1]:
				[blockval,expval] = self.prod_expression(item)
				block = block + blockval
				#block = block + 'tmp' + str(self.tmpvarcount) + ' = ' + expval + '\n'
				#tmplist = tmplist + ['tmp' + str(self.tmpvarcount)]
				tmplist = tmplist + [expval]
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
	
	def prod_functioncall(self, listobject):
		block = ''
		functionname = listobject[1][1]
		argumentlist = listobject[3]	
		tmplist = []
		for item in argumentlist:
			[blockval,expval] = self.prod_expression(item)
			block = block + blockval
			#block = block + 'tmp' + str(self.tmpvarcount) + ' = ' + expval + '\n'
			#tmplist = tmplist + ['tmp' + str(self.tmpvarcount)]
			tmplist = tmplist + [expval]
			self.tmpvarcount = self.tmpvarcount + 1
			
		pythonarglist = '([' + ','.join(tmplist) + '])'
		if functionname in tgl.customfunctions:
			expval = functionname + '(' + ','.join(tmplist) + ')'
		else:
			expval = 'tfl.r_' + functionname + pythonarglist
		return [block,expval]

	def prod_forstatement(self, listobject):
		block = ''
		varname = listobject[1][1]
		[block,expval] = self.prod_expression(listobject[2])
		block = block + 'for ' + varname + ' in ' + expval + ':\n'
		return block



	def prod_conditional(self, listobject):
		control = listobject[1][1]
		if control == 'elseif': control = 'elif'
		result = self.prod_boolean_list(listobject[2])
		if not result: return control + ':\n'
		else: return result[0] + control + ' ' + result[1] + ':\n'

	def prod_boolean_list(self, listobject):
		this_list = listobject[1]
		if not this_list[0][0]:
			return None
		if len(this_list) > 1:
			# uses a logical (AND/OR/NOT)
			result1 = self.prod_boolean_list(this_list[0])
			result2 = self.prod_boolean_list(this_list[2])
			result = [result1[0] + result2[0]]
			result.append(result1[1] + ' ' + this_list[1] + ' ' + result2[1])
		else:
			# single boolean expression
			return self.prod_boolean(this_list[0])

	def prod_boolean(self, listobject):
		if len(listobject) == 3:
			# parenthesized boolean list
			result = self.prod_boolean_list(listobject[1])
			result[1] = '(' + result[1] + ')'
			return result
		elif len(listobject) == 2:
			# negation
			result = self.prod_boolean(listobject[1])
			result[1] = 'not ' + result[1]
			return result
		elif len(listobject) == 1:
			# expression
			return self.prod_expression(listobject[0])
		else:
			raise Exception('Illegal boolean format')


			
	#custom function handler
	def prod_custom(self, listobject):
		if listobject[1] is 'return':
			block = 'return ' + listobject[2][1][1]
		else:
			block = 'def ' + listobject[1] + '('
			next_type = []
			nt = 'text'
			new_var = False
			for arg in listobject[2]:
				if type(arg) is str:
					block = block + arg + ','
					next_type.append(nt)
					nt = 'text'
					if new_var:
						tgl.varlist[1][arg] = nt
					new_var = False
				else:
					nt = str(arg[1])
					new_var = True

			block = block[:-1] + ')' + ':' + '\n' 
			block = block + '\tif not tfl.checktype('+ str(next_type) +',list(reversed(locals().values()))): return \'' + listobject[1] + ' is used improperly\''
			tgl.customfunctions.append(listobject[1])
		return block



	# Function checks for abstract syntax tree structures.
	def checkaslintegrity(self, inputline):
		if inputline[0][0] == "indentlevel":
			if inputline[1][0] == "declaration":
				if (inputline[1][1][0] == "datatype") and (inputline[1][1][1] in ["number", "text", "url", "numlist", "textlist", "urllist"]):
					pass
				else:
					tgl.returnError("Syntax Error", "Declaration syntax mismatch", False)
			elif inputline[1][0] == "assignment":
				if inputline[1][1][0] == "variable":
					pass
				else:
					tgl.returnError("Syntax Error", "Assignment syntax mismatch", False)
			elif inputline[1][0] == "expression":
				if inputline[1][1][0] == "functioncall":
					if inputline[1][1][1][0] == "functionname":
						pass
					else:
						tgl.returnError("Syntax Error", "Expression function name mismatch", False)
				else:
					tgl.returnError("Syntax Error", "Expression function syntax mismatch", False)
			elif inputline[1][0] == "conditional":
				if inputline[1][1][0] == "control":
					pass
				else:
					tgl.returnError("Syntax Error", "Conditional function syntax mismatch", False)
			elif inputline[1][0] == "forstatement":
				pass
			elif inputline[1][0] == "custom":
				pass
			else:
				tgl.returnError("Syntax Error", "Missing syntax header", False)
			pass
		else:
			tgl.returnError("Syntax Error", "Missing indentation information", False)


if __name__ == '__main__':
	main()
