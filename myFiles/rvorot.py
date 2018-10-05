# Created by Olesya Bandurina
# Date 30.09.2018
# Task Description: Выведите последовательность в обратном порядке

def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)


reverse()

