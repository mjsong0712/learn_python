from re import search


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


N, K = input().split(" ")

N, K = int(N), int(K)
Q = Queue(100000)


searched = [0 for i in range(200001)]

Q.push((N, 0))


while searched[K] == 0:
    P, d = Q.pop()
    if P == K:
        print(d)
        break

    if searched[P] != 0:
        continue

    searched[P] = d

    if P - 1 >= 0 and searched[P - 1] == 0:
        Q.push((P - 1, d + 1))

    if P + 1 < 200000 and searched[P + 1] == 0:
        Q.push((P + 1, d + 1))

    if P * 2 < 200000 and searched[P * 2] == 0:
        Q.push((P * 2, d + 1))
