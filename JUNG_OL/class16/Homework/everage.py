mx = 0
s = 0
n = int(raw_input())
m = raw_input().split(" ")
m = map(float,m)
for i in range(n):
	if mx < m[i]:
		mx = m[i]
for i in range(n):
	m[i] = m[i]/mx*100
	s += m[i]
print s/n