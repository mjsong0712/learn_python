word = raw_input()
a = 0
for i in range(len(word)):
	a += (ord(word[i])-65)/3+3
