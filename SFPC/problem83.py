n = input().split()
cnt = 0

n = list(map(int, n))
for i in range(n[0]):
  for j in range(n[1]):
    for k in range(n[2]):
      print(i,j,k)
      cnt += 1

print(cnt)