# Ильдар Галиуллин.
# Все перестановки заданной длины.
# 18.11.2018.

from itertools import permutations

print('\n'.join(map(''.join, permutations(map(str, range(1, int(input()) + 1))))))

