import sys
def maxinL(L):
	mx = 0
	for i in range(len(L)):
		if mx < L[i]:
			mx = L[i]
	return mx


n = int(raw_input())
S = [0 for i in range(n+1)]
F = [0 for i in range(n+1)]

for i in range(1,n+1):
	S[i] = int(raw_input())

if n == 1:
	print S[n]
	sys.exit()
elif n == 2:
	print S[n] + S[n-1]
	sys.exit()

F[n] = 0
F[n-1] = S[n]
F[n-2] = S[n-1] + S[n]
F[n-3] = maxinL([S[n-2] + S[n] , F[n-2]])

for i in range(n-4,-1,-1):

	F[i] = maxinL([S[i+1]+S[i+3]+F[i+3] ,
					S[i+2]+F[i+2] ,
					S[i+1]+S[i+2]+S[i+4]+F[i+4]])
print F[0]