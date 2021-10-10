def CP(L,X,Y):
	isSame = True
	for i in range(X[0],X[1]):
		for j in range(Y[0],Y[1]):
			if L[X[0]][Y[0]] != L[i][j]:
				print(len(L), i, j)
				isSame = False
	if isSame:
		return (1,0) if L[0][0] == 1 else (0,1)


	CL1 = CP(L, (X[0] , (X[0] + X[1])//3), (Y[0] , (Y[0]+Y[1])//3))
	CL2 = CP(L, (((X[0] + X[1])//3) , ((X[0] + X[1])//3)*2), (Y[0] , (Y[0]+Y[1])//3))
	CL3 = CP(L, (((X[0] + X[1])//3)*2 , X[1]), (Y[0] , (Y[0]+Y[1])//3))
	CL4 = CP(L, (X[0] , (X[0] + X[1])//3), (((Y[0]+Y[1])//3) , (((Y[0]+Y[1])//3)*2)))
	CL5 = CP(L, (((X[0] + X[1])//3, ((X[0] + X[1])//3)*2)), (((Y[0]+Y[1])//3) , (((Y[0]+Y[1])//3)*2)))
	CL6 = CP(L, (((X[0] + X[1])//3)*2 , X[1]), (((Y[0]+Y[1])//3) , (((Y[0]+Y[1])//3)*2)))
	CL7 = CP(L, (X[0] , (X[0] + X[1])//3), ((((Y[0]+Y[1])//3)*2) , Y[1]))
	CL8 = CP(L, (((X[0] + X[1])//3) , ((X[0] + X[1])//3)*2), ((((Y[0]+Y[1])//3)*2) , Y[1]))
	CL9 = CP(L, (((X[0] + X[1])//3)*2 , X[1]), ((((Y[0]+Y[1])//3)*2) , Y[1]))

	b = CL1[0] + CL2[0] + CL3[0] + CL4[0] + CL5[0] + CL6[0] + CL7[0] + CL8[0] + CL9[0]
	w = CL1[1] + CL2[1] + CL3[1] + CL4[1] + CL5[1] + CL6[1] + CL7[1] + CL8[1] + CL9[1]
	p = CL1[2] + CL2[2] + CL3[2] + CL4[2] + CL5[2] + CL6[2] + CL7[2] + CL8[2] + CL9[2]

	return (b, w, p)
N = int(input())
L = []
for i in range(N):
	K = input().split(' ')
	L.append(K)

b, w, p = CP(L,(0,len(L[0])),(0,len(L[0])))

print(w)
print(b)
print(p)