import trowelglobals as tgl
import ply.lex as lex, ply.yacc as yacc
import lexingrules, parsingrules

def main():
	inputfile = file('input.twl','r')
	tokenfile = file('tokens.out','w')
	aslfile = file('asl.out','w')
	
	parsebox = parsewrapper()
	inputline = processline(inputfile.readline())
	while inputline:
		tokenfile.write(str(parsebox.gettokens(inputline)) + '\n')
		aslfile.write(str(parsebox.getabstractlist(inputline)) + '\n')
		inputline = processline(inputfile.readline())

def processline(line):
	if line:
		line = line.rstrip()
		line = line.lower()
	return line
	
class parsewrapper:
	def __init__(self):
		self.initparser()
	
	def initparser(self):
		self.lexer = lex.lex(module = lexingrules)
		self.parser = yacc.yacc(module = parsingrules)

	def gettokens(self, inputline):
		self.lexer.input(inputline)
		tokenlist = []
		for token in self.lexer:
			tokenlist = tokenlist + [[token.type,token.value,token.lineno]]
		return tokenlist
	
	def getabstractlist(self, inputline):
		return self.parser.parse(input = inputline, lexer = self.lexer)
	
if __name__ == '__main__':
	main()