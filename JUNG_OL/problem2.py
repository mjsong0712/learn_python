N = int(raw_input())
n = 0

for i in range(5):
	if (N -i*3) % 5 == 0:
		n = i
		n2 = (N - i*3) / 5

if N in [1,2,4,7]:
	print -1
else:	
	print n + n2