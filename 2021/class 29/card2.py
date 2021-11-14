def search(L,X,Y,n):
	if Y-X <= 0:
			return 0
	if L[(X+Y)//2] == n:
		return 1

	else:
		
		if n < L[(X+Y)//2]:
			return search(L,X,(X+Y)//2,n)
		else:
			return search(L,(X+Y)//2+1,Y,n)


def find_first(L,X,Y,n):
	if X == Y:
		return X
	if L[(X+Y)//2] > n:
		return find_first(L,X,(X+Y)//2,n)
	if L[(X+Y)//2] < n:
		return find_first(L,(X+Y)//2+1,Y,n)

	if L[(X+Y)//2] == n:
		if X == 0 and Y == 1:
			return 0
		if L[(X+Y)//2-1] != n:
			return (X+Y)//2
		else:
			return find_first(L,X,(X+Y)//2,n)

def find_end(L,X,Y,n):
	if X == Y:
		return X - 1
	if L[(X+Y)//2] > n:
		return find_end(L,X,(X+Y)//2,n)
	if L[(X+Y)//2] < n:
		return find_end(L,(X+Y)//2+1,Y,n)

	if L[(X+Y)//2] == n:
		if (X+Y)//2 == len(L)-1:
			if L[len(L)-1] != n:
				return len(L)-2
			else:
				return len(L)-1
		if L[(X+Y)//2+1] != n:
			return (X+Y)//2
		else:
			return find_end(L,(X+Y)//2,Y,n)


N = int(input())
NL = input().split(' ')
M = int(input())
ML = input().split(' ')

# NL = list(map(int, NL))
# ML = list(map(int, ML))
NL.sort()

for i in range(M):
	print(find_end(NL,0,N,ML[i]) - find_first(NL,0,N,ML[i]) + 1,end=' ')

