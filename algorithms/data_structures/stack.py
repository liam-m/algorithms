'''
Laurence Joseph Smith <Sourceless>, 2012

stack.py
A simple implementation of a stack.
'''

class StackData:
	'''Any single item of data pushed onto the stack. This object also stores the last StackData to be pushed onto the stack, and the child StackData has its own child StackData, and so on until you get to the end. '''
	def __init__(self, value=None, child=None):
		self.value = value
		self.child = child

class Stack:
	''' A container for StackData objects, tracks one StackData object which is at the top of the stack'''
	def __init__(self):
		self.top = None
		self.length = 0
	
	def push(self, value):
		'''Push an item on to the stack - if there is a self.top defined, make it the child of the new self.top '''
		if self.length == 0:
			self.top = StackData(value)
		else:
			child = self.top
			self.top = StackData(value, child)
		self.length += 1

	def pop(self):
		'''Pop an item fromt the stack - if there are no items on the stack, return None, else return the value of self.top, replacing self.top with its child.'''
		if self.length == 0:
			return None
		else:
			popped = self.top
			self.top = self.top.child
			self.length -= 1
			return popped.value
