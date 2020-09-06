word = raw_input()
ind = [-1 for i in range(26)]

for i in range(len(word)):
	if -1 == ind[ord(word[i])-97]:
		ind[ord(word[i])-97] = i

for i in range(len(ind)):
	print ind[i],