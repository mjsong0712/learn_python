n = int(input())
L = []
for i in range(1,n+1):
	L.append(i)

for i in range(1,n+1):
	if i % 3 == 0:
		L.remove(i)


for i in range(len(L)):
	print(L[i], end=' ')