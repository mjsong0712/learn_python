while True:
	inp = input().split(" ")
	s = int(inp[0])
	e = int(inp[1])

	if (not 2 <= s <= 9) or (not 2 <= e <= 9): 
		print("INPUT ERROR!")
		continue
	break

for i in range(1, 10):
	if s > e:
		l = ''
		for j in range(s,e-1,-1):
			l += str(j) + ' * ' + str(i) + ' = ' + "%2i" %(i*j) + '   '
		l = l[:-3]
		print(l)

	else:
		l = ''
		for j in range(s,e+1):
			l += str(j) + ' * ' + str(i) + ' = ' + "%2i" %(i*j) + '   '
		l = l[:-3]
		print(l)