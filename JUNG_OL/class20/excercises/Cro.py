L = ["c=","c-","d-","lj","nj","s=","z="]
def Cro(word):
	if word == "":
		return 0
	if word[:3] == "dz=":
		return 1+Cro(word[3:])
	elif word[:2] in L:
		return 1+Cro(word[2:])
	else:
		return 1+Cro(word[1:])


s = raw_input()
print Cro(s)