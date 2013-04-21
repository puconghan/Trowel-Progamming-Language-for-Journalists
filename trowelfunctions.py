import sys
import trowelglobals as tgl
import urlparse

#Section created by Hareesh and implemented by Pucong Han on April 20, 2013

def isnumber(input):
	if str(type(input)) == "<type 'int'>":
		return True
	else:
		return False
	
def isurl(input):
	parts = urlparse.urlsplit(input)
	if not parts.scheme or not parts.netloc:  
	    return False
	else:
	    print True

def istext(input):
	if str(type(input)) == "<type 'str'>":
		return True
	else:
		return False

def isnumlist(inputlist):
	if str(type(inputlist)) == "<type 'list'>":
		if str(type(inputlist[0])) == "<type 'int'>":
			return True
		else:
			return False
	else:
		return False
	
def isurllist(inputlist):
	if str(type(inputlist)) == "<type 'list'>":
		parts = urlparse.urlsplit(inputlist[0])
		if not parts.scheme or not parts.netloc:  
		    return False
		else:
		    print True
	else:
		return False
	
def istextlist(inputlist):
	if str(type(inputlist)) == "<type 'list'>":
		if str(type(inputlist[0])) == "<type 'str'>":
			return True
		else:
			return False
	else:
		return False

def checktype(typelist, inputlist):
	if len(typelist) == len(inputlist):
		flag = True
		for idx, val in typelist:
			if var in ['number', 'url', 'text', 'numlist', 'textlist', 'urllist']:
				if val == 'number':
					flag = flag and isnumber(inputlist[idx])
				if val == 'url':
					flag = flag and isurl(inputlist[idx])
				if val == 'text':
					flag = flag and istext(inputlist[idx])
				if val == 'numlist':
					flag = flag and isnumlist(inputlist[idx])
				if val == 'urllist':
					flag = flag and isurllist(inputlist[idx])
				if val == 'textlist':
					flag = flag and istextlist(inputlist[idx])
			else:
				if var == inputlist[idx]:
					flag = True
				else:
					flag = False
		if flag == True:
			return True
		else:
			return False
	else:
		return False

#--------------------------------------------------------------------------

#Section created and implemented by Victoria Mo and Robert Walport.

#takes a list of number/url/text
def r_printvars(arglist):
	to_print = ''
	for entry in arglist:
		to_print = to_print + str(entry)
	print to_print
	return 1 #success

#takes a list of urllists/textlists
def r_printlist(arglist):
	for list_to_print in arglist: #can print multiple lists
		for entry in list_to_print:
			print entry
	return 1 #success

#arglist is ['url',"with","text"/number]
def r_combine(arglist):
	return str(arglist[0]) + str(arglist[2])

#takes a url or text and adds it to the end of a urllist/textlist
#arglist is ['url'/"text", "into", urllist/textlist]
def r_insert(arglist):
	if len(arglist) != 3:
		print "Format for insert in \"url/text\" into \"urllist/textlist\""
		return 0
	arglist[2].append(arglist[0])
	return arglist[2]

#returns length of a list
def r_length(arglist):
	return len(arglist[0])
	
#--------------------------------------------------------------------------

#Section created and implemented by Pucong Han on April 13, 2013.

##Save function for Trowel.
# Save a list of urls to an external txt file.
def r_save(arglist):
	if(arglist[1] != 'into'):
		tgl.returnError("Save Function Syntax Miss Match", "Wrong format for save function. It should be 'save list of urls (or variables that contains list of urls) into filename'.", True)
	else:
		data = arglist[0]
		filename = arglist[2]
		outfile = open(filename, 'w')
		for item in data:
			outfile.write(item + "\n")

##Append function for Trowel.
# Append an url to an existing external txt file.
def r_append(arglist):
	if(arglist[1] != 'into'):
		tgl.returnError("Append Function Syntax Miss Match", "Wrong format for append function. It should be 'append url (or variable contain an url) into filename'.", True)
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

##Read function for Trowel.
# Read an external txt file and return a list of urls.
def r_read(arglist):
	filename = arglist[0]
	try:
		read_url_list = []
		with open(filename, "r") as inputfile:
			for item in inputfile:
				read_url_list.append(item.rstrip('\n'))
	except IOError:
		tgl.returnError("Read Function Missing File Error", "Error: can\'t find the txt file or read data from the txt file", True)
	return read_url_list

#--------------------------------------------------------------------------

#Section created and implemented by David Tagatac and Robert Walport

from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

def r_findUrl(arglist):
	# arglist[0] is the urlList to search (set() removes duplicates)
	this_urllist = list(set(arglist[0]))
	# arglist[1] is the FE to find
	keywords = []
	for entry in arglist[1:]:
		if entry != "and" and entry != "or" and entry != "not":
			keywords.append(entry)
			
	result = []
	for this_url in this_urllist:
		print this_url
		soup = BeautifulSoup(urlopen(this_url))
		truthiList = []
		for keyword in keywords:
			if soup.find_all(text = re.compile(keyword)):
				truthiList.append(True)
			else:
				truthiList.append(False)
		print truthiList

def r_findText(arglist):
	# arglist[0] is the urlList to search (set() removes duplicates)
	this_urllist = set(arglist[0])
	#arglist[1] is the FE to find
	this_FE = arglist[1]
	parents_visited = []
	result = []
	for this_url in this_urllist:
		soup = BeautifulSoup(urlopen(this_url))
		for this_tag in soup.find_all(text = re.compile(this_FE)):
			this_parent = this_tag.parent
			if this_parent in parents_visited: continue
			parents_visited.append(this_parent)
			this_text = ''
			for this_sibling in this_tag.parent.children: this_text += this_sibling.string
			result.append(this_text)
	return result