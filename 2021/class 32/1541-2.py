s = input()
a = -1
ans = 0
sign = 1
for i in range(len(s)):

	if s[i] in '-+':
		ans += sign*(int(s[a+1:i]))
		a = i

	if s[i] == '-':
		sign = -1
		

ans += sign*(int(s[a+1:]))

print(ans)