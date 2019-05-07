n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or\
           abs(x[i] - x[j]) == abs(y[i] - y[j]):
            r = 1
        else:
            r = 0
if r == 1:
    print('YES')
else:
    print('NO')
