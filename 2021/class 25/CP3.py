def CP(L,X,Y):
	isSame = True
	for i in range(X[0],X[1]):
		for j in range(Y[0],Y[1]):
			if L[X[0]][Y[0]] != L[i][j]:
				isSame = False
	if isSame:
		# return (1,0) if L[0][0] == 1 else (0,1)
		return (L[X[0]][Y[0]],1-L[X[0]][Y[0]])



	CL1 = CP(L, (X[0] , (X[0] + X[1])//2), (Y[0] , (Y[0]+Y[1])//2))
	CL2 = CP(L,( (X[0] + X[1]) // 2 , X[1]) , (Y[0] , (Y[0]+Y[1])//2))
	CL3 = CP(L,(X[0],(X[0] + X[1])//2), ((Y[0]+Y[1])//2,Y[1]))
	CL4 = CP(L,((X[0] + X[1]) // 2 , X[1]),((Y[0]+Y[1])//2,Y[1]))

	b = CL1[0] + CL2[0] + CL3[0] + CL4[0]
	w = CL1[1] + CL2[1] + CL3[1] + CL4[1]

	return (b, w)


n = int(input())

L = []




for i in range(n):
	K = [int(x) for x in input().split(' ')]
	L.append(K)

b, w = CP(L,(0,len(L[0])),(0,len(L[0])))

print(w)
print(b)

