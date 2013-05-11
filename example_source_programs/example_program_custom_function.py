#!/usr/bin/python
import os, sys
sys.path.append("/Users/RWalport/Desktop/Rob_CS/PLT/plt")
import trowelfunctions as tfl
def gettweets(of,person,searching,twitter):
	if not tfl.checktype(['text', 'text', 'text', 'text'],list(reversed(locals().values()))): return 'gettweets is used improperly'
	prefix = ""
	prefix = 'https://twitter.com/'
	twitterurl = ""
	tmp0 = prefix
	tmp1 = 'and'
	tmp2 = person
	tfl.r_combine([tmp0,tmp1,tmp2])
	twitterurl = tfl.r_combine([tmp0,tmp1,tmp2])
	results = ""
	tmp0 = 'in'
	tmp1 = twitterurl
	tfl.r_findtext([tmp0,tmp1])
	results = tfl.r_findtext([tmp0,tmp1])
	return results
tweets = ""
tmp0 = 'of'
tmp1 = 'barackobama'
tmp2 = 'searching'
tmp3 = 'twitter'
gettweets(tmp0,tmp1,tmp2,tmp3)
tweets = gettweets(tmp0,tmp1,tmp2,tmp3)
tmp0 = tweets
tfl.r_print([tmp0])
