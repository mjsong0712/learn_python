MAX_L = 10001

# push, pop, empty, size, front, back

import sys


class Deque:
	def __init__(self):
		self.L = [0 for i in range(MAX_L)]
		self.front = 0
		self.back = -1


	def push_back(self, item):
		self.back += 1
		if self.back == MAX_L:
			self.back = 0
		self.L[self.back] = item
	
	def push_front(self, item):
		self.front -= 1
		if self.front == 0:
			self.front = MAX_L-1
		self.L[self.front] = item

	def pop_back(self):
		tmp = self.L[self.back]
		self.back -= 1
		if self.back == 0:
			self.back = MAX_L-1
		return tmp

	def pop_front(self):
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



D = Deque()

N = int(input())

for i in range(N):
	cmd = input().split()
	a = cmd[0]
	if len(cmd) == 2:
		b = cmd[1]
	if a == "push_back":
		D.push_back(b)
	if a == "push_front":
		D.push_front(b)
	if a == "pop_back":
		if D.empty():
			print("-1")
		else:
			print(D.pop_back())
	if a == "pop_front":
		if D.empty():
			print("-1")
		else:
			print(D.pop_front())
	if a == "front":
		if D.empty():
			print("-1")
		else:
			print(D.L[D.front])
	if a == "back":
		if D.empty():
			print("-1")
		else:
			print(D.L[D.back])
	if a == "empty":
		print(int(D.empty()))
	if a == "size":
		print(D.size())