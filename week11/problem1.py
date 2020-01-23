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

inp = raw_input().split(" ")

def is_sqr(n):
	return int(n**0.5)**2 == n
		

def sqr_nono(mn,mx):
	c = 0
	for i in range(mn,mx+1):
		m = False
		for j in range(2,i+1):
			if is_sqr(j):
				if i % j == 0:
					m = True
		if not m:
			c += 1
	return c
			
print(sqr_nono(int(inp[0]), int(inp[1])))


	
#######################
#print(sqr_nono(1,10)) # 7
