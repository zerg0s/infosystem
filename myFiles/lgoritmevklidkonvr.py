# Created by Olesya Bandurina
# Date 30.09.2018
# Task Description: Реализуйте рекурсивный алгоритм Евклида

def gcd(aValue, bValue):
    while bValue != 0:
        aValue, bValue = bValue, aValue % bValue
    print(aValue)


x = int(input())
y = int(input())
print(gcd(x, y))
