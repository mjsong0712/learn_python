inp = raw_input().split(' ')

A, B, V = int(inp[0]), int(inp[1]), int(inp[2])

p = float(V-A)/(A-B) + 1
if int(p) == p:
	print int(p)
else:
	print int(p)+1