def minFlight(m):
	k = 1
	k = 2*(int(m**0.5)-3)
	for i in range(k, 100000):
		if i % 2 == 0:
			if (i/2)**2< m <=(i/2)*((i/2)+1):
				return i
		else:
			if (i/2)*(i/2+1)< m <=((i/2)+1)**2:
				return i


N = int(raw_input())

for i in range(N):
	inp = raw_input().split()
	x = int(inp[0])
	y = int(inp[1])
	print minFlight(y-x)