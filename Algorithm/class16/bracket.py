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




def vps(brackets):
	S = Stack()
	for i in range(len(brackets)):
		if brackets[i] == "(":
			S.push(1)
		else:
			if not S.pop():
				return "NO"
	if len(S) == 0:
		return "YES"
	else:
		return "NO"


n = int(raw_input())

for i in range(n):
	inp = raw_input()
	print vps(inp)
