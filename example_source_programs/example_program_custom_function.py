#!/usr/bin/python
import os, sys
sys.path.append("/Users/RWalport/Desktop/Rob_CS/PLT/plt")
import trowelfunctions as tfl
def gettweets(of,person,searching,twitter):
	if not tfl.checktype(['text', 'text', 'text', 'text'],list(reversed(locals().values()))): return 'gettweets is used improperly'
	prefix = 'https://twitter.com/'
	twitterurl = tfl.r_combine([prefix,'and',person])
	results = tfl.r_findtext(['in',twitterurl])
	return results
tweets = gettweets('of','barackobama','searching','twitter')
tfl.r_print([tweets])
