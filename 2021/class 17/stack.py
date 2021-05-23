class Stack:
	def __init__(self):
		self.L = []
		self.top = -1
	def push(self,obj):
		self.L.append(obj)
		self.top += 1
		return self.L
	def pop(self):
		a = self.L[self.top]
		del self.L[self.top]
		self.top -= 1
		return a
		
		


S = Stack()

S.push(2)
S.push(3)
S.push(4)
print (S.pop())
print (S.pop())

