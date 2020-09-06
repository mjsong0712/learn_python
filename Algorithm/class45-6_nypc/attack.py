N, A, B = raw_input().split()
N, A, B = int(N), int(A), int(B)
L = []
S = []

for i in range(N):
	x, y = raw_input().split()
	L.append([int(x), int(y)])

for i in range(N):
	g1 = float(L[i][1])/float(L[i][0]-A)
	g2 = float(L[i][1])/float(L[i][0]-B)
	S.append([g1,g2])


def cmp1(a,b):
	if a*b>0:
		if a-b<0:
			return -1
		return 1
	else:
		if b<0:
			return -1
		return 1


def cmp2(A,B):
	return cmp1(A[0],B[0])



S.sort(cmp=cmp2)

i = 0

while True:
	if i >= len(S):
		break
	j = i+1
	while True:
		if j >= len(S):
			break
		if cmp1(S[i][1], S[j][1]) == 1:
			del S[j]
		else:
			j+=1
	i+=1
print len(S)