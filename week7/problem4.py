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

def compare(L1, L2):
	L1.sort()
	L2.sort()
	l = len(L1)
	for i in range(l):
		if L1[i] != L2[i]:
			return False
	return True

print(compare([8,1,5,2], [1,2,5,8]))
print(compare([2,8,4,6,3,5],[4,2,3,7,8,5]))