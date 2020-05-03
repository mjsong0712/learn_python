NL = raw_input().split(" ")

N1 = int(NL[0])
N2 = int(NL[1])

N1 = (N1%10 * 100) + ((N1/10)%10)*10 + N1/100
N2 = (N2%10 * 100) + ((N2/10)%10)*10 + N2/100

if N1 > N2:
	print N1
else:
	print N2
