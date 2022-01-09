nL = [0 for i in range(1000000)]
nL[0] = 1
nL[1] = 1


for i in range(2, len(nL)):
	if(nL[i]) == 0:
		for j in range(2, len(nL)):
			if(i * j >= len(nL)):
				break
			nL[i*j] = 1

pL = []


for i in range(len(nL)):
	if(nL[i]) == 0:
		pL.append(i)


M, N = input().split(" ")

M = int(M)
N = int(N)

for i in range(len(pL)):
	if M <= pL[i] and pL[i] <= N:
		print(pL[i])