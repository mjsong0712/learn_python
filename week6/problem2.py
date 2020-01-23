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

def countRange(numbers, lower, upper):
	m = 0
	l = len(numbers)
	for i in range(l):
		if lower < numbers[i] < upper:
			m = m + 1
	return m

print countRange([2,4,6,8,3,3,7,9], 2, 7)
print countRange([7,9,3,6,1,2,13,8,5], 1, 8)