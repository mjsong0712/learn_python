def isPalindrome(st):
	for i in range(len(st)/2):
		if st[i] != st[len(st)-1-i]:
			return False				
	return True

def main(st):
	if isPalindrome(st):
		return 0
	for i in range(len(st)):
		if isPalindrome(st[:i] + st[i+1:]):
			return 1
	return 2

n = int(raw_input())
for i in range(n):
	st = raw_input()
	print main(st)



'''
7
abba
summuus
xabba
xabbay
comcom
comwwmoc
comwwtmoc

'''
