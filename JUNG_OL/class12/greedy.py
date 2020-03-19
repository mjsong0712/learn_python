N,K = raw_input().split(' ')
K =int(K)
L = []
cnt = 0
for i in range(int(N)):
	tmp = int(raw_input())
	L.append(tmp)
	
L = L[::-1]

for i in range(len(L)):
	if K >= L[i]:
		cnt = cnt + (K / L[i])
		K = K % L[i]

print cnt