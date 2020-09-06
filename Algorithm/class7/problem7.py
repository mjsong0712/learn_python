def fibonacci(n):
	f = [0,1]
	for i in range(n+1):
		f.append(f[i] + f[i+1])
	print f[n-1]

fibonacci(10)




cnt = 0

def fibo_rec(n):
	global cnt
	cnt+=1
	if n < 2:
		return n
	return fibo_rec(n-1) + fibo_rec(n-2)



n = int(raw_input())
print fibo_rec(n)
print cnt