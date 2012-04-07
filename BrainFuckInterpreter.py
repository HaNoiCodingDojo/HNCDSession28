#!/usr/bin/env python

import unittest

class BrainfuckInterpreter( object ):
	def __init__( self ):
		pass

	def run( self, program ):
		if len(program) == 0:
			return ""

		elif len(program) == 1:
			return "\0"
		else: 
			return "\0\0"


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


if __name__ == "__main__":
	unittest.main()