N = int(input())
nge = []
a = input().split()

a = list(map(int, a))


for i in range(N):
	for j in range(i,N):
		if a[i] < a[j]:
			nge.append(a[j])
			break
		if j == N-1:
			nge.append(-1)
print(" ".join([str(a) for a in nge]))