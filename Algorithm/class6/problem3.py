n = int(raw_input())

if n == 1:
	print 1
else:

	for i in range(2, 20000):
		m1 = 3*i**2-9*i+8
		m2 = 3*i**2-3*i+1

		if m1 <= n <= m2:
			print i
			break