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


class Node_smj:
    def __init__(self, n):
        self.number = n
        self.adj = []

    def __str__(self):
        return "Node " + str(self.number)

    def link(self, node):
        if self not in node.adj:
            if len(node.adj) == 0:
                node.adj = [self]
            if len(node.adj) == 1:
                if node.adj[0].number < self.number:
                    node.adj = [self] + node.adj
                else:
                    node.adj = node.adj + [self]

            for i in range(len(node.adj) - 1):
                if node.adj[0].number < self.number:
                    node.adj = [self] + node.adj

                if node.adj[-1].number > self.number:
                    node.adj = node.adj + [self]

                if node.adj[i].number > self.number > node.adj[i + 1].number:
                    node.adj = node.adj[: i + 1] + [self] + node.adj[i + 1 :]

        if node not in self.adj:
            if len(self.adj) == 0:
                self.adj = [node]

            if len(self.adj) == 1:
                if self.adj[0].number < node.number:
                    self.adj = [node] + self.adj
                else:
                    self.adj = self.adj + [node]

            for i in range(len(self.adj) - 1):
                if self.adj[0].number < node.number:
                    self.adj = [node] + self.adj

                if self.adj[-1].number > node.number:
                    self.adj = self.adj + [node]

                if self.adj[i].number > node.number > self.adj[i + 1].number:
                    self.adj = self.adj[: i + 1] + [node] + self.adj[i + 1 :]
