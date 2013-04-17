import trowelglobals as tgl
#import trowelfunctions as tfs
import ply.lex as lex, ply.yacc as yacc
import lexingrules, parsingrules
from copy import copy

def main():
	inputfile = file('input.twl','r')
	tokenfile = file('tokens.twl','w')
	aslfile = file('asl.twl','w')
	pythonfile = file('python.twl','w')
	
	parsebox = parsewrapper()
	pythonbox = pythonwrapper()
	
	pythonfile.write(pythonbox.headblock())
	inputline = parsebox.getline(inputfile)
	while inputline:
		tokenline = parsebox.gettokens(inputline)
		aslline = parsebox.getabstractlist(inputline)
		pythonblock = pythonbox.buildpython(aslline)

		tokenfile.write(str(tokenline) + '\n')
		aslfile.write(str(aslline) + '\n')
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
		if line:
			line = line.rstrip()
			line = line.lower()
			line = self.filterindentation(line)
		return line
		
	def filterindentation(self, inputline):
		indentlevel = 0
		if inputline[0] == '\t':
			inputline = inputline[1:]
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


		
class pythonwrapper:
	def __init__(self):
		self.tmpvarcount = 0
		
	def headblock(self):
		block = 'import trowelfunctions as tfs\n'
		return block

	def checkaslintegrity(self, inputline):
		pass

		
	def buildpython(self, listobject):
		self.checkaslintegrity(listobject)
		indentlevel = listobject[0][1]
		prodobject = listobject[1]
		production = listobject[1][0]
		block = ''
		
		if production == 'declaration':
			block = block = block + self.prod_declaration(prodobject)
		elif production == 'assignment':
			block = block = block + self.prod_assignment(prodobject)
		elif	production == 'expression':
			block = block = block + self.prod_expression(prodobject)
		return block

			
	def prod_declaration(self, listobject):
		return ''

		
	def prod_assignment(self, listobject):
		return ''

		
	def prod_expression(self, listobject):
		return ''

		
	
if __name__ == '__main__':
	main()	