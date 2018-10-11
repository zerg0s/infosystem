# Ильдар Галиуллин.
# Четные индексы.
# 08.10.2018.

numbers = [int(s) for s in input().split()]
for i in range(len(numbers)):
    if i % 2 == 0:
        print('%d' % numbers[i], end=' ')
