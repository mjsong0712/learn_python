class Stack:
	def __init__(self):
		self.L = [0]*10
		self.top = -1
	def push(self,item):
		self.top += 1
		self.L[self.top] = item
	def pop(self):
		if self.top < 0:
			return False
		item = self.L[self.top]
		self.top -= 1
		return item



S = Stack()
S.push(1)
print S.L
S.push(2)
print S.L
S.push(3)
print S.L
print S.pop()
print S.L
print S.pop()
print S.L
S.push(4)
print S.L
S.push(5)
print S.L
