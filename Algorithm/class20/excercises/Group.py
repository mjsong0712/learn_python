def Group(word):
	L = []
	for i in range(len(word)-1):
		if word[i] != word[i+1]:
			L.append(word[i])
		if word[i+1] in L:
			return False
	return True


cnt = 0


n = int(raw_input())

for i in range(n):
	word = raw_input()
	if Group(word):
		cnt += 1
print cnt
