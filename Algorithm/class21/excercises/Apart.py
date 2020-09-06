L = [[0 for i in range(15)] for i in range(15)]

for k in range(15):
	L[0][k]=k
	L[k][1]=1

for i in range(1,15):
	for j in range(2,15):
		L[i][j] = L[i][j-1]+L[i-1][j]

tc = int(raw_input())

for i in range(tc):
	N = int(raw_input())
	N2 = int(raw_input())
	print L[N][N2]
