mn1 = 3000
mn2 = 3000
for i in range(3):
	n1 = int(raw_input())
	if mn1 > n1:
		mn1 = n1
for i in range(2):
	n2 = int(raw_input())
	if mn2 > n2:
		mn2 = n2
print mn1 + mn2 - 50