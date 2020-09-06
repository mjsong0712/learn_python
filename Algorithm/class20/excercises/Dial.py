num2 = ['A','B','C']
num3 = ['D','E','F']
num4 = ['G','H','I']
num5 = ['J','K','L']
num6 = ['M','N','O']
num7 = ['P','Q','R','S']
num8 = ['T','U','V']
num9 = ['W','X','Y','Z']
p = 0
L = [num2,num3,num4,num5,num6,num7,num8,num9]
'''
L = [['A','B','C'],
	 ['D','E','F'],
	 ['G','H','I'],
	 ['J','K','L'],
	 ['M','N','O'],
	 ['P','Q','R','S'],
	 ['T','U','V'],
	 ['W','X','Y','Z']]
'''
word = raw_input()

for i in range(len(word)):
	for j in range(len(L)):
		if word[i] in L[j]:
			p += j+3
print p
