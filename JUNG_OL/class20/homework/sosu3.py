inp = raw_input().split()
M = int(inp[0])
N = int(inp[1])
P = [2]

for i in range(3,N+1):
	#print "############"
	cnt = 0
	for j in range(len(P)):
		#print P[j], i
		if i**0.5 < P[j]:
			break
		if i%P[j]==0:
			cnt += 1
	if cnt == 0:
		P.append(i)

for i in range(len(P)):
	if M <= P[i]:
		print P[i]