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

def inOrder(L):
	l = len(L)
	for i in range(l-1):
		if L[i] > L[i+1]:
			return False
	return True


print(inOrder([3,5,6,2,8])) # False
print(inOrder([2,4,6,7,9])) # True