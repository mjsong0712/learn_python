inp = raw_input().split(' ')
N = int(inp[0])
M = int(inp[1])
deck = raw_input().split(' ')
for i in range(len(deck)):
	deck[i] = int(deck[i])
#deck = [int(deck[i]) for i in range(len(deck))]
mx = 0
for i in range(N-2):
	for j in range(i+1,N-1):
		for k in range(j+1,N):
			sm = deck[i] + deck[j] + deck[k]
			if mx < sm <= M:
				mx = sm
print mx