a = int(raw_input())
inp = raw_input().split(' ')
mx = -10000000
mn = 10000000
for i in range(a):
	if mx < int(inp[i]):
		mx = int(inp[i])
	if mn > int(inp[i]):
		mn = int(inp[i])
print mn,mx