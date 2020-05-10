n = raw_input().split()
raw = int(n[0])
col = int(n[1])
S = ["W", "B"]
L = []
sgn = 0
mn = 64

for i in range(raw):
	L.append(raw_input())
	

for i in range(raw-7):
	for j in range(col-7):

		for sgn in (0,1):
			cnt = 0
			for k in range(8):
				for l in range(8):
					if S[(k+l+sgn)%2] != L[i+k][j+l]:
						cnt += 1
			if mn > cnt:
				mn = cnt
print mn