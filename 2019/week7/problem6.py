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

def countAlphabet(s,a):
	m = 0
	l = len(s)
	for i in range(l):
		if s[i] == a:
			m = m + 1
	return m
	#return len([for i in s if i==a])

print(countAlphabet('asvhgjfvAvvhjasvdfbmAASFaaA','v'))
print(countAlphabet('VGsAsSAsAasdaghaA','s'))