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
class person:
	def __init__(self,height,weight,score):
		self.height = height
		self.weight = weight
		self.score = score
	def bmi(self):
		return self.weight/(self.height/100.0)**2


p1=person(145, 45, 1)
p2=person(156, 47, 1)
p3=person(178, 50, 1)
p4=person(181, 49, 1)
L = [p1, p2, p3, p4]




def horder(L1):
	l = len(L1)
	for i in range(l-1):
		if L1[i].height > L1[i+1].height:
			return False
	return True

def worder(L2):
	l = len(L2)
	for i in range(l-1):
		if L2[i].weight > L2[i+1].weight:
			return False
	return True

def border(L3):
	l = len(L3)
	for i in range(l-1):
		if L3[i].bmi() > L3[i+1].bmi():
			return False
	return True


print horder(L)
print worder(L)
print border(L)
