xL = []
yL = []
n = raw_input().split()
for i in range(3):
		x, y = map(int, n)
		xL.append(x)
		yL.append(y)
for i in range(3):
		if xL.count(xL[i]) == 1:
				x = xL[i]
		if yL.count(yL[i]) == 1:
				y = yL[i]
print(x, y)