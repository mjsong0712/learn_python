class Node:
    def __init__(self, n):
        self.number = n
        self.adj = []

    def link(self, node):
        if self not in node.adj:
            node.adj.append(self)

        if node not in self.adj:
            self.adj.append(node)
