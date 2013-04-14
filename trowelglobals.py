intentlevel = 0
varlist = dict()
typelist = dict()
funclist = dict()
reservedlist = dict()

#functionname : [returntype(s)]
prebuiltfunctions = {
	'print' : [None],
	'read' : ['urllist','textlist'],
	'save' : [None],
	'append' : [None],
	'insert' : [None],
	'findurl' : ['urllist'],
	'findtext' : ['textlist'],
	'combine' : ['url'],
}

funclist = prebuiltfunctions