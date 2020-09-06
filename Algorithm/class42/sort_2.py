import random
def quickSort(L):
	if len(L) <= 1:
		return L

	pivot = L[0]
	L1 = []
	L2 = []
	for i in range(1, len(L)):
		if pivot > L[i]:
			L1.append(L[i])
		else:
			L2.append(L[i])
	L1 = quickSort(L1)
	L2 = quickSort(L2)
	return L1+[pivot]+L2


n = int(raw_input())
L = []
# for i in range(n):
# 	m = int(raw_input())
# 	L.append(m)


L = range(1000000)
random.shuffle(L)

# for i in range(len(L)):
# 	print SL[i]

