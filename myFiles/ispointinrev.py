# Created by Anita Kuzmina
# is_point_in_area
# 28.09.2018


def isPointInArea(xCord, yCord):
    circleCore = 2 * 2 >= abs(xCord + 1) * abs(xCord + 1) + abs(yCord - 1) * abs(yCord - 1)
    overLines = yCord >= 2 * xCord + 2 and yCord >= -xCord
    underLines = yCord <= 2 * xCord + 2 and yCord <= -xCord
    circleBorder = 2 * 2 == abs(xCord + 1) * abs(xCord + 1) + abs(yCord - 1) * abs(yCord - 1)

    if circleCore and overLines or (circleBorder or not circleCore) and underLines:
        print("YES")
    else:
        print("NO")


firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))

isPointInArea(firstNum, secondNum)
