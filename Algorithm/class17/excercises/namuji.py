L = []
for i in range(10):
	n = int(raw_input())
	k = n%42
	if k not in L:
		L.append(k)
print len(L)