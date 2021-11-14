s = input()
L = []
a = -1
c = -1
for i in range(len(s)):
	if s[i] in '-+': 
		L.append(int(s[a+1:i]))
		a = i
	if s[i] == '-' and c == -1:
		c = len(L)-1

L.append(int(s[a+1:]))




if c == -1:
	print(sum(L))
else:
	print(sum(L[:c+1]) - sum(L[c+1:]))