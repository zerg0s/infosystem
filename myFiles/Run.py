# Created by Alexey Maltsev
# 15.09.18
# Run

x = int(input())
y = int(input())
d = 1
while x < y:
    x = x + (x * 0.1)
    d += 1
print(d)
