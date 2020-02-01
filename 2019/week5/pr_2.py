# -*- coding: utf-8 -*-
# 변수명 예시
# L, M, N
# input, number_input, numbers
# input

# 함수 사용시 f1(input), f2()
# 변수 사용시 v1 = v2 + v3

# range(5) == [0, 1, 2, 3, 4]
# [0 for i in range(5)] == [0, 0, 0, 0, 0]

def min(input) :
	# l = len(input)
	# L = [0 for i in range(l)]

	# for i in range(l):
	#  	L[i] = input[l-1-i]
	# return L
	return input[::-1]

print min([3,1,5,2,4])