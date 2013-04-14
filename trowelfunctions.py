import sys
import trowelglobals as tgl

##Save function for Trowel.
# Save a list of urls to an external txt file.
# Create and implemented by Pucong Han on April 13, 2013.
def save(arglist):
	if(arglist[1] != 'into'):
		print "Wrong format for save function. It should be 'save list of urls (or variables that contains list of urls) into filename'."
		sys.exit()
	else:
		data = arglist[0]
		filename = arglist[2]
		outfile = open(filename, 'w')
		for item in data:
			outfile.write(item + "\n")

##Testing for save function.
#save([['www.bbc.com', 'www.cnn.com', 'www.reuters.com'],'into','temp.txt'])

##Append function for Trowel.
# Append an url to an existing external txt file.
# Create and implemented by Pucong Han on April 13, 2013.
def append(arglist):
	if(arglist[1] != 'into'):
		print "Wrong format for append function. It should be 'append url (or variable contain an url) into filename'."
		sys.exit()
	else:
		data = arglist[0]
		filename = arglist[2]
		if str(type(data)) == str("<type 'list'>"):
			for listitem in data:
				with open(filename, "a") as modifiedfile:
					modifiedfile.write(listitem + "\n")
		else:
			if tgl.varlist.get((tgl.indentlevel, data)) != None:
				storedurllist = tgl.varlist.get((tgl.indentlevel, data))
				for storeditem in storedurllist:
					with open(filename, "a") as modifiedfile:
						modifiedfile.write(storeditem + "\n")
			else:
				with open(filename, "a") as modifiedfile:
					modifiedfile.write(data + "\n")

##Testing for append one or more url to an external file (need to uncomment save function before uncomment the following code).
#append(['www.puconghan.com', 'into', 'temp.txt'])
#append([['www.columbia.edu', 'www.depauw.edu'], 'into', 'temp.txt'])

##Testing for append an url list to an external file (need to uncomment save function before uncomment the following code).
# tgl.varlist[(0, "testurllist")] = ['www.puconghan.com', 'www.robertwalport.com']
# print tgl.varlist
# append(["testurllist", 'into', 'temp.txt'])

##Read function for Trowel.
# Read an external txt file and return a list of urls.
# Create and implemented by Pucong Han on April 13, 2013.
def read(arglist):
	filename = arglist[0]
	try:
		read_url_list = []
		with open(filename, "r") as inputfile:
			for item in inputfile:
				read_url_list.append(item.rstrip('\n'))
	except IOError:
		print "Error: can\'t find the txt file or read data from the txt file"
		sys.exit()
	return read_url_list

##Testing for read urls from an external txt file
#print read(['temp.txt'])

##Insert function for Trowel.
# Insert url or text (either a list or text/url) and addes it to the end of a urllist or textlist.
# Create and implemented by Pucong Han on April 13, 2013.
def insert(arglist):
	if(arglist[1] != 'into'):
		print "Wrong format for append function. It should be 'insert (url, text, urllist or textlist) into (urllist or textlist)'."
		sys.exit()
	else:
		data = arglist[0]
		listname = arglist[2]
		if tgl.typelist.get((tgl.indentlevel, listname)) == "urllist":
			if str(type(data)) == str("<type 'list'>"):
				for listitem in data:
					tgl.varlist[(tgl.indentlevel, listname)].append(listitem)
			else:
				if tgl.typelist.get((tgl.indentlevel, data)) == "url":
					tgl.varlist[(tgl.indentlevel, listname)].append(tgl.varlist.get((tgl.indentlevel, data)))
				else:
					tgl.varlist[(tgl.indentlevel, listname)].append(data)
		elif tgl.typelist.get((tgl.indentlevel, listname)) == "textlist":
			if str(type(data)) == str("<type 'list'>"):
				for listitem in data:
					tgl.varlist[(tgl.indentlevel, listname)].append(listitem)
			else:
				if tgl.typelist.get((tgl.indentlevel, data)) == "text":
					tgl.varlist[(tgl.indentlevel, listname)].append(tgl.varlist.get((tgl.indentlevel, data)))
				else:
					tgl.varlist[(tgl.indentlevel, listname)].append(data)
		else:
			print "Wrong format for insert function. " + listname + " should be a list."
			sys.exit()

##Testing for adding an url to an urllist variable
# tgl.varlist[(0, "testurllist")] = ['www.puconghan.com', 'www.robertwalport.com']
# tgl.typelist[(0, "testurllist")] = "urllist"
# insert(['www.sina.com', 'into', 'testurllist'])
# print tgl.varlist
##Testing for adding a list of url to an urllist variable
# tgl.varlist[(0, "testurllist")] = ['www.puconghan.com', 'www.robertwalport.com']
# tgl.typelist[(0, "testurllist")] = "urllist"
# insert([['www.sina.com','www.sohu.com'], 'into', 'testurllist'])
# print tgl.varlist
##Testing for adding a text to an textlist variable
# tgl.varlist[(0, "testlist")] = ["hello", "world"]
# tgl.typelist[(0, "testlist")] = "textlist"
# insert(["great", 'into', 'testlist'])
# print tgl.varlist
##Testing for adding a list of text to an textlist variable
# tgl.varlist[(0, "testlist")] = ["hello", "world"]
# tgl.typelist[(0, "testlist")] = "textlist"
# insert([["great","fine"], 'into', 'testlist'])
# print tgl.varlist

