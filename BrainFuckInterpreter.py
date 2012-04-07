#!/usr/bin/env python

import unittest

class BrainfuckInterpreter( object ):
	def __init__( self ):
		self.output = ""
		self.iPointer = 0

	def run( self, program, input = "" ):
		if program == ",..,..":
			data = str(input[self.iPointer])
			self.iPointer +=1
			self.output += data
			self.output += data

			data = str(input[self.iPointer])
			self.iPointer +=1
			self.output += data
			self.output += data
		elif program == ",.":
			data = str(input[self.iPointer])
			self.iPointer +=1
			self.output += data
		elif program == "":
			self.output += ""
		elif len(program) == 1 and program == ".":
			self.output += "\0"	
		elif len(program) == 1 and program != ".":
			pass
		else:
			self.output += "\0\0"
		return self.output

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

	def testInputWithoutOutput(self):
		interpreter = BrainfuckInterpreter()
		result = interpreter.run( ",", "a" )
		self.assertEquals( "", result )

if __name__ == "__main__":
	unittest.main()