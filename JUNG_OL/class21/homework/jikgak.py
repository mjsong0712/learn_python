while True:
	n = raw_input().split()
	n[0] = int(n[0])
	n[1] = int(n[1])
	n[2] = int(n[2])
	if n[0] == 0 and n[1] == 0 and n[2] == 0:
		break
	if n[0]**2 + n[1]**2 == n[2] ** 2:
		print "right"
	else:
		print "wrong"
	