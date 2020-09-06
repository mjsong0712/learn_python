class Stack:
	def __init__(self):
		self.L = [0]*100000
		self.top = -1

	def __len__(self):
		return self.top+1

	def push(self,item):
		self.top += 1
		self.L[self.top] = item

	def pop(self):
		if self.top < 0:
			return False
		item = self.L[self.top]
		self.top -= 1
		return item

v = 0
S = Stack()
n = int(raw_input())
for i in range(n):
	inp = int(raw_input())
	if inp == 0:
		S.pop()
	else:
		S.push(inp)



while True:
	s = S.pop()
	if s != False:
		v += s
	else:
		break
print v