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

	def isEmpty(self):
		if self.top == -1:
			return True
		return False


def bracket(s):
	S = Stack()
	for i in range(len(s)):
		if s[i] == '(':
			S.push(s[i])
		
		if s[i] == '[':
			S.push(s[i])
		

		
		if s[i] == ')':
			# if S.L[S.top] == '(':
			# 	S.pop()
			# else:
			# 	return False
			item = S.pop()
			if not item:
				return False
			if item != "(":
				return False

		if s[i] == ']':
			item = S.pop()
			if not item:
				return False
			if item != "[":
				return False

	if not S.isEmpty():
		return True
	else:
		return False


while True:
	s = raw_input()
	if s == ".":
		break
	if bracket(s):
		print("yes")
	else:
		print("no")
		