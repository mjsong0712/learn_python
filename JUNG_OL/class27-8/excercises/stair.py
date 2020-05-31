import sys

n = int(raw_input())
S = [0 for i in range(n+1)]
F = [0 for i in range(n+1)]


for i in range(1,n+1):
	S[i] = (int(raw_input()))

if n == 1:
	print S[1]
	sys.exit()
elif n == 2:
	print S[1] + S[2]
	sys.exit()
F[n] = 0
F[n-1] = S[n]
F[n-2] = S[n]


for i in range(n-3,0,-1):
	F[i] = max(S[i+1] + S[i+3] + F[i+3], S[i+2] + F[i+2])

F[0] = max(F[1] + S[1], F[2] + S[2])

print F[0]