A = map(int, raw_input().split())
B = map(int, raw_input().split())
C = map(int, raw_input().split())
x = 0
y = 0
if (A[0] == B[0] or A[0] == C[0]) and (A[1] != B[1] and A[1] != C[1]):
	y = A[1]
if (A[0] != B[0] and A[0] != C[0]) and (A[1] == B[1] or A[1] == C[1]):
	x = A[0]



if (A[0] == B[0] or B[0] == C[0]) and (A[1] != B[1] and B[1] != C[1]):
	y = B[1]
if (A[0] != B[0] and B[0] != C[0]) and (A[1] == B[1] or B[1] == C[1]):
	x = B[0]



if (C[0] == B[0] or A[0] == C[0]) and (C[1] != B[1] and A[1] != C[1]):
	y = C[1]
if (C[0] != B[0] and A[0] != C[0]) and (C[1] == B[1] or A[1] == C[1]):
	x = C[0]

print x,y
'''
L = [[0, 0], [0, 0], [0, 0]]
for i in range(3):
	L[i] = map(int, raw_input().split())


for i in range(3):
	a = 
	b = 
	if (L[i][0] == L[(i+1)%3][0] or L[i][0] == L[(i+2)%3][0]) and (L[i][1] != L[(i+1)%3][1] and L[i][1] != L[(i+2)%3][1]):
		y = L[i][1]
	if (L[i][0] != L[(i+1)%3][0] and L[i][0] != L[(i+2)%3][0]) and (L[i][1] == L[(i+1)%3][1] or L[i][1] == L[(i+2)%3][1]):
		x = L[i][0]

print x,y'''