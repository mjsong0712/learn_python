MAX_L = 100010

# push, pop, empty, size, front, back

import sys

T = int(input())

for i in range(T):
	p = input()
	int(input())
	X = input()[1:-1]
	X = X.split(',') if X else []
	err_flg = 0

	indices = [0, len(X)-1]
	ind = 0
	for j in range(len(p)):

		if p[j] == "R":
			ind = (ind+1)%2
		else:
			if indices[0] > indices[1]:
				print("error")
				err_flg = 1
				break
			indices[ind] -= (ind*2 - 1)

	if not err_flg:
		if ind == 0:
			L = X[ indices[0] : indices[1]+1 ]
		else:
			X = [0]+X
			L = X[ indices[1]+1 : indices[0] : -1]

		print("[" + ",".join([str(i) for i in L]) + "]")