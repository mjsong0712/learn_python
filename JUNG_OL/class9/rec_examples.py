def suum(n):
	if n == 1:
		return 1
	return suum(n-1) + n

print suum(5)
print "################"


def h(n):
	if n<10:
		print n
	else:
		h(n/10)
		print n % 10

h(3408)
print "################"


def maxVal(L):
	if len(L) == 1:
		return L[0]
	a = maxVal(L[:-1])
	if a < L[-1]:
		return L[-1]
	else:
		return a

print maxVal([4,11,5,7,8])
print "################"


	