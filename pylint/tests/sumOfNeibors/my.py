n = int(input())
answer = 0
for i in range(1, n):
    print(i, '*', i + 1, sep='', end='')
    if i != n - 1:
        print('+', end='')
    answer += i * (i + 1)
print('=', answer, sep='')
