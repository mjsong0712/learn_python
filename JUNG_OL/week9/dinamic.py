F = {1:1,
	 2:1}

cnt = 0
def fibo_rec(n):
	global cnt
	cnt+=1
	if n in F:
		return F[n]
	v = fibo_rec(n-1) + fibo_rec(n-2)
	F[n] = v
	return v

print fibo_rec(1000)
print cnt