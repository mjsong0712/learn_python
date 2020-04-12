cnt = [0 for i in range(10)]

a=int(raw_input())
b=int(raw_input())
c=int(raw_input())
m = a*b*c
while m>0:
	cnt[m%10] +=1
	m /= 10
for i in range(10):
	print cnt[i]