n = int(raw_input())

L1 = [1 for i in range(10)]
L2 = [1 for i in range(10)]
for i in range(n-1):
	L2[0] = L1[1]
	L2[9] = L1[8]
	for j in range(1,9):
		L2[j] = (L1[j-1] + L1[j+1]) % 1000000000

	L1 = L2[:]


print sum(L2[1:])%1000000000