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


	def left(self):
		self.push_back(self.pop_front())
	

	def right(self):
		self.push_front(self.pop_back())

D = Deque()

N, M = input().split()
R = input().split()
N, M = int(N), int(M)
R = list(map(int, R))
L = []
k = 0

for i in range(N):
	D.push_back(i+1)

for i in range(len(R)):
	cnt = 0
	while not R[i] == D.L[D.front]:
		D.left()
		cnt += 1
	if cnt >= D.size()/2:
		k += D.size()-cnt
	else:
		k += cnt
	L.append(D.pop_front())

print(k)