typelist = {}
locallist = []

def addNewType(variablename, typename):
	typelist[variablename] = typename
	locallist.append([typename, variablename])
	print "added"

def cleanLocalList():
	locallist = []

def printHash():
	print "Type list"
	print typelist

def printLocal():
	print "Local list"
	print locallist