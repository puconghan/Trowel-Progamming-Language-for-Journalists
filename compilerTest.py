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
        self.assertEqual(python, ['#!/usr/bin/python\n', 'import trowelfunctions as tfl\n', '\n', 'x = ""\n', 'j = ""\n', '\n', 'lengthcheck = 0\n', '\n', 'z = ""\n', 'tmp0 = 6\n', 'tmp1 = 7\n', 'tmp2 = 8\n', 'tmp3 = 9\n', 'tmp4 = 10\n', 'z = [tmp0,tmp1,tmp2,tmp3,tmp4]\n', '\n', 'tmp0 = 1\n', 'tmp1 = 2\n', 'tmp2 = 3\n', 'tmp3 = 4\n', 'tmp4 = 5\n', 'x = [tmp0,tmp1,tmp2,tmp3,tmp4]\n'])
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
        self.assertEqual(python, ['#!/usr/bin/python\n', 'import trowelfunctions as tfl\n', '\n', 'tmp0 = 45\n', 'tfl.r_print([tmp0])\n'])
        f.close()
        
    def test_flighttime_program(self):
        os.system("./trowel tests/flighttime.twl")
        k = open("tokens.twl")
        tokens = k.readlines()
        self.assertEqual(tokens, ["[['TEXTLIST', 'textlist', 1], ['UNKNOWNWORD', 'flighttime', 1]]\n", '[[\'URL\', \'url\', 1], [\'UNKNOWNWORD\', \'spacearticle\', 1], [\'IS\', \'is\', 1], [\'URLVAL\', "\'http://www.bbc.co.uk/news/science-environment-22344398\'", 1]]\n', '[[\'UNKNOWNWORD\', \'flighttime\', 1], [\'IS\', \'is\', 1], [\'UNKNOWNWORD\', \'findtext\', 1], [\'UNKNOWNWORD\', \'in\', 1], [\'UNKNOWNWORD\', \'spacearticle\', 1], [\'UNKNOWNWORD\', \'with\', 1], [\'TEXTVAL\', \'"time"\', 1], [\'UNKNOWNWORD\', \'and\', 1], [\'TEXTVAL\', \'"flight"\', 1]]\n', '[[\'UNKNOWNWORD\', \'save\', 1], [\'UNKNOWNWORD\', \'flighttime\', 1], [\'UNKNOWNWORD\', \'into\', 1], [\'TEXTVAL\', \'"output.txt"\', 1]]\n'])
        k.close()
        a = open("asl.twl")
        asl = a.readlines()
        a.close()
        self.assertEqual(asl, ["[['indentlevel', 0], ['declaration', ['datatype', 'textlist'], [['flighttime']]]]\n", "[['indentlevel', 0], ['declaration', ['datatype', 'url'], [['spacearticle', ['expression', ['value', ['url', 'http://www.bbc.co.uk/news/science-environment-22344398']]]]]]]\n", "[['indentlevel', 0], ['assignment', ['variable', 'flighttime'], ['expression', ['functioncall', ['functionname', 'findtext'], 'arguments', [['expression', ['insertword', 'in']], ['expression', ['variable', 'spacearticle']], ['expression', ['insertword', 'with']], ['expression', ['value', ['text', 'time']]], ['expression', ['insertword', 'and']], ['expression', ['value', ['text', 'flight']]]]]]]]\n", "[['indentlevel', 0], ['expression', ['functioncall', ['functionname', 'save'], 'arguments', [['expression', ['variable', 'flighttime']], ['expression', ['insertword', 'into']], ['expression', ['value', ['text', 'output.txt']]]]]]]\n"])
        f = open('tests/flighttime.py')
        python = f.readlines()
        self.assertEqual(python, ['#!/usr/bin/python\n', 'import trowelfunctions as tfl\n', '\n', 'flighttime = ""\n', '\n', 'spacearticle = ""\n', "spacearticle = 'http://www.bbc.co.uk/news/science-environment-22344398'\n", '\n', "tmp0 = 'in'\n", 'tmp1 = spacearticle\n', "tmp2 = 'with'\n", "tmp3 = 'time'\n", "tmp4 = 'and'\n", "tmp5 = 'flight'\n", 'tfl.r_findtext([tmp0,tmp1,tmp2,tmp3,tmp4,tmp5])\n', 'flighttime = tfl.r_findtext([tmp0,tmp1,tmp2,tmp3,tmp4,tmp5])\n', '\n', 'tmp0 = flighttime\n', "tmp1 = 'into'\n", "tmp2 = 'output.txt'\n", 'tfl.r_save([tmp0,tmp1,tmp2])\n'])
        f.close()
        
if __name__ == '__main__':
    unittest.main()
