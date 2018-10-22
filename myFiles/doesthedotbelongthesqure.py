#Created by Grebneva Kseniya
#does_the_dot_belong_the_square
#15.10.2018

def isPointInSquare(firstNum, secondNum):
    return abs(firstNum) + abs(secondNum) <= 1

x = float(input('x = '))
y = float(input('y = '))
if isPointInSquare(x, y):
    print('YES')
else:
    print('NO')
