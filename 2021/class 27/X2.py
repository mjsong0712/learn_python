def f(A,B,C):
	if B == 1:
		return A%C

	if B % 2 == 1:
		return (f(A,B-1,C) * (A%C))%C

	if B % 2 == 0:
		return (f(A,B//2,C) ** 2)%C


n = input().split(' ')
A = int(n[0])
B = int(n[1])
C = int(n[2])

print(f(A,B,C))