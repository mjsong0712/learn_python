s = input()
L = []
a = -1
for i in range(len(s)):
	if s[i] not in ['0','1','2','3','4','5','6','7','8','9']:
		 
		L.append(int(s[a+1:i]))
		a = i
L.append(int(s[a+1:]))

print(L)