N, A, B = raw_input().split()
N, A, B = int(N), int(A), int(B)
L = []
S = []

for i in range(N):
	x, y = raw_input().split()
	L.append([int(x), int(y)])

def cmpA(p1, p2):

	if p1[0] == A:
		if p2[0]<A:
			return -1
		return 1

	if p2[0] == A:
		if p1[0]>A:
			return -1
		return 1

	s1 = float(p1[1])/float(p1[0]-A)
	s2 = float(p2[1])/float(p2[0]-A)

	if s1*s2>0:
		if s1-s2<0:
			return -1
		return 1
	else:
		if s2<0:
			return -1
		return 1

def cmpB(p1,p2):

	if p1[0] == B:
		if p2[0]<B:
			return -1
		return 1

	if p2[0] == B:
		if p1[0]>B:
			return -1
		return 1


	s1 = float(p1[1])/float(p1[0]-B)
	s2 = float(p2[1])/float(p2[0]-B)

	if s1*s2>0:
		if s1-s2<0:
			return -1
		return 1
	else:
		if s2<0:
			return -1
		return 1

L.sort(cmp=cmpA)

#print L

i = 0

while True:
	if i >= len(L):
		break
	j = i+1
	while True:
		if j >= len(L):
			break
		if cmpB(L[i], L[j]) == 1:
			del L[j]
		else:
			j+=1
	i+=1
print len(L)