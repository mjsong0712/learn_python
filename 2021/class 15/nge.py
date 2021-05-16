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


N = int(input())
nge = [-1 for i in range(N)]

L = [int(i) for i in input().split()]
S = Stack()

for i in range(len(L)):
	if S.top == -1:
		S.push(i)
	else:
		if L[S.L[S.top]] > L[i]:
			S.push(i)
		if L[S.L[S.top]] < L[i]:
			# print(S.top, L[S.top], L[i])
			while not (S.top == -1 or L[S.L[S.top]] > L[i]):
				nge[S.pop()] = L[i]
				# print("pop",i)
			S.push(i)

for i in range(len(nge)):
	print(nge[i],end=' ')

# print(" ".join([str(a) for a in nge]), end = "")