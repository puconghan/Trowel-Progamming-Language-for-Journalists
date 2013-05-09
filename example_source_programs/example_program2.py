#!/usr/bin/python
import trowelfunctions as tfl

stories = ""
tmp0 = 'http://www.bbc.co.uk/news/business-21857393'
tmp1 = 'http://www.bbc.co.uk/news/uk-northern-ireland-21855357'
stories = [tmp0,tmp1]
filteredresult = ""

term1 = ""
term1 = 'obama'
term2 = ""
term2 = 'ireland'

tmp0 = 'in'
tmp1 = stories
tmp2 = 'with'
tmp3 = term1
tmp4 = 'and'
tmp5 = term2
tfl.r_findurl([tmp0,tmp1,tmp2,tmp3,tmp4,tmp5])
filteredresult = tfl.r_findurl([tmp0,tmp1,tmp2,tmp3,tmp4,tmp5])

tmp0 = filteredresult
tfl.r_print([tmp0])
