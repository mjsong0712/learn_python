MAX_L = 10

# push, pop, empty, size, front, back
class Queue:
	def __init__(self):
		self.L = [0 for i in range(MAX_L)]
		self.front = 0
		self.back = -1
	def push(self, a):
		self.L.append(a)
		self.back += 1
	def pop(self):
		self.L


	

		
		


Q = Stack()

Q.push(1)
Q.push(2)
Q.push(3)
Q.push(4)
print(Q.pop())
print(Q.pop())
print(Q.pop())

Q.push(5)
Q.push(6)
Q.push(7)
print(Q.pop())
print(Q.pop())
print(Q.pop())

Q.push(8)
Q.push(9)
Q.push(10)
print(Q.pop())
print(Q.pop())
print(Q.pop())

Q.push(11)
Q.push(12)
Q.push(13)
print(Q.pop())
print(Q.pop())
print(Q.pop())

