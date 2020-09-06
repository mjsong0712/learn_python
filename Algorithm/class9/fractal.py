import math

def concat(S1,S2,S3):
	l = []
	for i in range(len(S1)):
		l.append(S1[i] + S2[i] + S3[i])
	return l

def fractal(n):
	if n == 0:
		 return ["*"]
	pre = fractal(n-1)
	l = len(pre)
	e = [' '*l]*l
	L = []
	return concat(pre, pre, pre)+concat(pre, e, pre)+concat(pre, pre, pre)


N = int(raw_input())

k = fractal(int(math.log(N, 3)+0.1))
#print int(math.log(N, 3))
for i in range(len(k)):
	print k[i]