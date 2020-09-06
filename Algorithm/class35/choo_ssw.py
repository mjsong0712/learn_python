def choo(weight):
	L = []
	l = len(weight)
	for i in range(3**l):
		w = 0
		for j in range(l):
			w += ((i%(3**(j+1)))/(3**j) - 1) * weight[j]
		L.append(w)
	return L

n = int(raw_input())
L = map(int, raw_input().split())

G = choo(L)
S = sum(L)
cnt = 0


for i in range(1,S+1):
	if i not in G:
		cnt+=1

print cnt
#https://www.acmicpc.net/problem/17610