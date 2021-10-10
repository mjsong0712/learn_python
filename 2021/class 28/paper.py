def CP(L,X,Y):
	isSame = True
	for i in range(X[0],X[1]):
		for j in range(Y[0],Y[1]):
			if L[X[0]][Y[0]] != L[i][j]:
				isSame = False
				break

		if not isSame:
			break


	if isSame:
		if L[X[0]][Y[0]] == '-1':
			return (1,0,0)
		if L[X[0]][Y[0]] == '0':
			return (0,1,0)
		if L[X[0]][Y[0]] == '1':
			return (0,0,1)

	n1 = (2*X[0] + X[1])//3
	n2 = (X[0] + 2*X[1])//3

	m1 = (2*Y[0]+Y[1])//3
	m2 = (Y[0]+2*Y[1])//3

	CL=[]
	
	X_indices =[(X[0] , n1), (n1 , n2), (n2 , X[1])]
	Y_indices = [(Y[0] , m1), (m1 , m2), (m2 , Y[1])]

	for x_index in X_indices:
		for y_index in Y_indices:
			CL.append(CP(L, x_index, y_index))

	m = sum([item[0] for item in CL])
	z = sum([item[1] for item in CL])
	p = sum([item[2] for item in CL])

	# sum([CL[i][0] for i in range(9)])
	# m = CL1[0] + CL2[0] + CL3[0] + CL4[0] + CL5[0] + CL6[0] + CL7[0] + CL8[0] + CL9[0]
	# z = CL1[1] + CL2[1] + CL3[1] + CL4[1] + CL5[1] + CL6[1] + CL7[1] + CL8[1] + CL9[1]
	# p = CL1[2] + CL2[2] + CL3[2] + CL4[2] + CL5[2] + CL6[2] + CL7[2] + CL8[2] + CL9[2]

	return (m, z, p)
N = int(input())
L = []
for i in range(N):
	K = input().split(' ')
	L.append(K)

m, z, p = CP(L,(0,len(L[0])),(0,len(L[0])))

print(m)
print(z)
print(p)