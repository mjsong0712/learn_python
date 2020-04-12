n = int(raw_input())
for i in range(2*n-1,1,-2):
	print " "*(n-(1+i)/2)+"*"*i
for i in range(n):
	print " "*(n-1-i) + "*"*(i*2+1)