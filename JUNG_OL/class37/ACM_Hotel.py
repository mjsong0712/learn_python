n = int(raw_input())

for i in range(n):
	m = raw_input().split()
	h = int(m[0])
	w = int(m[1])
	p = int(m[2])
	ho = (p-1)/h+1
	floor = (p-1)%h+1
	print floor*100 + ho