MAX_L = 8

# push, pop, empty, size, front, back

import sys


class Queue:
	def __init__(self):
		self.L = [0 for i in range(MAX_L)]
		self.front = 0
		self.back = -1


	def push(self, item):
		self.back += 1
		if self.back == MAX_L:
			self.back = 0
		self.L[self.back] = item
	
	def pop(self):
		tmp = self.L[self.front]
		self.front += 1
		if self.front == MAX_L:
			self.front = 0
		return tmp
	
	def empty(self):
		return self.back - self.front == -1
	
	def size(self):
		if self.back >= self.front:
			return (self.back-self.front+1)
		if self.empty():
			return 0

		return (MAX_L+(self.back-self.front+1))

	def check_print(self):
		i = self.front + 1
		if i == MAX_L:
			i = 0
		while (self.	back != MAX_L-1 and i != self.back+1) or (self.back == MAX_L-1 and i != 0):
			if self.L[self.front][0] < self.L[i][0]:
				self.push(self.pop())
				return
			if self.L[self.front][0] >= self.L[i][0]:
				if i == self.back:
					return (self.pop())
					
			
			i += 1
			if i == MAX_L:
				i = 0


Q = Queue()

tc = int(input())
for i in range(tc):
	L = []
	Q.back = Q.front-1
	N, M = input().split()
	N, M = int(N), int(M)
	imp = input().split()
	l = len(imp)
	imp = list(map(int, imp))
	if imp == [imp[M] for j in range(l)]:
		print(M+1)
	else:
		for j in range(len(imp)):
			Q.push([imp[j], j])
			# Q.push({
			# 	"value":int(imp[j]),
			# 	"index":j
			# 	})

		while Q.size() >= 2:
			L.append(Q.check_print())
			print(L)
			

		L.append(Q.pop())
		L = list(filter(None, L))
		
		for j in range(len(L)):
			if L[j][1] == M:
				print(i+1)
