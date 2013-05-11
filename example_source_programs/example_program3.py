#!/usr/bin/python
import os, sys
sys.path.append("/Users/RWalport/Desktop/Rob_CS/PLT/plt")
import trowelfunctions as tfl
stories = ""
filteredresult = ""
term1 = 'obama'
term2 = 'ireland'
stories = tfl.r_read(['example_source_programs/example3.txt'])
filteredresult = tfl.r_findurl(['in',stories,'with',term1,'and',term2])
tfl.r_save([filteredresult,'into','example_source_programs/example3_output.txt'])
