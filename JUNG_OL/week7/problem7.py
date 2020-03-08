def fibonacci(n):
	f = [0,1]
	for i in range(n+1):
		f.append(f[i] + f[i+1])
	print f[n-1]

fibonacci(10)






def fibo_rec(n):
	if n < 3:
		return n-1
	return fibo_rec(n-1) + fibo_rec(n-2)


print fibo_rec(3)



