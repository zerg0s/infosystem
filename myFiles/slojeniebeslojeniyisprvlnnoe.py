# Created by Olesya Bandurina
# Date 4.10.2018
# Task Description: Напишите рекурсивную функцию

def sum(A, B):
    S = 0
    if A != 0:
        A -= 1
        S += 1
    if B != 0:
        B -= 1
        S += 1
    return 0 if S == 0 else S + sum(A, B)

X = int(input())
Y = int(input())
print(sum(X, Y))

