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

Q = Queue(2000000)
Q.push(((0, 0), 1, False))

searched = [[False for i in range(M)] for i in range(N)]

ans = -1

while not Q.isEmpty():
    P, d, b = Q.pop()

    if P[0] == N - 1 and P[1] == M - 1:
        ans = d
        break

    if b:
        indices = []
        if P[0] + 1 < N and L[P[0] + 1][P[1]] == "0" and not searched[P[0] + 1][P[1]]:
            indices.append((P[0] + 1, P[1]))
        if P[1] + 1 < M and L[P[0]][P[1] + 1] == "0" and not searched[P[0]][P[1] + 1]:
            indices.append((P[0], P[1] + 1))
        if P[0] - 1 >= 0 and L[P[0] - 1][P[1]] == "0" and not searched[P[0] - 1][P[1]]:
            indices.append((P[0] - 1, P[1]))
        if P[1] - 1 >= 0 and L[P[0]][P[1] - 1] == "0" and not searched[P[0]][P[1] - 1]:
            indices.append((P[0], P[1] - 1))

        for index in indices:
            searched[index[0]][index[1]] = True
            Q.push((index, d + 1, b))

    else:
        indices = []
        if P[0] + 1 < N and not searched[P[0] + 1][P[1]]:
            indices.append((P[0] + 1, P[1]))
            Q.push(((P[0] + 1, P[1]), d + 1, L[P[0] + 1][P[1]] == "1"))
        if P[1] + 1 < M and not searched[P[0]][P[1] + 1]:
            indices.append((P[0], P[1] + 1))
            Q.push(((P[0], P[1] + 1), d + 1, L[P[0]][P[1] + 1] == "1"))
        if P[0] - 1 >= 0 and not searched[P[0] - 1][P[1]]:
            indices.append((P[0] - 1, P[1]))
            Q.push(((P[0] - 1, P[1]), d + 1, L[P[0] - 1][P[1]] == "1"))
        if P[1] - 1 >= 0 and not searched[P[0]][P[1] - 1]:
            indices.append((P[0], P[1] - 1))
            Q.push(((P[0], P[1] - 1), d + 1, L[P[0]][P[1] - 1] == "1"))

        for index in indices:
            searched[index[0]][index[1]] = True
            Q.push((index, d + 1, L[index[0]][index[1]] == "1"))


print(ans)
