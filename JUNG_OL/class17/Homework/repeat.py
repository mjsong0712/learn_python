n = int(raw_input())
for i in range(n):
	sn = ""
	m = raw_input().split(" ")
	m[0] = int(m[0])
	for j in range(len(m[1])):
		k = m[1]
		st = m[0] * k[j]
		sn += st
	print sn