D = {}

N = int(raw_input())

S, K = raw_input().split()
S, K = int(S), int(K)


P = raw_input().split()
P = list(map(int, P))

for i in range(len(P)):
	D[P[i]] = i+1



P.sort()

if S<P[0]:
	L1 = []
	L2 = P

elif P[-1]<S:
	L1 = P
	L2 = []

else:
	for i in range(1,len(P)):
		if P[i-1] < S < P[i]:
			p = i
			break

	L1 = P[:p]
	L2 = P[p:]

if L1 == []:
	for i in range(K):
		print D[L2[i]],
elif L2 == []:
	for i in range(len(L1)-1, len(L1)-1-K, -1):
		print D[L1[i]],
else:
	cnt = 0
	v1 = len(L1)-1
	v2 = 0
	while cnt < K:
		if v1 < 0:
			print D[L2[v2]],
			cnt += 1
			v2 += 1
		elif v2 >= len(L2):
			print D[L1[v1]],
			cnt += 1
			v1 -= 1
		else:
			if (S-L1[v1])**2 < (S-L2[v2])**2:
				print D[L1[v1]],
				cnt += 1
				v1 -= 1
			elif (S-L1[v1])**2 > (S-L2[v2])**2:
				print D[L2[v2]],
				cnt += 1
				v2 += 1
			else:
				print D[L1[v1]],
				cnt += 1
				v1 -= 1










