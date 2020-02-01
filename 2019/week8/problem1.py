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

def triangle(n):
	m = 0
	for i in range(1,n-1):
		for j in range(1,n-i):
			if max(n-i-j,i,j) < n/2.0:
				m += 1
	return m


print(triangle(5)) #
print(triangle(7)) #
print(triangle(9)) #
