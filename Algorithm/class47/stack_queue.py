class Stack:
	def __init__(self):
		self.L = [0 for i in range(100001)]
		self.top = -1

	def push(self, n):
		self.L[self.top+1] = n
		self.top += 1

	def pop(self):
		item = self.L[self.top]
		self.top -= 1
		return item

	def isEmpty(self):
		if self.top == -1:
			return True
		else:
			return False

S = Stack()

n = int(raw_input())
L = [i for i in range(1,n+1)]
P = []
for i in range(n):
	p = int(raw_input())
	P.append(p)

cl = 0
cp = 0

while True:
	if cp == n:
		print "YES"
		break
	if cl == n:
		S.pop()
	if L[cl] <= P[cp]:
		while L[cl] <= P[cp]:
			S.push(L[cl])
			print L[cl], "push"
			cl+=1
		print S.pop(), "pop"
		cp+=1

	elif L[cl] > P[cp]:
		a = S.pop()
		print a
		if P[cp] != a:

			print "NO"
			break
		else:
			cp += 1


