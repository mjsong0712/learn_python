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



S = Stack()

n = int(raw_input())
for i in range(n):
	cmd = raw_input()
	if "push" in cmd:
		#cmd <- "push 1"
		tmp = cmd.split(" ")
		S.push(tmp[1])

	if "pop" in cmd:
		item = S.pop()
		if item:
			print item
		else:
			print -1

	if "size" in cmd:
		print len(S)

	if "empty" in cmd:
		if S.top == -1:
			print 1
		elif S.top >= 0:
			print 0
	
	if "top" in cmd:
		if S.top == -1:
			print -1
		else:
			print S.L[S.top]

