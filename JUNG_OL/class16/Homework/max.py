mx = 0
a = []
for i in range(9):
	n = int(raw_input())
	a.append(n)
	if mx < n:
		mx = n
print mx
print (a.index(mx)+1)
