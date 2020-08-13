# L = [i for i in range(10)]
# L = [i*2 for i in range(10)]

L = [  [chr(65+i),0] for i in range(26)]
D = dict(L)
s = raw_input().upper()


for i in range(len(s)):
	D[s[i]] += 1


cnt = 0
M = 0
for key in D:
	if D[key] > M:
		M = D[key]

for key in D:
	if D[key] == M:
		cnt += 1
		w = key

if cnt >= 2:
	print '?'
else:
	print w