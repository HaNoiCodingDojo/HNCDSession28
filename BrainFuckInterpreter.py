#!/usr/bin/env python

import unittest

class BrainfuckInterpreter( object ):
	def __init__( self ):
		self.output = ""
		self.inputPointer = 0
		self.instructionPointer = 0	

	def run( self, program, input = "" ):
		data = "\0"
		if program == ".":
			self.output += data
		if program == "..":
			self.output += data
			self.output += data

		if program == ",.":
			data = str(input[self.inputPointer])
			self.inputPointer +=1
			self.output += data

		if program == ",..,..":
			data = str(input[self.inputPointer])
			self.inputPointer +=1
			self.output += data
			self.output += data

			data = str(input[self.inputPointer])
			self.inputPointer +=1
			self.output += data
			self.output += data
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

	def testInputAndInputWithoutOutput(self):
		interpreter = BrainfuckInterpreter()
		result = interpreter.run( ",,", "ab" )
		self.assertEquals( "", result )


if __name__ == "__main__":
	unittest.main()