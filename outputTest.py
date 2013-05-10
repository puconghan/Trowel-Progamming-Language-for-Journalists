import os, unittest

class TestTrowel(unittest.TestCase):
    
    def test_save_program(self):
    	print "save program being tested"
        os.system("./trowel tests/save.twl")
        os.system("python tests/save.py")
        output = open("numlist.txt").readlines()
        self.assertEqual(output, ['line 1\n', 'line 2\n', 'line 3\n'])
        os.system("rm numlist.txt")
        
    def test_helloWorld_program(self):
    	print "helloWorld program being tested"
        os.system("./trowel tests/hello.twl")
        os.system("python tests/hello.py")
        output = open("output.txt").readlines()
        self.assertEqual(output, ['Hello World!\n'])
        os.system("rm output.txt")
        
    def test_addcombine_program(self):
    	print "add and combine program being tested"
        os.system("./trowel tests/addcombine.twl")
        os.system("python tests/addcombine.py")
        output = open("output.txt").readlines()
        self.assertEqual(output, ['www.bbc.co.uk?7\n'])
        os.system("rm output.txt")
        
    def test_flighttime_program(self):
    	print "flightTime program being tested"
        os.system("./trowel tests/flighttime.twl")
        os.system("python tests/flighttime.py")
        output = open("output.txt").readlines()
        self.assertEqual(output, ['SpaceShipTwo ignites its engine in flight for the first time\n', 'Sir Richard said in a statement: "For the first time, we were able to prove the key components of the system, fully integrated and in flight. Today\'s supersonic success opens the way for a rapid expansion of the spaceship\'s powered flight envelope, with a very realistic goal of full space flight by the year\'s end." \n'])
        os.system("rm output.txt")
        
    def test_if_program(self):
    	print "if program being tested"
        os.system("./trowel tests/boom.twl")
        os.system("python tests/boom.py")
        output = open("output.txt").readlines()
        self.assertEqual(output, ['boomshakalaka\n'])
        os.system("rm output.txt")
        
if __name__ == '__main__':
    unittest.main()
