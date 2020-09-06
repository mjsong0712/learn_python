x = int(raw_input())
if x==1:
	print "1/1"
else:
	for i in range(10000):
		if (i**2+i)/2<x<=(i**2+3*i+2)/2:
			n = i+1
			break
	k = x-(n*(n-1)/2)

	if n%2==0:
		print str(k)+"/"+str((n+1)-k)
	else:
		print str((n+1)-k)+"/"+str(k)