MAX_L = 2000001

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


	

		
		


Q = Queue()

n = int(input())

for i in range(n):
	p = sys.stdin.readline().split()
	if p[0] == "push":
		Q.push(p[1])
	if p[0] == "front":
		print(Q.ret_front())
	if p[0] == "back":
		print(Q.ret_back())
	if p[0] == "size":
		print(Q.size())
	if p[0] == "empty":
		if Q.empty():
			print(1)
		else:
			print(0)
	if p[0] == "pop":
		if Q.empty():
			print(-1)
		else:
			print(Q.pop())
