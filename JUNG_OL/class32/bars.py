S = []
n = int(raw_input())
N = [0 for i in range(n)]
for i in range(n):
	m = int(raw_input())
	N[i] = m


cnt = 1

s = N[n-1]

for i in range(len(N)-1,-1,-1):
	if N[i] > s:
		s = N[i]

		cnt += 1
#print S
print cnt