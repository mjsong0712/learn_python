n = input().split()

n = list(map(int,n))

for i in range(1,n[0]+1):
  for j in range(1,n[1]+1):
    print(i,j)