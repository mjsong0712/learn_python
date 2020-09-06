class Stack:
	def __init__(self):
		self.L = []
		self.top = -1
	def push(self,item):
		self.L.append(item)
		self.top += 1
		# top += 1
		# self.L[top] = item
	def pop(self):
		if self.top < 0:
			return False
		item = self.L.pop()
		self.top -= 1
		
		return item
		# item = self.L[top]
		# top -= 1
		# return item



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
print S.pop()
print S.L
print S.pop()