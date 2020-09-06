D = {}

N = int(raw_input())

S, K = raw_input().split()
S, K = int(S), int(K)

def num(x,y):
	if (S-x)**2 < (S-y)**2:
		return -1
	
	if (S-x)**2 > (S-y)**2:
		return 1

	if x < y:
		return -1
	return 1


P = raw_input().split()
P = list(map(int, P))
for i in range(len(P)):
	D[P[i]] = i

P.sort(cmp=num)
for i in range(K):
	print D[P[i]]+1,