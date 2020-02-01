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

def countZero(numbers) :
	m = 0
	l = len(numbers)
	for i in range(l):
		if numbers[i] == 0:
			m = m + 1
	return m
	# return len([7 for i in numbers if i==0])


print countZero([0,4,0,-2,4,0])
print countZero([1,0,-2,4,0,0,-7,0,5])
