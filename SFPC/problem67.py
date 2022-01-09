n = input().split()

n = list(map(int,n))

for i in range(len(n)):
	if n[i] % 2 == 0 and n[i] < 0:
		print("A")
	elif n[i] % 2 == 1 and n[i] < 0:
		print("B")
	elif n[i] % 2 == 0 and n[i] > 0:
		print("C")
	else:
		print("D")
		