def tri(n):
	pass




def choo(weight):
	L = []
	l = len(weight)
	#print(3**l)
	cnt = 0
	for i in range(3**l):
		w = 0
		for j in range(l):
			w += ((i % (3**(j+1))) / (3**j) - 1) * weight[j]
			cnt+=1
		L.append(w)
	print cnt
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