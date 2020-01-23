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

def allDistinct(numbers):
	l = len(numbers)
	for i in range(l-1):
		for j in range(i+1,l):
			if numbers[i] == numbers[j]:
				return False
	return True
			


print(allDistinct([4,7,2,5,8,9,0]))
print(allDistinct([4,7,2,6,9,2,5,8]))
print(allDistinct([4,7,2,6,9,2,5,8,1,1,1,1,1,1,1,1,1]))
print(allDistinct([4]))
print(allDistinct([]))