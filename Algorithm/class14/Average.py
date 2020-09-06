L = []
s = 0
for i in range(5):
	L.append(int(raw_input()))
	if L[i] < 40:
		L[i] = 40
	s += L[i]

print s/5


s = 0
for i in range(5):
	tmp = int(raw_input())
	if tmp < 40:
		tmp = 40
	s += tmp

print s/5