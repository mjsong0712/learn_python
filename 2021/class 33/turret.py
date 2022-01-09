T = int(input())

for i in range(T):
	x1,y1,r1,x2,y2,r2 = list(map(int,input().split(" ")))

	d = (((x1-x2)**2 + (y1-y2)**2) ** 0.5)

	if r1 + r2 == d:
		print(1)

	elif r1 == r2 and x1 == x2 and y1 == y2:
		print(-1)

	elif r1 + r2 > d and abs(r2-r1) < d:
		print(2)


	elif r1 + r2 < d:
		print(0)

	elif abs(r2-r1) > d:
		print(0)

	elif abs(r2-r1) == d:
		print(1)

