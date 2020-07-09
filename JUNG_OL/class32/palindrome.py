def isPalindrome(st):
	for i in range(len(st)):
		if st[i] == st[len(st)-i]:
			if len(st) % 2 == 0:
