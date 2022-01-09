a, b = input().split()

a, b = int(a), int(b)


n = bin(a&b)

print(int(n, 2))