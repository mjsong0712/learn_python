
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
	mini = 10000
	for a in input:
		if a < mini:
			mini = a
	return mini
print min([3,1,5,2,3,5,2,6])
print min([3,1,5,2,3])
