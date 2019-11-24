# Created by Georgiy Abramyan
# Date: 06.10.2019
# Task description: find out whether a point belongs to an area

from math import sqrt

def isPointInSquare(xCoord, yCoord):
    vectLength = sqrt(xCoord**2 + yCoord**2)
    sinus = yCoord / vectLength
    cosinus = xCoord / vectLength
    return vectLength <= sinus**2 + cosinus**2

abscissa, ordinate = float(input()), float(input())
answer = 'YES' if isPointInSquare(abscissa, ordinate) else 'NO'
print(answer)
