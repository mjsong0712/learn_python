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
L = []
N, M = int(N), int(M)

for i in range(N):
    k = input()
    L.append(k)

searched = []
Q = Queue(2000000)
Q.push(((0, 0), 1, False))

while not Q.isEmpty():
    P, d, b = Q.pop()

    if P in searched:
        continue

    if b:
        if P[0] + 1 < N and L[P[0] + 1][P[1]] == 0:
            Q.push((P[0] + 1, P[1]), d + 1, b)
        if P[0] + 1 < M and L[P[0]][P[1] + 1] == 0:
            Q.push((P[0], P[1] + 1), d + 1, b)
        if P[0] - 1 >= 0 and L[P[0] - 1][P[1]] == 0:
            Q.push((P[0] - 1, P[1]), d + 1, b)
        if P[0] - 1 >= 0 and L[P[0]][P[1] - 1] == 0:
            Q.push((P[0], P[1] - 1), d + 1, b)
    else:
        if P[0] + 1 < N:
            Q.push((P[0] + 1, P[1]), d + 1, L[P[0] + 1][P[1]] == 1)
        if P[0] + 1 < M:
            Q.push((P[0], P[1] + 1), d + 1, L[P[0]][P[1] + 1] == 1)
        if P[0] - 1 >= 0:
            Q.push((P[0] - 1, P[1]), d + 1, L[P[0] - 1][P[1]] == 1)
        if P[0] - 1 >= 0:
            Q.push((P[0], P[1] - 1), d + 1, L[P[0]][P[1] - 1] == 1)
