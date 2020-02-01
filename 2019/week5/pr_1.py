# -*- coding: utf-8 -*-
# 변수명 예시
# L, M, N
# input, number_input, numbers
# input

# 함수 사용시 f1(input), f2()
# 변수 사용시 v1 = v2 + v3

# range(5) == [0.1.2.3.4]

def sumSquares(input) :
	N = 0
	for i in input:
		N += i**2
		# print "hint",i,N
	return N

print sumSquares([3,5,4])