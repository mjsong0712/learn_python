
def solve(L):
	n = 0
	for i in range(len(L)):
		n += L[i]
	return n


L1 = [1,2,3,4,5]
print solve(L1)