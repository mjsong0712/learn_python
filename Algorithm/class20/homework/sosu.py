n = int(raw_input())
L = raw_input().split()
for i in range(n):
	L[i] = int(L[i])
#L = [int(L[i]) for i in range(n)]

cnt2 = 0
for i in range(n):
	cnt1 = 0
	for j in range(2,L[i]):
		if L[i] % j == 0:
			cnt1 += 1
	if L[i] != 1 and cnt1 == 0:
		cnt2 += 1

print cnt2
