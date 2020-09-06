import sys
n = int(raw_input())

G = [0 for i in range(n+1)]
F = [0 for i in range(n+1)]

for i in range(1,n+1):
	m = int(raw_input())
	G[i] = m

F[n] = 0
F[n-1] = G[n]
F[n-2] = max(G[n-1], G[n])
F[n-3] = max(G[n-2] + G[n], G[n-1] + G[n])

if n == 1:
	print G[1]
	sys.exit()
	
elif n == 2:
	print G[1]+G[2]
	sys.exit()

for k in range(n-4,0,-1):
	F[k] = max(G[k+1] + G[k+3] + F[k+3],
		       G[k+1] + G[k+4] + F[k+4],
		       G[k+2] + F[k+2])

print max(G[1]+F[1], G[2]+F[2])