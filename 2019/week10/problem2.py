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


def inRevOrder(s):
	l = len(s)
	# for i in range(l):
	# 	for j in range(i+1,l):
	# 		if not s[i] > s[j]:
	# 			return False
	# return True
	for i in range(l-1):
		if s[i] < s[i+1]:
			return False
	return True
	
#######################
print(inRevOrder([8,7,5,4,3,1])) # True
print(inRevOrder([9,7,6,4,7,3])) # False
print(inRevOrder([4,6,3,1,2])) # False

