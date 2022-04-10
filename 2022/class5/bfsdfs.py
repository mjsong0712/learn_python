from Stack import Stack
from Queue import Queue
from Node import Node

N, M, V = list(map(int, input().split()))


def bubble_sort(L):
    for i in range(len(L) - 1, 0, -1):
        for j in range(i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]


tL = [5, 124, 15, 12, 44, 55, 22]
bubble_sort(tL)
print(tL)

Nodes = [None]
for i in range(1, N + 1):
    Nodes.append(Node(i))


for i in range(M):
    frm, to = list(map(int, input().split()))
    Nodes[frm].link(Nodes[to])

searched = []
S = Stack(1000)
S.push(Nodes[V])

while not S.isEmpty():
    P = S.pop()
    if P.number in searched:
        continue
    searched.append(P.number)

    for i in range(len(P.adj)):
        if P.adj[i].number not in searched:
            print(P.adj[i].number, "b")
            S.push(P.adj[i])


print(searched)


# sort에 cmp function 삽입하는 방법 검색
