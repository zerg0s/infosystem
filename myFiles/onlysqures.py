# Created by Georgiy Abramyan
# Date: 07.10.2019
# Task description: print reverse sequence including only squares

from math import sqrt

def onlySquares():
    num = int(input())
    if num != 0:
        onlySquares()
        if int(sqrt(num))**2 == num:
            print(num, end=' ')

onlySquares()
