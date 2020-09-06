def bubbleSort(L):
	l = len(L)
	for i in range(l-1):
		for j in range(l-i-1):
			if L[j] > L[j+1]:
				tmp = L[j]
				L[j] = L[j+1]
				L[j+1] = tmp
	return L

tc = int(raw_input())
L = []
for i in range(tc):
	n = int(raw_input())
	L.append(n)



for item in bubbleSort(L):
	print item