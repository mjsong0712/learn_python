n = int(input())
L = input().split()


for i in range(n):
  L[i] = int(L[i])

tmp = L[0]

L.reverse()


for i in range(n):
  print(L[i], end=' ')