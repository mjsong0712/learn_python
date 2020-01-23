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

def deleteThree(L):
	N = []
	l = len(L)
	for i in range(l):
		if L[i] != 3:
			N.append(L[i])
	return N

print(deleteThree([3,5,6,8,3,3,2,5,3]))
print(deleteThree([3,3,3,3,3]))
print(deleteThree([3,5,2,1,5,3,3,2,5,3]))