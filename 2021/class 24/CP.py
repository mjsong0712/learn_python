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
		if L[0][0] == '1':
			return [0,1]
		if L[0][0] == '0':
			return [1,0]


	for i in range(len(L)//2):
		L1.append(L[i][:len(L)//2])
		L2.append(L[i][len(L)//2:])
	for i in range(len(L)//2, len(L)):
		L3.append(L[i][:len(L)//2])
		L4.append(L[i][len(L)//2:])


	for i in range(len(CP(L1))):
		Y.append(CP(L1)[i])
	for i in range(len(CP(L2))):
		Y.append(CP(L2)[i])
	for i in range(len(CP(L3))):
		Y.append(CP(L3)[i])
	for i in range(len(CP(L4))):
		Y.append(CP(L4)[i])
	return Y




n = int(input())

L = []

b = 0
w = 0


for i in range(n):
	K = input().split(' ')
	L.append(K)
AL = CP(L)

for i in range(0, len(AL), 2):
	if AL[i] == 0:
		b +=1
	if AL[i] == 1:
		w +=1

print(w)
print(b)

