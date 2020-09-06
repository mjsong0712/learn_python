n = int(raw_input())

for i in range(n):
	if n%2==0:
		print "* "*(n/2)
		print " *"*(n/2)
	else:
		print "* "*(n/2)+"*"
		print " *"*(n/2)+" "
