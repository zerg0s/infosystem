#Created by Grebneva Kseniya
#does_the_dot_belong_to_the_area
#15.10.2018

def isPointInArea(firstNum, secondNum):
    inCir = 2 * 2 >= abs(firstNum + 1) * abs(firstNum + 1) + abs(secondNum - 1) * abs(secondNum - 1)
    onCir = 2 * 2 == abs(firstNum + 1) * abs(firstNum + 1) + abs(secondNum - 1) * abs(secondNum - 1)
    return ((inCir and secondNum >= 2 * firstNum + 2 and secondNum >= -firstNum) or
            ((onCir or not inCir) and secondNum <= 2 * firstNum + 2 and secondNum <= -firstNum))

x = float(input('x = '))
y = float(input('y = '))
if isPointInArea(x, y):
    print('YES')
else:
    print('NO')
