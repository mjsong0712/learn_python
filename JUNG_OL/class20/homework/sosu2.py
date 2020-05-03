N = int(raw_input())
M = int(raw_input())
L = []

for i in range(N, M+1):
	cnt = 0
	for j in range(1, i+1):
		if i % j == 0:
			cnt += 1
	if cnt == 2:
		L.append(i)
if len(L) != 0:
	print(sum(L))
	print(L[0])
else:
	print('-1')
	