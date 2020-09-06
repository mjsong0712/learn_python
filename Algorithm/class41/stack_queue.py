class Stack:
	def __init__(self):
		self.L = [0 for i in range(101)]
		self.top = -1

	def pop(self):
		if self.top==-1:
			return False
		self.top-=1
		return self.L[self.top+1]

	def push(self, p):
		self.L[self.top+1] = p
		self.top += 1



while True:
	s = raw_input()
	g = Stack()
	if s == ".":
		break
	for i in range(len(s)):
		if s[i] == "("or"[":
			g.push(s[i])



