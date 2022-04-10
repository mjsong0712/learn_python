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
