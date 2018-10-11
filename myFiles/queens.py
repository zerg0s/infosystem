# Ильдар Галиуллин.
# Ферзи.
# 08.10.2018.

import math


def test(list1, list2, listLen):
    j = 0
    for i in range(listLen):
        if list1[i] < 1 or list1[i] > 8 or list2[i] < 1 or list2[i] > 8:
            print("Error")
            exit(0)
        for j in range(i + 1, listLen):
            if list1[i] == list1[j] or list2[i] == list2[j] or \
                    math.fabs(list1[i] - list1[j]) == math.fabs(list2[i] - list2[j]):
                return False
    return True

n = 8
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = [int(s) for s in input().split()]
if test(x, y, n):
    print("NO")
else:
    print("YES")
