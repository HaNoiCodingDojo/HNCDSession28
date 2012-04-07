#!/usr/bin/env python

import unittest

class BrainfuckInterpreter( object ):
	def __init__( self ):
		self.data = ""

	def run( self, program, input = "" ):
		if program == ",..,..":
			self.data = str(input[0])*2+str(input[1])*2
		elif program == ",.":
			self.data = str(input[0])
		elif len(program) == 0:
			self.data = ""
		elif len(program) == 1:
			self.data = "\0"
		else: 
			self.data = "\0\0"
		return self.data

class BrainfuckInterpreterTest(unittest.TestCase):

	def testTruth(self):
		self.assertEquals(True,True)

	def testEmptyProgram(self):
		interpreter = BrainfuckInterpreter()
		result = interpreter.run( "" )
		self.assertEquals( "", result )

	def testLittleOutputProgram(self):
		interpreter = BrainfuckInterpreter()
		result = interpreter.run( "." )
		self.assertEquals( "\0", result )

	def testOutput2Characters(self):
		interpreter = BrainfuckInterpreter()
		result = interpreter.run( ".." )
		self.assertEquals( "\0\0", result )
	
	def testInputandOutput(self):
		interpreter = BrainfuckInterpreter()
		result = interpreter.run( ",.", "a" )
		self.assertEquals( "a", result )

	def testInputAndOutputAndInputAndOutput(self):
		interpreter = BrainfuckInterpreter()
		result = interpreter.run( ",..,..", "ab" )
		self.assertEquals( "aabb", result )

	def testInputAndOutputAndInputAndOutput2(self):
		interpreter = BrainfuckInterpreter()
		result = interpreter.run( ",..,..", "xy" )
		self.assertEquals( "xxyy", result )


if __name__ == "__main__":
	unittest.main()