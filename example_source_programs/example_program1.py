#!/usr/bin/python
import trowelfunctions as tfl

hellocontents = ""

hello = ""
hello = 'http://pythonweb.org/projects/webmodules/doc/0.5.3/html_multipage/web/node20.html'

tmp0 = 'in'
tmp1 = hello
tfl.r_findtext([tmp0,tmp1])
hellocontents = tfl.r_findtext([tmp0,tmp1])

tmp0 = hellocontents
tfl.r_print([tmp0])
