import random

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




L = range(10)
random.shuffle(L)
print L
print bubbleSort(L)

L = range(10)
random.shuffle(L)
print L
print insertionSort(L)


# https://hsp1116.tistory.com/33