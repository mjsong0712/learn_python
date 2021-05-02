N = int(input())
nge = []


for i in range(N):
	for j in range(i+1,N):
		if a[i] < a[j]:
			nge.append(a[j])
			break
		if j == N-1:
			nge.append(-1)
print(" ".join([str(n) for n in nge]))