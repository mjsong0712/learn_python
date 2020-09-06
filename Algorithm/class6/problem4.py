a, b, c = raw_input().split(' ')

n = int(int(a) / (int(c)-int(b))) + 1
if n < 0:
	n = -1

print n