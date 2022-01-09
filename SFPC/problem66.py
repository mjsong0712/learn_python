n = input().split()

n = list(map(int,n))

for i in range(len(n)):
	if n[i] % 2 == 0:
		print("even")
	else:
		print("odd")