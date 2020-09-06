n=int(raw_input())

for i in range(n):
	tc=raw_input().split(" ")
	H = int(tc[0])
	W = int(tc[1])
	N = int(tc[2])
	
	if N/H+1 >= 10:
		mid = ""
	else:
		mid = "0"

	if N%H == 0:
		print str(H) + mid + str(N/H)
	else:
		print str(N%H) + mid + str(N/H+1)