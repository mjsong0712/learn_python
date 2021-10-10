D = {1:1, 2:1}

def fibo(n):
	if n in D:
		return D[n]

	D[n] = fibo(n-1) + fibo(n-2)
	return D[n]


n = int(input())

print(fibo(n))