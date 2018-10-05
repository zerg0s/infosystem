# Created by Olesya Bandurina
# Date 30.09.2018
# Task Description: Реализуйте рекурсивный алгоритм Евклида

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    print(a)


x = int(input())
y = int(input())
print(gcd(x, y))


