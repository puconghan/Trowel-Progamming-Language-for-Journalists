import os, unittest

class TestTrowel(unittest.TestCase):
    
    def test_save_program(self):
    	print "save program output being tested"
        os.system("./trowel tests/save.twl")
        output = open("numlist.txt").readlines()
        self.assertEqual(output, ['line 1\n', 'line 2\n', 'line 3\n'])
        os.system("rm numlist.txt")
        
    def test_helloWorld_program(self):
    	print "helloWorld program output being tested"
        os.system("./trowel tests/hello.twl")
        output = open("output.txt").readlines()
        self.assertEqual(output, ['Hello World!\n'])
        os.system("rm output.txt")
        
    def test_addcombine_program(self):
    	print "add and combine program ouput being tested"
        os.system("./trowel tests/addcombine.twl")
        output = open("output.txt").readlines()
        self.assertEqual(output, ['www.bbc.co.uk?7\n'])
        os.system("rm output.txt")
        
    def test_flighttime_program(self):
    	print "flightTime program output being tested"
        os.system("./trowel tests/flighttime.twl")
        output = open("output.txt").readlines()
        self.assertEqual(output, ['SpaceShipTwo ignites its engine in flight for the first time\n', 'Sir Richard said in a statement: "For the first time, we were able to prove the key components of the system, fully integrated and in flight. Today\'s supersonic success opens the way for a rapid expansion of the spaceship\'s powered flight envelope, with a very realistic goal of full space flight by the year\'s end." \n'])
        os.system("rm output.txt")
        
    def test_if_program(self):
    	print "if program output being tested"
        os.system("./trowel tests/if.twl")
        output = open("output.txt").readlines()
        self.assertEqual(output, ['boomshakalaka\n'])
        os.system("rm output.txt")
        
    def test_example3_program(self):
    	print "Example program 3 out being tested"
        os.system("./trowel example_source_programs/example_program3.twl")
        output = open("example_source_programs/example3_output.txt").readlines()
        self.assertEqual(output, ['http://www.bbc.co.uk/news/uk-northern-ireland-21855357\n'])
        os.system("example_source_programs/example3_output.txt")
        
if __name__ == '__main__':
    unittest.main()
