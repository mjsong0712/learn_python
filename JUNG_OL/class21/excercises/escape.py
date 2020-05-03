n = raw_input().split()
x = int(n[0])
y = int(n[1])
w = int(n[2])
h = int(n[3])
mn = 1000
if mn > x:
	mn = x
if mn > y:
	mn = y
if mn > w-x:
	mn = w-x
if mn > h-y:
	mn = h-y
print mn
#n = raw_input().split();print(min([int(n[0]), int(n[1]), int(n[2])-int(n[0]), int(n[3])-int(n[1])]))


