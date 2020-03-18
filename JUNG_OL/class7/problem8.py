def pac(n):
	if n == 0:
		return 1
	return n * pac(n-1)

N = int(raw_input())
print((pac(N)))