#!/usr/bin/python
import os, sys
sys.path.append("/Users/RWalport/Desktop/Rob_CS/PLT/plt")
import trowelfunctions as tfl
hellocontents = ""
hello = 'http://pythonweb.org/projects/webmodules/doc/0.5.3/html_multipage/web/node20.html'
hellocontents = tfl.r_findtext(['in',hello])
tfl.r_print([hellocontents])
