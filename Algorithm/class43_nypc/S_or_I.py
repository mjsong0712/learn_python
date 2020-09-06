def sir(L):
	L1 = L[:4]
	L2 = L[4:]
	if sum(L1) > sum(L2) and max(L1) <= max(L2):
		return "S"
	elif sum(L1) <= sum(L2) and max(L1) > max(L2):
		return "I"
	return "R"




tc = int(raw_input())

for i in range(tc):
	v = raw_input().split()
	v = list(map(int, v))
	print sir(v)