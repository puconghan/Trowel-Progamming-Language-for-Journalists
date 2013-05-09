#!/usr/bin/python
import trowelfunctions as tfl

stories = ""
filteredresult = ""

term1 = ""
term1 = 'obama'
term2 = ""
term2 = 'ireland'

tmp0 = 'example_source_programs/example3.txt'
tfl.r_read([tmp0])
stories = tfl.r_read([tmp0])

tmp0 = 'in'
tmp1 = stories
tmp2 = 'with'
tmp3 = term1
tmp4 = 'and'
tmp5 = term2
tfl.r_findurl([tmp0,tmp1,tmp2,tmp3,tmp4,tmp5])
filteredresult = tfl.r_findurl([tmp0,tmp1,tmp2,tmp3,tmp4,tmp5])

tmp0 = filteredresult
tmp1 = 'into'
tmp2 = 'example_source_programs/example3_output.txt'
tfl.r_save([tmp0,tmp1,tmp2])
