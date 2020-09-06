j = raw_input()
j = int(j)
for i in range(1, j+1):
	a,b = raw_input().split(' ')
	a = int(a)
	b = int(b)
	x = a+b
	print 'Case' + ' ' + '#' + str(i) + ':' + ' ' + str(a) + ' ' + '+' + ' ' + str(b) + ' ' + '=' + ' ' + str(x)