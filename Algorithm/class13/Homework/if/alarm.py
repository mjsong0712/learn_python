inp = raw_input().split(' ')
a = int(inp[0])
b = int(inp[1])
if 45 <= b:
	b -= 45
	print str(a)+' '+str(b)
elif 45 > b:
	if a==0:
		a=24
		a -= 1
		b = 60-(45-b)
		print str(a)+' '+str(b)
	else:
		a -= 1
		b = 60-(45-b)
		print str(a)+' '+str(b)
