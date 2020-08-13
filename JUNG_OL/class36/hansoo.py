def isHansoo(n):
	if n==1000:
		return False
	if n<100:
		return True
	a = n/100
	b = (n/10)%10
	c = n%10
	if a-b==b-c:
		return True
	return False

n = int(raw_input())
cnt = 0
for i in range(1,n+1):
	if isHansoo(i):
		cnt +=1

print cnt

######################################

def isHansoo(n):
	if n==1000:
		return False

	if n<100:
		return True

	return n/100 + n%10 == (n/10)%10*2

n = int(raw_input())
cnt = 0
for i in range(1,n+1):
	if isHansoo(i):
		cnt += 1

print cnt