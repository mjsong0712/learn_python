def radixSort(L):
	bucket = [[] for i in range(10)]
	
	
	for i in range(len(L)):
		bucket[L[i]%10].append(L[i])

	tmp_bucket = [[] for i in range(10)]
	for k in range(10):
		for l in range(len(bucket[k])):
			tmp_bucket[(bucket[k][l]/10)%10].append(bucket[k][l])

	bucket = [[] for i in range(10)]
	for k in range(10):
		for l in range(len(tmp_bucket[k])):
			bucket[(tmp_bucket[k][l]/100)%10].append(tmp_bucket[k][l])

	tmp_bucket = [[] for i in range(10)]
	for k in range(10):
		for l in range(len(bucket[k])):
			tmp_bucket[bucket[k][l]/1000].append(bucket[k][l])


	SL = []
	for k in range(10):
		for l in range(len(tmp_bucket[k])):
			SL.append(tmp_bucket[k][l])


	return SL


n = int(raw_input())
L = [0 for i in range(n)]
L2 = []

k = 0

for i in range(n):
	m = int(raw_input())
	if m == 10000:
		L2.append(10000)
	else:
		L[k]=m
		k+=1

L = L[:k]

SL = radixSort(L)+L2

for i in range(n):
	print SL[i]

