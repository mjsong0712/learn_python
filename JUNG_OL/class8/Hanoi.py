def hanoi(n):
	if n == 1:
		return 1
	return 2 * hanoi(n-1) + 1



def hanoiSteps(s,e,n):
	if n==1:
		print str(s)+" "+str(e)
		return
	spare = 6-(s+e)
	hanoiSteps(s,spare,n-1)
	print str(s)+" "+str(e)
	hanoiSteps(spare,e,n-1)


i = int(raw_input())
print(hanoi(i))
hanoiSteps(1,3,i)