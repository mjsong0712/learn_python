N = raw_input()
N1 = raw_input().split(' ')
N1.sort()
M = raw_input()
M1 = raw_input().split(' ')

def binary_search(L,item):
	l=len(L)
	#print l
	if l == 0:
		return False

	if L[l/2] == item:
		return True	

	if L[l/2] > item:
		return binary_search(L[:l/2],item)
	else:
		return binary_search(L[l/2+1:],item)


for i in range(len(M1)):
	if binary_search(N1,M1[i]):
		print 1
	else:
		print 0