MAX_L = 101

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
		i = self.front+1
		if i == MAX_L:
			i = 0
		while i < self.back:
			if self.L[self.front] < self.L[i]:
				self.push(self.pop())
				break
				
			if self.L[self.front] >= self.L[i]:
				print(self.pop())
			i += 1




Q = Queue()

tc = int(input())

for i in range(tc):
	Q.back = Q.front-1
	N, M = input().split()
	imp = input().split()
	for j in range(len(imp)):
		Q.push(imp[j])
		Q.check_print()