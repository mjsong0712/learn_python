n = int(raw_input())
b=0
for i in range(n):
	p = 0
	a=i
	while a != 0:
		p = a%10+p
		a = a/10
	#print i,p
	if i + p == n:
		b+=1
		print i
		break
if b == 0:
	print 0['']