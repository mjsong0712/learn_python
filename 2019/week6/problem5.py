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

def sumOfTwoSquares(n):
	b=int(n**0.5)+1
	for i in range(1,b):
		for j in range(i+1,b):
			if i**2 + j**2 == n:
				return True
	return False

def printSOTS(n):
	for i in range(1,n+1):
		if sumOfTwoSquares(i):
			print(i)



printSOTS(100)