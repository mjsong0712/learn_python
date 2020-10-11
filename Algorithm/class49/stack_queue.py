import sys
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



def Pmaker(n, P):
	PM = []
	S = Stack()
	L = [i for i in range(1,n+1)]
	
	cl = 0
	cp = 0

	while True:
		if cp == n:
			return PM

		if cl == n:
			while cp != len(P):
				if S.pop() == P[cp]:
					PM.append("-")
					cp+=1
				else:
					return False
			return PM

		if L[cl] <= P[cp]:
			while (cl < n) and (L[cl] <= P[cp]):
				S.push(L[cl])
				PM.append("+")
				cl+=1
			
			S.pop()
			PM.append("-")
			cp+=1

		elif L[cl] > P[cp]:
			a = S.pop()
			PM.append("-")
			if P[cp] != a:
				return False
			else:
				cp += 1



n = int(raw_input())
P = []
for i in range(n):
	p = int(raw_input())
	P.append(p)


res = Pmaker(n,P)

if res:
	for c in res:
		print c
else:
	print "NO"


