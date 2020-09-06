N = int(raw_input())
L = [1,2]+[0]*(N-2)
for i in range(2,N):
	L[i] = (L[i-1]+L[i-2])%15746
print L[N-1]




N = int(raw_input())
L = [1,2]
for i in range(N-2):
	L.append((L[-1]+L[-2])%15746)
print L[N-1]