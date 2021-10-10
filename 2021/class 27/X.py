D = {}


def f(A,B,C):
	if B in D:
		return D[B]
	
	if B%2 == 1:
		D[B] = (f(A,B//2,C) * f(A,(B//2)+1,C)) % C
	if B%2 == 0:
		D[B] = (f(A,B//2,C) * f(A,B//2,C)) % C

	return D[B]
		
		







n = input().split(' ')
A = int(n[0])
B = int(n[1])
C = int(n[2])
D[1] = A%C
print(f(A,B,C))