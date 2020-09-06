def digit(n):
	p=0
	while n != 0:
		p = n%10+p
		n = n/10
	return p

def gen(n):
	for i in range(n):
		p = digit(i)
		if i + p == n:
			return i
	return 0

n = int(raw_input())
print gen(n)
