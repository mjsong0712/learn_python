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

def allWithinRange(numbers,lower,upper):
	l = len(numbers)
	for i in range(l):
	 	if lower >= numbers[i] or numbers[i] >= upper :
	 		return False
	return True
			


print(allWithinRange([4,7,2,5,8],1,6)) # False
print(allWithinRange([4,7,2,6,2],1,8)) # True
print(allWithinRange([4,3,5,6],2,9)) # True
print(allWithinRange([4],1,5)) # True