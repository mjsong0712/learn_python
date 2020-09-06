inp = raw_input().split()
M = int(inp[0])
N = int(inp[1])

P = [2]

L = [i for i in range(M, N+1)]
if 1 in L:
	L.remove(1)

for i in range(2, int(N**0.5)+1):
	for j in L:
		if j%i==0 and j!=i:
			L.remove(j)
print len(L)