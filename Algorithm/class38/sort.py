import random

def selectionSort(L):
	md = 0
	for i in range(len(L)):
		for j in range(len(L)):
			if L[j] < L[md]:
				md = j
				L[i], L[md] = L[md], L[i]
	return L






L = range(10)
random.shuffle(L)
print L
print selectionSort(L)
print L

# https://hsp1116.tistory.com/33