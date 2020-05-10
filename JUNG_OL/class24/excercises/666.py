def six(number):
	cnt = 0
	while number != 0:
		if number % 10 == 6:
			cnt += 1
		else:
			cnt = 0
		if cnt == 3:
			return True
		number /= 10
	return False


n = int(raw_input())

m = 665
while n:
	m+=1
	if six(m):
		n -= 1

print m

# m = 0
# for i in range(666,6670000):
# 	if six(i):
# 		m += 1
# 	if m == n:
# 		print i
# 		break