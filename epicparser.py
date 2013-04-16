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
	
	inputline = parsebox.getline(inputfile)
	while inputline:
		tokenline = parsebox.gettokens(inputline)
		aslline = parsebox.getabstractlist(inputline)
		pythonline = pythonbox.buildpython(aslline)

		tokenfile.write(str(tokenline) + '\n')
		aslfile.write(str(aslline) + '\n')
		pythonfile.write(str(pythonline) + '\n')
		inputline = parsebox.getline(inputfile)



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
		pass
		
	def buildpython(self, inputline):
		pass
	
if __name__ == '__main__':
	main()	