L = []

for i in range(19):
    k = input().split()
    L.append(k)

n=int(input())

for i in range(n):
    x,y=input().split()
    for j in range(19):
        if L[j][int(y)-1]==0:
            L[j][int(y)-1]=1
        else:
            L[j][int(y)-1]=0
           
        if L[int(x)-1][j]==0:
            L[int(x)-1][j]=1
        else:
            L[int(x)-1][j]=0  
           

for i in range(19):
    for j in range(19):
        print(int(L[i][j]), end=' ')
    print()