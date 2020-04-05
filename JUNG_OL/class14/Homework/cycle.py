n = int(raw_input())
cycle_tmp = n
cnt = 0
while True:
	dgt_1 = cycle_tmp%10
	digit = dgt_1 + cycle_tmp/10
	cycle_tmp = dgt_1*10 + digit%10
	cnt += 1
	if cycle_tmp == n:
		break

print cnt





a = raw_input()
a = int(a)
a1 = a
b = 0

while True:
	k1 = a1%10
	k2 = a1/10
	k3 = k1 + k2
	k3 = k3%10
	a1= k1*10 + k3
	b += 1
	if a1 == a:
		break
print b