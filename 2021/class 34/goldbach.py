T = int(input())
L = []
nL = [0 for i in range(10000)]
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



for i in range(T):
	n = int(input())
	
	k = n//2
	while k > 1:
		if k in pL and n-k in pL:
			L.append([k,n-k])
			break
		k-=1

for i in range(len(L)):
	print(str(L[i][0]),str(L[i][1]))