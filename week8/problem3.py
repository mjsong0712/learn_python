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


def countmines(F):
	l1 = len(F)
	l2 = len(F[0])
	mine = [[0 for i in range(l2)] for i in range(l1)]
	for i in range(l1):
		for j in range(l2): # 가로 j, 세로 i 번째 블록
			for m in (-1,0,1):
				for n in (-1,0,1): 
					if 0<=i+n<l1 and 0<=j+m<l2:
						if F[i+n][j+m]:
							mine[i][j]+=1
			
	return mine


######################
T,F = True, False
field = [
	[T,F,F,F,F,T],
    [F,F,F,F,F,T],
    [T,T,F,T,F,T],
    [T,F,F,F,F,F],
    [F,F,T,F,F,F],
    [F,F,F,F,F,F]]


Map = countmines(field)

for i in Map:
	print(i)