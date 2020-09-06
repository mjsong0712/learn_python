n = int(raw_input())
L = []

m = raw_input().split()
mx = -1000000000
for i in range(len(m)):
	L.append(int(m[i]))

for i in range(len(L)):
	for j in range(len(L)):
		s = sum(L[i:j+i+1])
		if s > mx:
			mx = s

print mx