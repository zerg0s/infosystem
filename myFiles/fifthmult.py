# Ильдар Галиуллин.
# Произведение пятых степеней.
# 18.11.2018.

from functools import reduce

print(reduce(lambda x, y: x * y, [i ** 5 for i in map(int, input().split())]))
