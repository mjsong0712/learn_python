N = int(input())
P = input().split(' ')
ans = 0

P = list(map(int, P))
P.sort()

for i in range(N):
	ans += sum(P[:i])

ans += sum(P)
print(ans)