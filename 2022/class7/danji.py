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


class Stack:
    def __init__(self, size):
        self.L = [0 for i in range(size + 1)]
        self.top = -1

    def isEmpty(self):

        return self.top == -1

    def pop(self):
        if self.isEmpty():

            return False
        self.top -= 1
        return self.L[self.top + 1]

    def push(self, item):
        self.top += 1
        self.L[self.top] = item


n = int(input())
L = []
L2 = []
Nodes = [[0 for _ in range(n)] for i in range(n)]
for i in range(n):
    l = list(map(int, input()))
    L.append(l)

for i in range(n):
    for j in range(n):
        if L[i][j] == 1:
            Nodes[i][j] = Node([i, j])

for i in range(n):
    for j in range(n):
        if Nodes[i][j] != 0:
            if i < n - 1 and Nodes[i + 1][j] != 0:
                Nodes[i][j].link(Nodes[i + 1][j])
            if j < n - 1 and Nodes[i][j + 1] != 0:
                Nodes[i][j].link(Nodes[i][j + 1])
searched = []

for i in range(n):
    for j in range(n):
        searched = []
        if Nodes[i][j] != 0:
            S = Stack(1100)
            S.push(Nodes[i][j])

            while not S.isEmpty():
                P = S.pop()
                if P in searched:
                    continue
                searched.append(P)
                for i in range(len(P.adj)):
                    if P.adj[i] not in searched:
                        S.push(P.adj[i])
            for k in range(len(searched)):
                Nodes[searched[k].ind[0]][searched[k].ind[1]] = 0
            L2.append(len(searched))
L2.sort()
print(len(L2))
for i in range(len(L2)):
    print(L2[i])
