n = int(input())

summ = 0
i = 1
while True:
  summ+=i
  if summ >= n:
    print(i)
    break
  i+=1