MAX_L = 100010

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
		if self.front == -1:
			self.front = MAX_L-1
		self.L[self.front] = item

	def pop_back(self):
		tmp = self.L[self.back]
		
		self.back -= 1
		if self.back == -1:
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

	def R(self):
		T = []
		sz = self.size()
		for i in range(sz):
			T.append(self.pop_back())
		for i in range(len(T)):
			self.push_back(T[i])




	def D(self):
		self.pop_front()



D = Deque()

T = int(input())

for i in range(T):
	p = input()
	n = int(input())
	X = input()[1:-1]
	X = X.split(',')
	L = []
	k = 0
	E = False
	for j in range(n):
		D.push_back(int(X[j]))
	for j in range(len(p)):
		if p[j] == "R":
			if k == 0:
				k = 1
				
			elif k == 1:
				k = 0
				
			#k = 1-k
			#k = (k+1)%2

			
		if p[j] == "D":
			if k == 0:
				if D.size() <= 0:
					print("error")
					E = True
					break
				else:
					
					D.pop_front()	
			if k == 1:
				if D.size() <= 0:
					print("error")
					E = True
					break
				else:
					D.pop_back()

		# if p[j] == "D":
		# 	if D.size() <= 0:
		# 		print("error")
		# 		E = True
		# 		break

		# 	if k == 0:
		# 			D.pop_front()	
		# 	else:
		# 			D.pop_back()



	if k == 0:
		for j in range(D.size()):
			L.append(D.pop_front())
	else:
		for j in range(D.size()):
			L.append(D.pop_back())


	if E != True:
		L = list(map(str,L))
		print("[" + ",".join(L) + "]")