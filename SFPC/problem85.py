import math

w, h, b = input().split()

w, h, b = int(w), int(h), int(b)



print(str(f'{round(w*h*b/8/1024/1024, 2):.2f}') + ' MB')

