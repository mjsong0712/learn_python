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


def inOrder_2(L):
	l1 = len(L)
	l2 = len(L[0])
	for i in range(l1):
		for j in range(l2-1):
			if L[i][j] > L[i][j+1]:
				return False
	for i in range(l2):
		for j in range(l1-1):
			if L[j][i] > L[j+1][i]:
				return False
	return True

######################

L1 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10,11,12],
      [13,14,15,16]]

L2 = [[1, 2, 3, 4],
      [5, 6, 9, 13],
      [9, 10,11,12],
      [13,14,15,16]]

L3 = [[1, 2, 3, 4],
      [5, 7, 9, 11],
      [9, 10,11,12],
      [13,14,15,16]]

print(inOrder_2(L1)) # True
print(inOrder_2(L2)) # False
print(inOrder_2(L3)) # True
