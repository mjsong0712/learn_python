N = int(input())
T = input().split(' ')
L = input().split(' ')

T = list(map(int, T))
L = list(map(int, L))

k = L[0]
ans = 0


for i in range(N):
	if i == N-1:
		break
	if k > L[i]:
		k = L[i]
	ans += k*T[i]

print(ans)