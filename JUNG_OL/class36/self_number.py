def digit(n):
	s = 0
	while n!=0:
		s += n % 10
		n /= 10
	return s


def self_number(n):
	L = []
	for i in range(n-1,10000):
		L.append(i+digit(i))
	return L

L = self_number(2)


for i in range(1,10000):
	if i not in L:
		print i
