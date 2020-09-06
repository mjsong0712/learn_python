s = raw_input()
cursor = 0
for i in range(len(s)):
	if s[i] == "S":
		cursor += 1
	if s[i] == "T":
		cursor = 4*(cursor/4+1)

print(cursor)