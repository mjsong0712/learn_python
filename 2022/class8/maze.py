class Node:
    def __init__(self, ind):
        self.adj = []
        self.ind = ind

    def link(self, node):
        if self not in node.adj:
            node.adj.append(self)

        if node not in self.adj:
            self.adj.append(node)


class Queue:
    def __init__(self, size):
        self._size = size + 1
        self.L = [0 for i in range(self._size)]
        self.front = 1
        self.back = 0

    def isEmpty(self):
        return self.next(self.back) == self.front

    def push(self, item):
        self.back = self.next(self.back)
        self.L[self.back] = item

    def next(self, i):
        if i == self._size - 1:
            return 0
        return i + 1

    def pop(self):
        item = self.L[self.front]
        self.front = self.next(self.front)
        return item


N, M = input().split()
N, M = int(N), int(M)
Maze = []

for i in range(N):
    kL = []
    mL = input()
    for j in range(len(mL)):
        kL.append(mL[j])
    Maze.append(kL)

Nodes = [[0 for i in range(M)] for i in range(N)]
for i in range(N):
    for j in range(M):
        if int(Maze[i][j]) == 1:
            Nodes[i][j] = Node([i, j])

for i in range(N):
    for j in range(M):
        if Nodes[i][j] != 0:
            if i < N - 1 and Nodes[i + 1][j] != 0:
                Nodes[i][j].link(Nodes[i + 1][j])
            if j < M - 1 and Nodes[i][j + 1] != 0:
                Nodes[i][j].link(Nodes[i][j + 1])

searched = []

Q = Queue(100000)
Q.push((Nodes[0][0], 1))

while not Q.isEmpty():
    P, d = Q.pop()
    if P in searched:
        continue
    if P.ind == [N - 1, M - 1]:
        print(d)
        break

    searched.append(P)

    for i in range(len(P.adj)):
        Q.push((P.adj[i], d + 1))
