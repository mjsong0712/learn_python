n = int(input())

i = 1
summ = 0
while True:
	if summ >= n:
		break
	summ += i
	i+=1

print(summ)