def choo(weight):
	if len(weight) == 1:
		return [weight[0], 0, weight[0]*-1]
	P = []
	G = []
	P = choo(weight[1:])
	for j in range(len(P)):
		G.append(P[j] + weight[0])
		G.append(P[j])
		G.append(P[j] + -1*weight[0])
	return G

n = int(raw_input())
L = map(int, raw_input().split())

G = choo(L)
print G
S = sum(L)
cnt = 0

for i in range(1,S+1):
	if i not in G:
		cnt+=1

print cnt
#https://www.acmicpc.net/problem/17610