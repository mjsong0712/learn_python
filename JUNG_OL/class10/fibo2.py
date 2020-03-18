M = {0:[1,0],
	 1:[0,1]}
def fibo(n):
	if n in M:
		return M[n]
	v1 = fibo(n-1)
	v2 = fibo(n-2)
	# a = v1[0] + v2[0]
	# b = v1[1] + v2[1]
	# M[n] = [a,b]
	# return [a,b]
	v = [v1[0] + v2[0], v1[1] + v2[1]]
	M[n] = v
	return v

N = int(raw_input())
for i in range(N):
	n1 = int(raw_input())
	V = fibo(n1)
	print str(V[0]) + ' ' + str(V[1])