class Node:
    def __init__(self, n):
        self.number = n
        self.adj = []

    def __str__(self):
        return "Node " + str(self.number)

    def link(self, node):
        if self not in node.adj:
            for i in range(len(node.adj)):
                if self.number < node.adj[i].number:
                    node.adj = node.adj[:i] + [self] + node.adj[i:]
                    break

            if self not in node.adj:
                node.adj.append(self)

        if node not in self.adj:
            for i in range(len(self.adj)):
                if node.number < self.adj[i].number:
                    self.adj = self.adj[:i] + [node] + self.adj[i:]
                    break

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


number = int(input())
connected = int(input())


Nodes = [None]

N = number
M = connected
V = 1

for i in range(1, N + 1):
    Nodes.append(Node(i))

for i in range(M):
    frm, to = list(map(int, input().split()))
    Nodes[frm].link(Nodes[to])


############################

searched = []
S = Stack(1100)
S.push(Nodes[V])

while not S.isEmpty():

    P = S.pop()

    if P.number in searched:
        continue
    searched.append(P.number)

    for i in range(len(P.adj) - 1, -1, -1):
        if P.adj[i].number not in searched:
            S.push(P.adj[i])


searched = list(map(str, searched))

print(len(searched) - 1)


##########################
