def QT(L,A,B):
	isSame = True
	ans = ''
	for i in range(A[0],A[1]):
		for j in range(B[0],B[1]):
			if L[A[0]][B[0]] != L[i][j]:
				isSame = False

	if isSame:
		ans += L[A[0]][B[0]]

	if not isSame:
		ans += '('
		a = QT(L,(A[0],(A[0]+A[1])//2),(B[0],(B[0]+B[1])//2))
		b = QT(L,(A[0],(A[0]+A[1])//2),((B[0]+B[1])//2,B[1]))
		c = QT(L,((A[0]+A[1])//2,A[1]),(B[0],(B[0]+B[1])//2))
		d = QT(L,((A[0]+A[1])//2,A[1]),((B[0]+B[1])//2,B[1]))
		ans += a+b+c+d
		ans += ')'

	return ans

# def QT2(L,x,y):return L[x[0]][y[0]] if sum([sum([int(c) for c in l[x[0]:x[1]]]) for l in L[y[0]:y[1]]]) in (0, (x[1]-x[0])* (y[1]-y[0])) else '('+QT2(L,(x[0],(x[0]+x[1])//2),(y[0],(y[0]+y[1])//2))+QT2(L,(x[0],(x[0]+x[1])//2),((y[0]+y[1])//2,y[1]))+QT2(L,((x[0]+x[1])//2,x[1]),(y[0],(y[0]+y[1])//2))+QT2(L,((x[0]+x[1])//2,x[1]),((y[0]+y[1])//2,y[1]))+')'




n = int(input())
L = []

for i in range(n):
	a = input()

	L.append(a)

print (QT(L,(0,len(L)),(0,len(L))))
print (QT2(L,(0,len(L)),(0,len(L))))
