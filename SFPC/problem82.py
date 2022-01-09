n=int(input())
prt = []

for i in range(1,n+1):
  if '3' in str(i) or '6' in str(i) or '9' in str(i):
    prt.append("X")
  else:
    prt.append(i)


for i in range(len(prt)):
  print(prt[i], end=' ')