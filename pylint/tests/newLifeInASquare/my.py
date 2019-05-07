import copy

N, T = list(map(int, input().split()))
a = list()
a.append([0] * (N + 2))
for i in range(0, N):
    b = [0]
    c = list(map(int, input().split()))
    for k in c:
        b.append(k)
    b.append(0)
    a.append(b)
a.append([0] * (N + 2))
d = 0
while d < T:
    temp = copy.deepcopy(a)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            s = a[i - 1][j - 1] + a[i - 1][j] + a[i - 1][j + 1] + a[i][j + 1] \
                + a[i][j - 1] + a[i + 1][j - 1] + a[i + 1][j] + a[i + 1][j + 1]
            if a[i][j] == 1:
                if s < 2:
                    temp[i][j] = 0
                elif s > 3:
                    temp[i][j] = 0
                elif s == 2:
                    temp[i][j] = a[i][j]
            else:
                if s == 3:
                    temp[i][j] = 1
    a = temp
    d += 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(a[i][j], end=" ")
    print()
