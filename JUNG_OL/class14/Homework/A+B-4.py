while True:
	try:
		a,b = raw_input().split(' ')
		a = int(a)
		b = int(b)
		print a+b	
	except EOFError:
		break