
def count(S):
	cnt = 0
	for i in range(len(S)):
		if S[i] in '369':
			cnt += 1
	return cnt


cnt = 0
n = int(raw_input())

for i in range(1,n+1):
	s = str(i)
	if '3' in s or '6' in s or '9' in s:
		cnt += count(s)

print cnt