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

# 입력: a = raw_input("enter input")

# a in B: boolean(True/False)
# var in [1, 2, 3]

n = 0
a = raw_input("input: ")
if a not in [str(i) for i in range(10)]:
	exit()

n = int(a)
print a

while True:
	a = raw_input("input: ")
	m = input("input: ")
	if a == '+':
		n += m 
	if a == '-':
		n -= m
	if a == '*':
		n *= m
	if a == '/':
		n /= m
	print n
