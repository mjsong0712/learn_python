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


def count1(L):
	m = 0
	l1 = len(L)
	l2 = len(L[0])
	for i in range(l1):
		for j in range(l2):
			if L[i][j] == 1:
				m += 1
	return m

	
#######################
print(count1([[1,3,7,1,5],
			 [2,4,5,7,2],
			 [2,4,5,7,2]])) # 2
print(count1([[1,3,7,1,5],
			 [2,4,5,1,2],
			 [1,4,5,7,2]])) # 4
print(count1([[1,3,7,1,5],
			 [2,4,1,7,2],
			 [2,4,1,7,2]])) # 4

