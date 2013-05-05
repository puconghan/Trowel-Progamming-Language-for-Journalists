###################################################################################################
# PROGRAM:      Trowel
# DESCRIPTION:  This trowelfunction.py program implement default functions for trowel.
#				This program will be imported by both targeted program and the parser.
# LICENSE:      PLY
# REFERENCES:   Python Lex-Yacc Documentation (http://www.dabeaz.com/ply/)
###################################################################################################

import sys
import trowelglobals as tgl
import urlparse
from urllib2 import Request, urlopen, URLError

#----------------------------------------------------------------------------------------------

#Section created by Hareesh and implemented by Pucong Han on April 20, 2013

def isnumber(input):
	if str(type(input)) == "<type 'int'>":
		return True
	else:
		return False
	
def isurl(input):
	if str(type(input)) == "<type 'int'>":
		return False
	parts = urlparse.urlsplit(input)
	if not parts.scheme or not parts.netloc:  
	    return False
	else:
		req = Request(input)
		try:
		    response = urlopen(req)
		except URLError, e:
		    if hasattr(e, 'reason'):
		        print 'Failed to reach a server.'
		        print 'Reason: ', e.reason
		        return False
		    elif hasattr(e, 'code'):
		        print 'The server does not respond request.'
		        print 'Error code: ', e.code
		        return False
		else:
			print "Yes"
			return True

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
		    return True
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

#----------------------------------------------------------------------------------------------

#Section created and implemented by Victoria Mo, Robert Walport and Pucong Han.

#takes a list of number/url/text
def r_printvars(arglist):
	print arglist
	return 1 #success

#takes a list of urllists/textlists
def r_printlist(arglist):
	for item in arglist: #can print multiple lists
		print item
	return 1 #success

#Print function handles both a list of number/url/text or a list of urllists/textlists
def r_print(arglist):
	for item in arglist:
		if str(type(item)) == "<type 'list'>":
			r_printlist(item)
		else:
			r_printvars(item)
	return 1 #success

#arglist is ['url',"with","text"/number]
def r_combine(arglist):
	return str(arglist[0]) + str(arglist[2])

#takes a url or text and adds it to the end of a urllist/textlist
#arglist is ['url'/"text", "into", urllist/textlist]
def r_insert(arglist):
	if len(arglist) != 3:
		tgl.returnError("Insert Function Syntax Error", "Format for insert in \"url/text\" into \"urllist/textlist\"", False)
		return 0
	arglist[2].append(arglist[0])
	return arglist[2]

#returns length of a list
def r_length(arglist):
	return len(arglist[0])
	
#----------------------------------------------------------------------------------------------

#Section created and implemented by Pucong Han on April 13, 2013.

##Save function for Trowel.
# Save a list of urls to an external txt file.
def r_save(arglist):
	if(arglist[1] != 'into'):
		tgl.returnError("Save Function Syntax Error", "Wrong format for save function. It should be 'save list of urls (or variables that contains list of urls) into filename'.", False)
		return False
	else:
		data = arglist[0]
		filename = arglist[2]
		outfile = open(filename, 'w')
		for item in data:
			outfile.write(item + "\n")
		return True

##Append function for Trowel.
# Append an url to an existing external txt file.
def r_append(arglist):
	if(arglist[1] != 'into'):
		tgl.returnError("Append Function Syntax Error", "Wrong format for append function. It should be 'append url (or variable contain an url) into filename'.", False)
		return False
	else:
		data = arglist[0]
		filename = arglist[2]
		if str(type(data)) == str("<type 'list'>"):
			for listitem in data:
				with open(filename, "a") as modifiedfile:
					modifiedfile.write("\n" + listitem)
		else:
			with open(filename, "a") as modifiedfile:
				modifiedfile.write("\n" + data)
		return True

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

#----------------------------------------------------------------------------------------------

#Section created and implemented by David Tagatac, Robert Walport and Pucong Han.

from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

LOGICALS = ['and', 'or', 'not', '(', ')']
IGNORE = ['with', 'in']

def r_findurl(arglist):
	# arglist[1] is the urlList to search (set() removes duplicates)
	this_urllist = set(arglist[1])
	result = []
	for this_url in this_urllist:
		parts = urlparse.urlsplit(this_url)
		if not parts.scheme or not parts.netloc:
			this_url = "http://" + this_url
		soup = BeautifulSoup(urlopen(this_url))
		truthiList = ""
		for entry in arglist[1:]:
			if str(type(entry)) != "<type 'list'>":
				if entry in LOGICALS:
					truthiList = truthiList + " " + entry
				elif entry in IGNORE:
					pass
				elif soup.find_all(text = re.compile(entry)):
					truthiList = truthiList + " True"
				else:
					truthiList = truthiList + " False"
		if eval(truthiList): result.append(this_url)
	return result

def r_findtext(arglist):
	link = arglist[1]
	parts = urlparse.urlsplit(link)
	if not parts.scheme or not parts.netloc:
		link = "http://" + link
	html = urlopen(link)	
	soup = BeautifulSoup(html)
	texts = soup.find_all('p')
	keyparas = []
	
	for para in texts:
		para = para.get_text()
		truthiList = ""
		for entry in arglist[2:]:
			if str(type(entry)) != "<type 'list'>":
				if entry in LOGICALS:
					truthiList = truthiList + " " + entry
				elif entry in IGNORE:
					pass
				elif entry in para:
					truthiList = truthiList + " True"
				else:
					truthiList = truthiList + " False"
		if eval(truthiList): keyparas.append(para)
	return keyparas