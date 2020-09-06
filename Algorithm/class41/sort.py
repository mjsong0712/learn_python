import random, time

def selectionSort(L):
	for i in range(len(L)):
		md = i
		for j in range(i, len(L)):
			if L[j] < L[md]:
				md = j
		L[i], L[md] = L[md], L[i]
	return L



def bubbleSort(L):
	p = len(L)
	for i in range(1,len(L)):
		for j in range(1, p):
			if L[j-1] > L[j]:
				L[j-1], L[j] = L[j], L[j-1]
		p-=1
				
	return L


def insertionSort(L):
	for i in range(1, len(L)):
		for j in range(i, 0, -1):
			if L[j] < L[j-1]:
				L[j], L[j-1] = L[j-1], L[j]
	return L


def mergeSort(L):
	if len(L) == 1:
		return L
	
	L1 = L[0:len(L)/2]
	L2 = L[len(L)/2:]
	
	L1 = mergeSort(L1)
	L2 = mergeSort(L2)

	p1 = 0
	p2 = 0
	SL = []
	while p1 != len(L1) or p2 != len(L2): # len(SL) < len(L)
		if p1==len(L1):
			while p2 < len(L2):
				SL.append(L2[p2])
				p2+=1
			break
		
		if p2==len(L2):
			while p1 < len(L1):
				SL.append(L1[p1])
				p1+=1
			break
		
		if L1[p1] < L2[p2]:
			SL.append(L1[p1])
			p1+=1
		
		else:
			SL.append(L2[p2])
			p2+=1
	
	return SL



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
			bucket[tmp_bucket[k][l]/100].append(tmp_bucket[k][l])

	SL = []
	for k in range(10):
		for l in range(len(bucket[k])):
			SL.append(bucket[k][l])
	return SL



st = time.time()
for i in range(100):
	L = range(1,1000)
	random.shuffle(L)
	selectionSort(L)
print "select", time.time() - st


st = time.time()
for i in range(100):
	L = range(1,1000)
	random.shuffle(L)
	bubbleSort(L)
print "bubble", time.time() - st


st = time.time()
for i in range(100):
	L = range(1,1000)
	random.shuffle(L)
	insertionSort(L)
print "insert", time.time() - st


st = time.time()
for i in range(100):
	L = range(1,1000)
	random.shuffle(L)
	mergeSort(L)
print "merge", time.time() - st


st = time.time()
for i in range(100):
	L = range(1,1000)
	random.shuffle(L)
	quickSort(L)
print "quick", time.time() - st


st = time.time()
for i in range(100):
	L = range(1,1000)
	random.shuffle(L)
	radixSort(L)
print "radix", time.time() - st



# https://hsp1116.tistory.com/33