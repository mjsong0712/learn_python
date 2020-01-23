# -*- coding: utf-8 -*-
# 변수명 예시
# L, M, N
# list, number_list, numbers
# input

# 함수 사용시 f1(input), f2()
# 변수 사용시 v1 = v2 + v3

# range(5) == [0, 1, 2, 3, 4]
# [0 for i in range(5)] == [0, 0, 0, 0, 0]

# m = m + 1 <=> m += 1 

# a<c and c<b <=> a<c<b

# 바꾸기: a,b = b,a

# 리스트 원소 추가 L.append(a)

# L.sort()

# L = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9,10,11,12]]
# len(L) == 3
# L[0] == [1,2,3,4]
# L[0][0] == 1
# len(L[0]) == 4

# 입력: a = raw_input("enter input")

# a in B: boolean(True/False)
# var in [1, 2, 3]
class calculator:
	def __init__(self):
		self.value = 0

	def prnt(self):
		print ("value: " +str(self.value))

	def add(self, c):
		self.value += c
		self.prnt()

	def sub(self, c):
		self.value -= c
		self.prnt()

	def mult(self, c):
		self.value *= c
		self.prnt()
	def div(self, c):
		self.value /= c
		self.prnt()



a = calculator()

a.add(2)
a.add(4)
a.sub(2)
a.add(2)
a.mult(2)
a.div(3)