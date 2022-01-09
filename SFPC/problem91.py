n = input().split()

a = int(n[0])
b = int(n[1])
c = int(n[2])

d = 1

while True:
    if d%a == 0 and d%b==0 and d%c==0:
        break
    d+=1
    
print(d)