def CP(L):
	Y = []
	L1 = []
	L2 = []
	L3 = []
	L4 = []
	isSame = True
	for i in range(len(L[0])):
		for j in range(len(L[0])):
			if L[0][0] != L[i][j]:
				isSame = False
	if isSame:
		# return (1,0) if L[0][0] == 1 else (0,1)
		return (L[0][0],1-L[0][0])

	for i in range(len(L)//2):
		L1.append(L[i][:len(L)//2])
		L2.append(L[i][len(L)//2:])
	for i in range(len(L)//2, len(L)):
		L3.append(L[i][:len(L)//2])
		L4.append(L[i][len(L)//2:])

	CL1 = CP(L1)
	CL2 = CP(L2)
	CL3 = CP(L3)
	CL4 = CP(L4)

	b = CL1[0] + CL2[0] + CL3[0] + CL4[0]
	w = CL1[1] + CL2[1] + CL3[1] + CL4[1]

	return (b, w)


n = int(input())

L = []




for i in range(n):
	K = [int(x) for x in input().split(' ')]
	L.append(K)

b, w = CP(L)

print(w)
print(b)

