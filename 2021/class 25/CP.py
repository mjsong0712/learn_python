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
			return 'b'
		if L[0][0] == '0':
			return 'w'


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

	for i in range(len(CL1)):
		Y.append(CL1[i])

	for i in range(len(CL2)):
		Y.append(CL2[i])
	
	for i in range(len(CL3)):
		Y.append(CL3[i])
	
	for i in range(len(CL4)):
		Y.append(CL4[i])
	
	return Y




n = int(input())

L = []

b = 0
w = 0


for i in range(n):
	K = input().split(' ')
	L.append(K)
AL = CP(L)


# for i in range(0, len(AL), 2):
# 	if AL[i] == 0:
# 		b +=1
# 	if AL[i] == 1:
# 		w +=1

for i in range(len(AL)):
	if AL[i] == 'b':
		b +=1
	if AL[i] == 'w':
		w +=1

print(w)
print(b)

