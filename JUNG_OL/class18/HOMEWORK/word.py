def main():
	mx = 0
	ind = 0
	word = raw_input().upper()
	L = [0 for i in range(26)]
	for i in range(len(word)):
		L[ord(word[i])-65]	+=1

	for i in range(len(L)):
		if mx == L[i] and mx !=0:
			print "?"
			return
		if mx < L[i]:
		 	mx = L[i]
		 	ind = i
	
	print chr(ind+65)
	return

main()