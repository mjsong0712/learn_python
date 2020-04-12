mn = 100000000
mx = 0
n = raw_input().split(" ")
for i in range(3):
	if mn > int(n[i]):
		mn = int(n[i])
	if mx < int(n[i]):
		mx = int(n[i])
n = map(int,n)
print sum(n) - mx-mn