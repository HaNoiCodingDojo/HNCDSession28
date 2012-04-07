#!/usr/bin/env python

import unittest

class BrainfuckInterpreter( object ):
	def __init__( self ):
		pass

	def run( self, program ):
		return ""

class BrainfuckInterpreterTest(unittest.TestCase):

	def testTruth(self):
		self.assertEquals(True,True)

	def testEmptyProgram(self):
		interpreter = BrainfuckInterpreter()
		result = interpreter.run( "" )
		self.assertEquals( "", result )

if __name__ == "__main__":
	unittest.main()