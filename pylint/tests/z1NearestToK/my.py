n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]
for j in range(n):
    my_list = []
    for i in range(n):
        my_list.append((abs(matrix[i][j] - k), matrix[i][j]))
    my_list.sort()
    for i in range(n):
        matrix[i][j] = my_list[i][1]
for i in range(n):
    print(*matrix[i])
