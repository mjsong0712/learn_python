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
