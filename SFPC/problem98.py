L = []
ant_loc = [2,2]

for i in range(10):
    k = input().split()
    k = list(map(int,k))
    L.append(k)

L[1][1] = 9 
for i in range(10):
    for j in range(10):
        if L[i][j] == 2:
            food_loc = [j+1,i+1]
            break
while True:
    if ant_loc == food_loc:
        break

    if L[ant_loc[1]-1][ant_loc[0]] == 1 and L[ant_loc[1]][ant_loc[0]-1] == 1:
        break
    if L[ant_loc[1]-1][ant_loc[0]] == 0:       
        ant_loc[0]+=1
        L[ant_loc[1]-1][ant_loc[0]-1] = 9
        if L[ant_loc[1]-1][ant_loc[0]] == 1 and L[ant_loc[1]][ant_loc[0]-1] == 1:
            break
    if L[ant_loc[1]-1][ant_loc[0]] == 1:
        ant_loc[1]+=1
        L[ant_loc[1]-1][ant_loc[0]-1] = 9
        if L[ant_loc[1]-1][ant_loc[0]] == 1 and L[ant_loc[1]][ant_loc[0]-1] == 1:
            break
    
    
for i in range(len(L)):
    for j in range(len(L)):
        print(L[i][j],end=' ')
    print()