n = int(input())

E = []

for i in range(1,n+1):
  if i % 2==0:
    E.append(i)

print(sum(E))