nL = [0 for i in range(250000)]
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



while True:
	cnt = 0
	n = int(input())
	if n == 0:
		break
	for i in range(len(pL)):
		if n < pL[i] and pL[i] <= 2*n:
			cnt += 1

	print(cnt)


