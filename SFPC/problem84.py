import math

h, b, c, s = input().split()

h, b, c, s = int(h), int(b), int(c), int(s)



print(str(round(h*b*c*s/8/1024/1024, 1)) + ' MB')

