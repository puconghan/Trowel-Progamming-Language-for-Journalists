#!/usr/bin/python
import os, sys
sys.path.append("/Users/RWalport/Desktop/Rob_CS/PLT/plt")
import trowelfunctions as tfl
stories = ['http://www.bbc.co.uk/news/business-21857393','http://www.bbc.co.uk/news/uk-northern-ireland-21855357']
filteredresult = ""
term1 = 'obama'
term2 = 'ireland'
filteredresult = tfl.r_findurl(['in',stories,'with',term1,'and',term2])
tfl.r_print([filteredresult])
