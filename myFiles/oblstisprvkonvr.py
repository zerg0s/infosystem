# Created by Olesya Bandurina
# Date 4.10.2018
# Task Description: Принадлежит ли точка области

def IsPointInArea(xValue, yValue):
    inCircle = 2 * 2 >= abs(xValue + 1) * abs(yValue + 1) \
               + abs(xValue - 1) * abs(yValue - 1)
    aboveLine1 = yValue >= 2 * xValue + 2
    aboveLine2 = yValue >= -xValue
    belowLine1 = yValue <= 2 * xValue + 2
    belowLine2 = yValue <= -xValue
    onCircle = 2 * 2 == abs(xValue + 1) * abs(xValue + 1) \
               + abs(yValue - 1) * abs(yValue - 1)
    return inCircle and aboveLine1 and aboveLine2 or \
           (onCircle or not inCircle) and belowLine1 and belowLine2


A = float(input("Введите x:"))
B = float(input("Введте у:"))

if IsPointInArea(A, B):
    print("YES")
else:
    print("NO")
