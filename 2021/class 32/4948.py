nL = list(range(1,1000))
pL = []
nL.remove(1)
j = 2
for i in range(1000):
	mn = min(nL)
	pL.append(mn)
	while mn*j < 1000:
		nL.remove(mn*j)
		j+=1
	nL.remove(mn)
	



# while True:
# 	n = int(input())
# 	L = list(range(n,2n+1))

print(pL)