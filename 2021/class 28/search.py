def search(L,X,Y,n):
	if Y-X <= 0:
			return 0
	print(X,Y,L,n)
	if L[(X+Y)//2] == n:
		return 1

	else:
		
		if n < L[(X+Y)//2]:
			return search(L,X,(X+Y)//2,n)
		else:
			return search(L,(X+Y)//2+1,Y,n)


N = int(input())
A = input().split(' ')
M = int(input())
ML = input().split(' ')

A.sort()
for i in range(M):
	print(search(A,0,N,ML[i]))