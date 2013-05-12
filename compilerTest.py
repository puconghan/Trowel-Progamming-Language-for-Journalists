#!/usr/bin/python
# -----------------------------------------------------------------------------
# compilerTest.py
# This file contains tests to verify that
# each module in the compiler is working correctly.
# -----------------------------------------------------------------------------
# Authors ->
#	This file was written by Robert.
# -----------------------------------------------------------------------------

import os, unittest

class TestTrowel(unittest.TestCase):

    def test_decassign_program(self):
        os.system("./trowel tests/decassign.twl")
        k = open("tokens.twl")
        tokens = k.readlines()
        self.assertEqual(tokens, ["[['NUMLIST', 'numlist', 1], ['UNKNOWNWORD', 'x', 1], ['COMMA', ',', 1], ['UNKNOWNWORD', 'j', 1]]\n", "[['NUMBER', 'number', 1], ['UNKNOWNWORD', 'lengthcheck', 1]]\n", "[['NUMLIST', 'numlist', 1], ['UNKNOWNWORD', 'z', 1], ['IS', 'is', 1], ['LEFTSQUAREBRACKET', '[', 1], ['NUMVAL', '6', 1], ['COMMA', ',', 1], ['NUMVAL', '7', 1], ['COMMA', ',', 1], ['NUMVAL', '8', 1], ['COMMA', ',', 1], ['NUMVAL', '9', 1], ['COMMA', ',', 1], ['NUMVAL', '10', 1], ['RIGHTSQUAREBRACKET', ']', 1]]\n", "[['UNKNOWNWORD', 'x', 1], ['IS', 'is', 1], ['LEFTSQUAREBRACKET', '[', 1], ['NUMVAL', '1', 1], ['COMMA', ',', 1], ['NUMVAL', '2', 1], ['COMMA', ',', 1], ['NUMVAL', '3', 1], ['COMMA', ',', 1], ['NUMVAL', '4', 1], ['COMMA', ',', 1], ['NUMVAL', '5', 1], ['RIGHTSQUAREBRACKET', ']', 1]]\n"])
        k.close()
        a = open("asl.twl")
        asl = a.readlines()
        a.close()
        self.assertEqual(asl, ["[['indentlevel', 0], ['declaration', ['datatype', 'numlist'], [['x'], ['j']]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'number'], [['lengthcheck']]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'numlist'], [['z', ['expression', ['list', [['expression', ['value', ['number', 6]]], ['expression', ['value', ['number', 7]]], ['expression', ['value', ['number', 8]]], ['expression', ['value', ['number', 9]]], ['expression', ['value', ['number', 10]]]]]]]]]]\n", "[['indentlevel', 0], ['assignment', ['variable', 'x'], ['expression', ['list', [['expression', ['value', ['number', 1]]], ['expression', ['value', ['number', 2]]], ['expression', ['value', ['number', 3]]], ['expression', ['value', ['number', 4]]], ['expression', ['value', ['number', 5]]]]]]]]\n"])
        f = open('tests/decassign.py')
        python = f.readlines()
        self.assertEqual(python[4:], ['x = ""\n', 'j = ""\n', 'lengthcheck = 0\n', 'z = [6,7,8,9,10]\n', 'x = [1,2,3,4,5]\n'])
        f.close()

    def test_print_program(self):
        os.system("./trowel tests/print.twl")
        k = open("tokens.twl")
        tokens = k.readlines()
        self.assertEqual(tokens, ["[['UNKNOWNWORD', 'print', 1], ['NUMVAL', '45', 1]]\n"])
        k.close()
        a = open("asl.twl")
        asl = a.readlines()
        a.close()
        self.assertEqual(asl, ["[['indentlevel', 0], ['expression', ['functioncall', ['functionname', 'print'], 'arguments', [['expression', ['value', ['number', 45]]]]]]]\n"])
        f = open('tests/print.py')
        python = f.readlines()
        self.assertEqual(python[4:], ['tfl.r_print([45])\n'])
        f.close()

    def test_addcombine_program(self):
        os.system("./trowel tests/addcombine.twl")
        k = open("tokens.twl")
        tokens = k.readlines()
        self.assertEqual(tokens, ["[['URL', 'url', 1], ['UNKNOWNWORD', 'x', 1]]\n", "[['NUMBER', 'number', 1], ['UNKNOWNWORD', 'y', 1], ['IS', 'is', 1], ['NUMVAL', '5', 1]]\n", '[[\'UNKNOWNWORD\', \'x\', 1], [\'IS\', \'is\', 1], [\'UNKNOWNWORD\', \'combine\', 1], [\'URLVAL\', "\'www.bbc.co.uk?\'", 1], [\'UNKNOWNWORD\', \'with\', 1], [\'LEFTPAREN\', \'(\', 1], [\'UNKNOWNWORD\', \'y\', 1], [\'PLUS\', \'+\', 1], [\'NUMVAL\', \'2\', 1], [\'RIGHTPAREN\', \')\', 1]]\n', '[[\'UNKNOWNWORD\', \'save\', 1], [\'UNKNOWNWORD\', \'x\', 1], [\'UNKNOWNWORD\', \'into\', 1], [\'TEXTVAL\', \'"output.txt"\', 1]]\n'])
        k.close()
        a = open("asl.twl")
        asl = a.readlines()
        a.close()
        self.assertEqual(asl, ["[['indentlevel', 0], ['declaration', ['datatype', 'url'], [['x']]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'number'], [['y', ['expression', ['value', ['number', 5]]]]]]]\n", "[['indentlevel', 0], ['assignment', ['variable', 'x'], ['expression', ['functioncall', ['functionname', 'combine'], 'arguments', [['expression', ['value', ['url', 'www.bbc.co.uk?']]], ['expression', ['insertword', 'with']], ['expression', ['functioncall', ['functionname', 'plus'], 'arguments', [['expression', ['variable', 'y']], ['expression', ['value', ['number', 2]]]]]]]]]]]\n", "[['indentlevel', 0], ['expression', ['functioncall', ['functionname', 'save'], 'arguments', [['expression', ['variable', 'x']], ['expression', ['insertword', 'into']], ['expression', ['value', ['text', 'output.txt']]]]]]]\n"])
        f = open('tests/addcombine.py')
        python = f.readlines()
        self.assertEqual(python[4:], ['x = ""\n', 'y = 5\n', "x = tfl.r_combine(['www.bbc.co.uk?','with',tfl.r_plus([y,2])])\n", "tfl.r_save([x,'into','output.txt'])\n"])
        f.close()

    def test_helloWorld_program(self):
        os.system("./trowel tests/hello.twl")
        k = open("tokens.twl")
        tokens = k.readlines()
        self.assertEqual(tokens, ["[['TEXTLIST', 'textlist', 1], ['UNKNOWNWORD', 'hellocontents', 1]]\n", '[[\'URL\', \'url\', 1], [\'UNKNOWNWORD\', \'hello\', 1], [\'IS\', \'is\', 1], [\'URLVAL\', "\'www.journotrowel.com/examples/hello.html\'", 1]]\n', "[['UNKNOWNWORD', 'hellocontents', 1], ['IS', 'is', 1], ['UNKNOWNWORD', 'findtext', 1], ['UNKNOWNWORD', 'in', 1], ['UNKNOWNWORD', 'hello', 1]]\n", "[['UNKNOWNWORD', 'print', 1], ['UNKNOWNWORD', 'hellocontents', 1]]\n", '[[\'UNKNOWNWORD\', \'save\', 1], [\'UNKNOWNWORD\', \'hellocontents\', 1], [\'UNKNOWNWORD\', \'into\', 1], [\'TEXTVAL\', \'"output.txt"\', 1]]\n'])
        k.close()
        a = open("asl.twl")
        asl = a.readlines()
        a.close()
        self.assertEqual(asl, ["[['indentlevel', 0], ['declaration', ['datatype', 'textlist'], [['hellocontents']]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'url'], [['hello', ['expression', ['value', ['url', 'www.journotrowel.com/examples/hello.html']]]]]]]\n", "[['indentlevel', 0], ['assignment', ['variable', 'hellocontents'], ['expression', ['functioncall', ['functionname', 'findtext'], 'arguments', [['expression', ['insertword', 'in']], ['expression', ['variable', 'hello']]]]]]]\n", "[['indentlevel', 0], ['expression', ['functioncall', ['functionname', 'print'], 'arguments', [['expression', ['variable', 'hellocontents']]]]]]\n", "[['indentlevel', 0], ['expression', ['functioncall', ['functionname', 'save'], 'arguments', [['expression', ['variable', 'hellocontents']], ['expression', ['insertword', 'into']], ['expression', ['value', ['text', 'output.txt']]]]]]]\n"])
        f = open('tests/hello.py')
        python = f.readlines()
        self.assertEqual(python[4:], ['hellocontents = ""\n', "hello = 'www.journotrowel.com/examples/hello.html'\n", "hellocontents = tfl.r_findtext(['in',hello])\n", 'tfl.r_print([hellocontents])\n', "tfl.r_save([hellocontents,'into','output.txt'])\n"])
        f.close()

    def test_flighttime_program(self):
        os.system("./trowel tests/flightTime.twl")
        k = open("tokens.twl")
        tokens = k.readlines()
        self.assertEqual(tokens, ["[['TEXTLIST', 'textlist', 1], ['UNKNOWNWORD', 'flighttime', 1]]\n", '[[\'URL\', \'url\', 1], [\'UNKNOWNWORD\', \'spacearticle\', 1], [\'IS\', \'is\', 1], [\'URLVAL\', "\'http://journotrowel.com/examples/science-environment-22344398.html\'", 1]]\n', '[[\'UNKNOWNWORD\', \'flighttime\', 1], [\'IS\', \'is\', 1], [\'UNKNOWNWORD\', \'findtext\', 1], [\'UNKNOWNWORD\', \'in\', 1], [\'UNKNOWNWORD\', \'spacearticle\', 1], [\'UNKNOWNWORD\', \'with\', 1], [\'TEXTVAL\', \'"time"\', 1], [\'AND\', \'and\', 1], [\'TEXTVAL\', \'"flight"\', 1]]\n', '[[\'UNKNOWNWORD\', \'save\', 1], [\'UNKNOWNWORD\', \'flighttime\', 1], [\'UNKNOWNWORD\', \'into\', 1], [\'TEXTVAL\', \'"output.txt"\', 1]]\n'])
        k.close()
        a = open("asl.twl")
        asl = a.readlines()
        a.close()
        self.assertEqual(asl, ["[['indentlevel', 0], ['declaration', ['datatype', 'textlist'], [['flighttime']]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'url'], [['spacearticle', ['expression', ['value', ['url', 'http://journotrowel.com/examples/science-environment-22344398.html']]]]]]]\n", "[['indentlevel', 0], ['assignment', ['variable', 'flighttime'], ['expression', ['functioncall', ['functionname', 'findtext'], 'arguments', [['expression', ['insertword', 'in']], ['expression', ['variable', 'spacearticle']], ['expression', ['insertword', 'with']], ['expression', ['value', ['text', 'time']]], ['expression', ['insertword', 'and']], ['expression', ['value', ['text', 'flight']]]]]]]]\n", "[['indentlevel', 0], ['expression', ['functioncall', ['functionname', 'save'], 'arguments', [['expression', ['variable', 'flighttime']], ['expression', ['insertword', 'into']], ['expression', ['value', ['text', 'output.txt']]]]]]]\n"])
        f = open('tests/flighttime.py')
        python = f.readlines()
        self.assertEqual(python[4:], ['flighttime = ""\n', "spacearticle = 'http://journotrowel.com/examples/science-environment-22344398.html'\n", "flighttime = tfl.r_findtext(['in',spacearticle,'with','time','and','flight'])\n", "tfl.r_save([flighttime,'into','output.txt'])\n"])
        f.close()
        
    def test_if_program(self):
        os.system("./trowel tests/if.twl")
        k = open("tokens.twl")
        tokens = k.readlines()
        self.assertEqual(tokens, ["[['TEXTLIST', 'textlist', 1], ['UNKNOWNWORD', 'hello', 1]]\n", "[['IF', 'if', 1], ['NUMVAL', '4', 1], ['GREATER', '>', 1], ['NUMVAL', '3', 1], ['COLON', ':', 1]]\n", '[[\'UNKNOWNWORD\', \'print\', 1], [\'TEXTVAL\', \'"boomshakalaka"\', 1]]\n', '[[\'UNKNOWNWORD\', \'save\', 1], [\'TEXTVAL\', \'"boomshakalaka"\', 1], [\'UNKNOWNWORD\', \'into\', 1], [\'TEXTVAL\', \'"output.txt"\', 1]]\n'])
        k.close()
        a = open("asl.twl")
        asl = a.readlines()
        a.close()
        self.assertEqual(asl, ["[['indentlevel', 0], ['declaration', ['datatype', 'textlist'], [['hello']]]]\n", "[['indentlevel', 1], ['conditional', ['control', 'if'], ['boolean_list', [[['expression', ['functioncall', ['functionname', 'greater'], 'arguments', [['expression', ['value', ['number', 4]]], ['expression', ['value', ['number', 3]]]]]]]]]]]\n", "[['indentlevel', 1], ['expression', ['functioncall', ['functionname', 'print'], 'arguments', [['expression', ['value', ['text', 'boomshakalaka']]]]]]]\n", "[['indentlevel', 1], ['expression', ['functioncall', ['functionname', 'save'], 'arguments', [['expression', ['value', ['text', 'boomshakalaka']]], ['expression', ['insertword', 'into']], ['expression', ['value', ['text', 'output.txt']]]]]]]\n"])
        f = open('tests/if.py')
        python = f.readlines()
        self.assertEqual(python[4:], ['hello = ""\n', 'if tfl.r_greater([4,3]):\n', "\ttfl.r_print(['boomshakalaka'])\n", "\ttfl.r_save(['boomshakalaka','into','output.txt'])\n"])
        f.close()
        
        
    ## Example programs
    #Example 1
    def test_example1_program(self):
        os.system("./trowel example_source_programs/example_program1.twl")
        k = open("tokens.twl")
        tokens = k.readlines()
        self.assertEqual(tokens, ["[['COMMENT', '#hello world! trowel example program 1', 1]]\n", "[['TEXTLIST', 'textlist', 1], ['UNKNOWNWORD', 'hellocontents', 1]]\n", '[[\'URL\', \'url\', 1], [\'UNKNOWNWORD\', \'hello\', 1], [\'IS\', \'is\', 1], [\'URLVAL\', "\'http://pythonweb.org/projects/webmodules/doc/0.5.3/html_multipage/web/node20.html\'", 1]]\n', "[['UNKNOWNWORD', 'hellocontents', 1], ['IS', 'is', 1], ['UNKNOWNWORD', 'findtext', 1], ['UNKNOWNWORD', 'in', 1], ['UNKNOWNWORD', 'hello', 1]]\n", "[['UNKNOWNWORD', 'print', 1], ['UNKNOWNWORD', 'hellocontents', 1]]\n"])
        k.close()
        a = open("asl.twl")
        asl = a.readlines()
        a.close()
        self.assertEqual(asl, ['None\n', "[['indentlevel', 0], ['declaration', ['datatype', 'textlist'], [['hellocontents']]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'url'], [['hello', ['expression', ['value', ['url', 'http://pythonweb.org/projects/webmodules/doc/0.5.3/html_multipage/web/node20.html']]]]]]]\n", "[['indentlevel', 0], ['assignment', ['variable', 'hellocontents'], ['expression', ['functioncall', ['functionname', 'findtext'], 'arguments', [['expression', ['insertword', 'in']], ['expression', ['variable', 'hello']]]]]]]\n", "[['indentlevel', 0], ['expression', ['functioncall', ['functionname', 'print'], 'arguments', [['expression', ['variable', 'hellocontents']]]]]]\n"])
        f = open('example_source_programs/example_program1.py')
        python = f.readlines()
        self.assertEqual(python[4:], ['hellocontents = ""\n', "hello = 'http://pythonweb.org/projects/webmodules/doc/0.5.3/html_multipage/web/node20.html'\n", "hellocontents = tfl.r_findtext(['in',hello])\n", 'tfl.r_print([hellocontents])\n'])
        f.close()
        
    def test_example2_program(self):
        os.system("./trowel example_source_programs/example_program2.twl")
        k = open("tokens.twl")
        tokens = k.readlines()
        self.assertEqual(tokens, ["[['COMMENT', '#manyurls trowel example program 2', 1]]\n", '[[\'URLLIST\', \'urllist\', 1], [\'UNKNOWNWORD\', \'stories\', 1], [\'IS\', \'is\', 1], [\'LEFTSQUAREBRACKET\', \'[\', 1], [\'URLVAL\', "\'http://www.bbc.co.uk/news/business-21857393\'", 1], [\'COMMA\', \',\', 1], [\'URLVAL\', "\'http://www.bbc.co.uk/news/uk-northern-ireland-21855357\'", 1], [\'RIGHTSQUAREBRACKET\', \']\', 1], [\'COMMA\', \',\', 1], [\'UNKNOWNWORD\', \'filteredresult\', 1]]\n', '[[\'TEXT\', \'text\', 1], [\'UNKNOWNWORD\', \'term1\', 1], [\'IS\', \'is\', 1], [\'TEXTVAL\', \'"obama"\', 1], [\'COMMA\', \',\', 1], [\'UNKNOWNWORD\', \'term2\', 1], [\'IS\', \'is\', 1], [\'TEXTVAL\', \'"ireland"\', 1]]\n', "[['UNKNOWNWORD', 'filteredresult', 1], ['IS', 'is', 1], ['UNKNOWNWORD', 'findurl', 1], ['UNKNOWNWORD', 'in', 1], ['UNKNOWNWORD', 'stories', 1], ['UNKNOWNWORD', 'with', 1], ['UNKNOWNWORD', 'term1', 1], ['AND', 'and', 1], ['UNKNOWNWORD', 'term2', 1]]\n", "[['UNKNOWNWORD', 'print', 1], ['UNKNOWNWORD', 'filteredresult', 1]]\n"])
        k.close()
        a = open("asl.twl")
        asl = a.readlines()
        a.close()
        self.assertEqual(asl, ['None\n', "[['indentlevel', 0], ['declaration', ['datatype', 'urllist'], [['stories', ['expression', ['list', [['expression', ['value', ['url', 'http://www.bbc.co.uk/news/business-21857393']]], ['expression', ['value', ['url', 'http://www.bbc.co.uk/news/uk-northern-ireland-21855357']]]]]]], ['filteredresult']]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'text'], [['term1', ['expression', ['value', ['text', 'obama']]]], ['term2', ['expression', ['value', ['text', 'ireland']]]]]]]\n", "[['indentlevel', 0], ['assignment', ['variable', 'filteredresult'], ['expression', ['functioncall', ['functionname', 'findurl'], 'arguments', [['expression', ['insertword', 'in']], ['expression', ['variable', 'stories']], ['expression', ['insertword', 'with']], ['expression', ['variable', 'term1']], ['expression', ['insertword', 'and']], ['expression', ['variable', 'term2']]]]]]]\n", "[['indentlevel', 0], ['expression', ['functioncall', ['functionname', 'print'], 'arguments', [['expression', ['variable', 'filteredresult']]]]]]\n"])
        f = open('example_source_programs/example_program2.py')
        python = f.readlines()
        self.assertEqual(python[4:], ["stories = ['http://www.bbc.co.uk/news/business-21857393','http://www.bbc.co.uk/news/uk-northern-ireland-21855357']\n", 'filteredresult = ""\n', "term1 = 'obama'\n", "term2 = 'ireland'\n", "filteredresult = tfl.r_findurl(['in',stories,'with',term1,'and',term2])\n", 'tfl.r_print([filteredresult])\n'])
        f.close()
        
    def test_example3_program(self):
        os.system("./trowel example_source_programs/example_program3.twl")
        k = open("tokens.twl")
        tokens = k.readlines()
        self.assertEqual(tokens, ["[['COMMENT', '# file i/o trowel example program 3', 1]]\n", "[['URLLIST', 'urllist', 1], ['UNKNOWNWORD', 'stories', 1], ['COMMA', ',', 1], ['UNKNOWNWORD', 'filteredresult', 1]]\n", '[[\'TEXT\', \'text\', 1], [\'UNKNOWNWORD\', \'term1\', 1], [\'IS\', \'is\', 1], [\'TEXTVAL\', \'"obama"\', 1], [\'COMMA\', \',\', 1], [\'UNKNOWNWORD\', \'term2\', 1], [\'IS\', \'is\', 1], [\'TEXTVAL\', \'"ireland"\', 1]]\n', '[[\'UNKNOWNWORD\', \'stories\', 1], [\'IS\', \'is\', 1], [\'UNKNOWNWORD\', \'read\', 1], [\'TEXTVAL\', \'"example_source_programs/example3.txt"\', 1]]\n', "[['UNKNOWNWORD', 'filteredresult', 1], ['IS', 'is', 1], ['UNKNOWNWORD', 'findurl', 1], ['UNKNOWNWORD', 'in', 1], ['UNKNOWNWORD', 'stories', 1], ['UNKNOWNWORD', 'with', 1], ['UNKNOWNWORD', 'term1', 1], ['AND', 'and', 1], ['UNKNOWNWORD', 'term2', 1]]\n", '[[\'UNKNOWNWORD\', \'save\', 1], [\'UNKNOWNWORD\', \'filteredresult\', 1], [\'UNKNOWNWORD\', \'into\', 1], [\'TEXTVAL\', \'"example_source_programs/example3_output.txt"\', 1]]\n'])
        k.close()
        a = open("asl.twl")
        asl = a.readlines()
        a.close()
        self.assertEqual(asl, ['None\n', "[['indentlevel', 0], ['declaration', ['datatype', 'urllist'], [['stories'], ['filteredresult']]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'text'], [['term1', ['expression', ['value', ['text', 'obama']]]], ['term2', ['expression', ['value', ['text', 'ireland']]]]]]]\n", "[['indentlevel', 0], ['assignment', ['variable', 'stories'], ['expression', ['functioncall', ['functionname', 'read'], 'arguments', [['expression', ['value', ['text', 'example_source_programs/example3.txt']]]]]]]]\n", "[['indentlevel', 0], ['assignment', ['variable', 'filteredresult'], ['expression', ['functioncall', ['functionname', 'findurl'], 'arguments', [['expression', ['insertword', 'in']], ['expression', ['variable', 'stories']], ['expression', ['insertword', 'with']], ['expression', ['variable', 'term1']], ['expression', ['insertword', 'and']], ['expression', ['variable', 'term2']]]]]]]\n", "[['indentlevel', 0], ['expression', ['functioncall', ['functionname', 'save'], 'arguments', [['expression', ['variable', 'filteredresult']], ['expression', ['insertword', 'into']], ['expression', ['value', ['text', 'example_source_programs/example3_output.txt']]]]]]]\n"])
        f = open('example_source_programs/example_program3.py')
        python = f.readlines()
        self.assertEqual(python[4:], ['stories = ""\n', 'filteredresult = ""\n', "term1 = 'obama'\n", "term2 = 'ireland'\n", "stories = tfl.r_read(['example_source_programs/example3.txt'])\n", "filteredresult = tfl.r_findurl(['in',stories,'with',term1,'and',term2])\n", "tfl.r_save([filteredresult,'into','example_source_programs/example3_output.txt'])\n"])
        f.close()
        
    def test_example4_program(self):
        os.system("./trowel example_source_programs/example_program4.twl")
        k = open("tokens.twl")
        tokens = k.readlines()
        self.assertEqual(tokens, ["[['COMMENT', '# control structures trowel example program 4', 1]]\n", '[[\'URLLIST\', \'urllist\', 1], [\'UNKNOWNWORD\', \'stories\', 1], [\'IS\', \'is\', 1], [\'UNKNOWNWORD\', \'read\', 1], [\'TEXTVAL\', \'"example_source_programs/election.txt"\', 1]]\n', '[[\'TEXT\', \'text\', 1], [\'UNKNOWNWORD\', \'term1\', 1], [\'IS\', \'is\', 1], [\'TEXTVAL\', \'"obama"\', 1], [\'COMMA\', \',\', 1], [\'UNKNOWNWORD\', \'term2\', 1], [\'IS\', \'is\', 1], [\'TEXTVAL\', \'"romney"\', 1]]\n', "[['TEXTLIST', 'textlist', 1], ['UNKNOWNWORD', 'filteredresult', 1]]\n", "[['FOR', 'for', 1], ['UNKNOWNWORD', 'storyitem', 1], ['UNKNOWNWORD', 'in', 1], ['UNKNOWNWORD', 'stories', 1], ['COLON', ':', 1]]\n", "[['UNKNOWNWORD', 'filteredresult', 1], ['IS', 'is', 1], ['UNKNOWNWORD', 'findtext', 1], ['UNKNOWNWORD', 'in', 1], ['UNKNOWNWORD', 'storyitem', 1], ['UNKNOWNWORD', 'with', 1], ['UNKNOWNWORD', 'term1', 1]]\n", "[['IF', 'if', 1], ['UNKNOWNWORD', 'filteredresult', 1], ['COLON', ':', 1]]\n", '[[\'UNKNOWNWORD\', \'append\', 1], [\'UNKNOWNWORD\', \'storyitem\', 1], [\'UNKNOWNWORD\', \'into\', 1], [\'TEXTVAL\', \'"example_source_programs/example4_output.txt"\', 1]]\n'])
        k.close()
        a = open("asl.twl")
        asl = a.readlines()
        a.close()
        self.assertEqual(asl, ['None\n', "[['indentlevel', 0], ['declaration', ['datatype', 'urllist'], [['stories', ['expression', ['functioncall', ['functionname', 'read'], 'arguments', [['expression', ['value', ['text', 'example_source_programs/election.txt']]]]]]]]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'text'], [['term1', ['expression', ['value', ['text', 'obama']]]], ['term2', ['expression', ['value', ['text', 'romney']]]]]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'textlist'], [['filteredresult']]]]\n", "[['indentlevel', 1], ['forstatement', ['variable', 'storyitem'], ['expression', ['variable', 'stories']]]]\n", "[['indentlevel', 1], ['assignment', ['variable', 'filteredresult'], ['expression', ['functioncall', ['functionname', 'findtext'], 'arguments', [['expression', ['insertword', 'in']], ['expression', ['variable', 'storyitem']], ['expression', ['insertword', 'with']], ['expression', ['variable', 'term1']]]]]]]\n", "[['indentlevel', 2], ['conditional', ['control', 'if'], ['boolean_list', [[['expression', ['variable', 'filteredresult']]]]]]]\n", "[['indentlevel', 2], ['expression', ['functioncall', ['functionname', 'append'], 'arguments', [['expression', ['variable', 'storyitem']], ['expression', ['insertword', 'into']], ['expression', ['value', ['text', 'example_source_programs/example4_output.txt']]]]]]]\n"])
        f = open('example_source_programs/example_program4.py')
        python = f.readlines()
        self.assertEqual(python[4:], ["stories = tfl.r_read(['example_source_programs/election.txt'])\n", "term1 = 'obama'\n", "term2 = 'romney'\n", 'filteredresult = ""\n', 'for storyitem in stories:\n', "\tfilteredresult = tfl.r_findtext(['in',storyitem,'with',term1])\n", '\tif filteredresult:\n', "\t\ttfl.r_append([storyitem,'into','example_source_programs/example4_output.txt'])\n"])
        f.close()
        
    def test_example5_program(self):
        os.system("./trowel example_source_programs/example_program5.twl")
        k = open("tokens.twl")
        tokens = k.readlines()
        self.assertEqual(tokens, ["[['COMMENT', '#find logic trowel example program 5', 1]]\n", "[['URLLIST', 'urllist', 1], ['UNKNOWNWORD', 'stories', 1], ['COMMA', ',', 1], ['UNKNOWNWORD', 'filteredresult', 1]]\n", "[['TEXTLIST', 'textlist', 1], ['UNKNOWNWORD', 'obamat', 1]]\n", '[[\'TEXT\', \'text\', 1], [\'UNKNOWNWORD\', \'term1\', 1], [\'IS\', \'is\', 1], [\'TEXTVAL\', \'"obama"\', 1], [\'COMMA\', \',\', 1], [\'UNKNOWNWORD\', \'term2\', 1], [\'IS\', \'is\', 1], [\'TEXTVAL\', \'"ireland"\', 1]]\n', '[[\'UNKNOWNWORD\', \'stories\', 1], [\'IS\', \'is\', 1], [\'UNKNOWNWORD\', \'read\', 1], [\'TEXTVAL\', \'"example_source_programs/example3.txt"\', 1]]\n', '[[\'UNKNOWNWORD\', \'filteredresult\', 1], [\'IS\', \'is\', 1], [\'UNKNOWNWORD\', \'findurl\', 1], [\'UNKNOWNWORD\', \'in\', 1], [\'UNKNOWNWORD\', \'stories\', 1], [\'UNKNOWNWORD\', \'with\', 1], [\'UNKNOWNWORD\', \'term1\', 1], [\'AND\', \'and\', 1], [\'UNKNOWNWORD\', \'term2\', 1], [\'OR\', \'or\', 1], [\'TEXTVAL\', \'"barack"\', 1]]\n', "[['IF', 'if', 1], ['LEFTPAREN', '(', 1], ['UNKNOWNWORD', 'length', 1], ['UNKNOWNWORD', 'of', 1], ['UNKNOWNWORD', 'filteredresult', 1], ['RIGHTPAREN', ')', 1], ['GREATER', '>', 1], ['NUMVAL', '10', 1], ['COLON', ':', 1]]\n", "[['FOR', 'for', 1], ['UNKNOWNWORD', 'entry', 1], ['UNKNOWNWORD', 'in', 1], ['UNKNOWNWORD', 'filteredresult', 1], ['COLON', ':', 1]]\n", '[[\'UNKNOWNWORD\', \'insert\', 1], [\'LEFTPAREN\', \'(\', 1], [\'UNKNOWNWORD\', \'findtext\', 1], [\'UNKNOWNWORD\', \'in\', 1], [\'UNKNOWNWORD\', \'entry\', 1], [\'UNKNOWNWORD\', \'with\', 1], [\'TEXTVAL\', \'"obama said"\', 1], [\'RIGHTPAREN\', \')\', 1], [\'UNKNOWNWORD\', \'into\', 1], [\'UNKNOWNWORD\', \'obamat\', 1]]\n', '[[\'UNKNOWNWORD\', \'save\', 1], [\'UNKNOWNWORD\', \'obamat\', 1], [\'UNKNOWNWORD\', \'into\', 1], [\'TEXTVAL\', \'"example_source_programs/example5_output.txt"\', 1]]\n'])
        k.close()
        a = open("asl.twl")
        asl = a.readlines()
        a.close()
        self.assertEqual(asl, ['None\n', "[['indentlevel', 0], ['declaration', ['datatype', 'urllist'], [['stories'], ['filteredresult']]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'textlist'], [['obamat']]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'text'], [['term1', ['expression', ['value', ['text', 'obama']]]], ['term2', ['expression', ['value', ['text', 'ireland']]]]]]]\n", "[['indentlevel', 0], ['assignment', ['variable', 'stories'], ['expression', ['functioncall', ['functionname', 'read'], 'arguments', [['expression', ['value', ['text', 'example_source_programs/example3.txt']]]]]]]]\n", "[['indentlevel', 0], ['assignment', ['variable', 'filteredresult'], ['expression', ['functioncall', ['functionname', 'findurl'], 'arguments', [['expression', ['insertword', 'in']], ['expression', ['variable', 'stories']], ['expression', ['insertword', 'with']], ['expression', ['variable', 'term1']], ['expression', ['insertword', 'and']], ['expression', ['variable', 'term2']], ['expression', ['insertword', 'or']], ['expression', ['value', ['text', 'barack']]]]]]]]\n", "[['indentlevel', 1], ['conditional', ['control', 'if'], ['boolean_list', [[['expression', ['functioncall', ['functionname', 'greater'], 'arguments', [['expression', ['functioncall', ['functionname', 'length'], 'arguments', [['expression', ['insertword', 'of']], ['expression', ['variable', 'filteredresult']]]]], ['expression', ['value', ['number', 10]]]]]]]]]]]\n", "[['indentlevel', 2], ['forstatement', ['variable', 'entry'], ['expression', ['variable', 'filteredresult']]]]\n", "[['indentlevel', 2], ['expression', ['functioncall', ['functionname', 'insert'], 'arguments', [['expression', ['functioncall', ['functionname', 'findtext'], 'arguments', [['expression', ['insertword', 'in']], ['expression', ['variable', 'entry']], ['expression', ['insertword', 'with']], ['expression', ['value', ['text', 'obama said']]]]]], ['expression', ['insertword', 'into']], ['expression', ['variable', 'obamat']]]]]]\n", "[['indentlevel', 0], ['expression', ['functioncall', ['functionname', 'save'], 'arguments', [['expression', ['variable', 'obamat']], ['expression', ['insertword', 'into']], ['expression', ['value', ['text', 'example_source_programs/example5_output.txt']]]]]]]\n"])
        f = open('example_source_programs/example_program5.py')
        python = f.readlines()
        self.assertEqual(python[4:], ['stories = ""\n', 'filteredresult = ""\n', 'obamat = ""\n', "term1 = 'obama'\n", "term2 = 'ireland'\n", "stories = tfl.r_read(['example_source_programs/example3.txt'])\n", "filteredresult = tfl.r_findurl(['in',stories,'with',term1,'and',term2,'or','barack'])\n", "if tfl.r_greater([tfl.r_length(['of',filteredresult]),10]):\n", '\tfor entry in filteredresult:\n', "\t\ttfl.r_insert([tfl.r_findtext(['in',entry,'with','obama said']),'into',obamat])\n", "tfl.r_save([obamat,'into','example_source_programs/example5_output.txt'])\n"])
        f.close()
    
    def test_example6_program(self):
        os.system("./trowel example_source_programs/example_program_custom_function.twl")
        k = open("tokens.twl")
        tokens = k.readlines()
        self.assertEqual(tokens, ["[['DEFINE', 'define', 1], ['UNKNOWNWORD', 'gettweets', 1], ['UNKNOWNWORD', 'of', 1], ['LEFTPAREN', '(', 1], ['TEXT', 'text', 1], ['UNKNOWNWORD', 'person', 1], ['RIGHTPAREN', ')', 1], ['UNKNOWNWORD', 'searching', 1], ['UNKNOWNWORD', 'twitter', 1], ['COLON', ':', 1]]\n", '[[\'TEXT\', \'text\', 1], [\'UNKNOWNWORD\', \'prefix\', 1], [\'IS\', \'is\', 1], [\'URLVAL\', "\'https://twitter.com/\'", 1]]\n', "[['URL', 'url', 1], ['UNKNOWNWORD', 'twitterurl', 1], ['IS', 'is', 1], ['UNKNOWNWORD', 'combine', 1], ['UNKNOWNWORD', 'prefix', 1], ['AND', 'and', 1], ['UNKNOWNWORD', 'person', 1]]\n", "[['TEXTLIST', 'textlist', 1], ['UNKNOWNWORD', 'results', 1], ['IS', 'is', 1], ['UNKNOWNWORD', 'findtext', 1], ['UNKNOWNWORD', 'in', 1], ['UNKNOWNWORD', 'twitterurl', 1]]\n", "[['RETURN', 'return', 1], ['UNKNOWNWORD', 'results', 1]]\n", '[[\'TEXTLIST\', \'textlist\', 1], [\'UNKNOWNWORD\', \'tweets\', 1], [\'IS\', \'is\', 1], [\'UNKNOWNWORD\', \'gettweets\', 1], [\'UNKNOWNWORD\', \'of\', 1], [\'TEXTVAL\', \'"barackobama"\', 1], [\'UNKNOWNWORD\', \'searching\', 1], [\'UNKNOWNWORD\', \'twitter\', 1]]\n', "[['UNKNOWNWORD', 'print', 1], ['UNKNOWNWORD', 'tweets', 1]]\n"])
        k.close()
        a = open("asl.twl")
        asl = a.readlines()
        a.close()
        self.assertEqual(asl, ["[['indentlevel', 1], ['custom', 'gettweets', ['of', ['datatype', 'text'], 'person', 'searching', 'twitter']]]\n", "[['indentlevel', 1], ['declaration', ['datatype', 'text'], [['prefix', ['expression', ['value', ['url', 'https://twitter.com/']]]]]]]\n", "[['indentlevel', 1], ['declaration', ['datatype', 'url'], [['twitterurl', ['expression', ['functioncall', ['functionname', 'combine'], 'arguments', [['expression', ['variable', 'prefix']], ['expression', ['insertword', 'and']], ['expression', ['variable', 'person']]]]]]]]]\n", "[['indentlevel', 1], ['declaration', ['datatype', 'textlist'], [['results', ['expression', ['functioncall', ['functionname', 'findtext'], 'arguments', [['expression', ['insertword', 'in']], ['expression', ['variable', 'twitterurl']]]]]]]]]\n", "[['indentlevel', 1], ['custom', 'return', ['expression', ['variable', 'results']]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'textlist'], [['tweets', ['expression', ['functioncall', ['insertword', 'gettweets'], 'arguments', [['expression', ['insertword', 'of']], ['expression', ['value', ['text', 'barackobama']]], ['expression', ['insertword', 'searching']], ['expression', ['insertword', 'twitter']]]]]]]]]\n", "[['indentlevel', 0], ['expression', ['functioncall', ['functionname', 'print'], 'arguments', [['expression', ['variable', 'tweets']]]]]]\n"])
        f = open('example_source_programs/example_program_custom_function.py')
        python = f.readlines()
        self.assertEqual(python[4:], ['def gettweets(of,person,searching,twitter):\n', "\tif not tfl.checktype(['text', 'text', 'text', 'text'],list(reversed(locals().values()))): return 'gettweets is used improperly'\n", "\tprefix = 'https://twitter.com/'\n", "\ttwitterurl = tfl.r_combine([prefix,'and',person])\n", "\tresults = tfl.r_findtext(['in',twitterurl])\n", '\treturn results\n', "tweets = gettweets('of','barackobama','searching','twitter')\n", 'tfl.r_print([tweets])\n'])
        f.close()
        
if __name__ == '__main__':
    unittest.main()
