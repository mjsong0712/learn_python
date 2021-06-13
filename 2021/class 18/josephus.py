MAX_L = 1001

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

	def ret_front(self):
		if self.empty():
			return -1
		return self.L[self.front]


	def ret_back(self):
		if self.empty():
			return -1
		return self.L[self.back]


N, K = input().split()
N, K = int(N), int(K)
ans = []
Q = Queue()

for i in range(N):
	Q.push(i+1)

while not Q.empty():
	