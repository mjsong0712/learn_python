nL = list(range(2,20000))
pL = [0 for i in range(20000)]
ind = 0

cnt= 0


while len(nL) >= 1:
	j = 2
	mn = nL[0]
	pL[ind] = mn
	ind += 1
	while mn*j <= 20000:
		if mn*j in nL:
			nL.remove(mn*j)
			cnt +=1 
		j+=1
	nL.remove(mn)
	



# while True:
# 	n = int(input())
# 	L = list(range(n,2n+1))

print(cnt)