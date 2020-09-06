n = int(raw_input())
L = []
L2 = []

for i in range(n):
	wh = raw_input().split()
	weight = int(wh[0])
	height = int(wh[1])
	L.append([weight,height])

for i in range(len(L)):
	cnt = 0
	for j in range(len(L)):
		if L[i][0] < L[j][0] and L[i][1] < L[j][1]:
			cnt += 1
	print cnt+1,

