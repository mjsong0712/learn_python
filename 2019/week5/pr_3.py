# -*- coding: utf-8 -*-
# 변수명 예시
# L, M, N
# list, number_list, numbers
# input

# 함수 사용시 f1(input), f2()
# 변수 사용시 v1 = v2 + v3

# range(5) == [0, 1, 2, 3, 4]
# [0 for i in range(5)] == [0, 0, 0, 0, 0]

def min(input) :
	l = len(input)
	L = [None for i in range(l)]
	L[0] = input[0]
	for i in range(1, l):
	 	L[i] = L[i-1] + input[i]
	return L

print min([3,1,5,2,4])