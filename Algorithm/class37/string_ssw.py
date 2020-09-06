D = {"Q":0,
"W":0,
"E":0,
"R":0,
"T":0,
"Y":0,
"U":0,
"I":0,
"O":0,
"P":0,
"A":0,
"S":0,
"D":0,
"F":0,
"G":0,
"H":0,
"J":0,
"K":0,
"L":0,
"Z":0,
"X":0,
"C":0,
"V":0,
"B":0,
"N":0,
"M":0}



s = raw_input()

for c in s:
	D[c.upper()]+=1
mx = 0
for key in D:
	if mx<D[key]:
		mx = D[key]

cnt = 0
for key in D:
	if mx == D[key]:
		c = key
		cnt += 1
if cnt>1:
	print "?"
else:
	print c