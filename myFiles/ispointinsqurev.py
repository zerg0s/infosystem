# Created by Anita Kuzmina
# is_point_in_square
# 28.09.2018


def isPointInSquare(xCord, yCord):
    if abs(xCord) + abs(yCord) <= 1:
        print("YES")
    else:
        print("NO")


firstCord = int(input("Enter first number: "))
secondCord = int(input("Enter second number: "))

isPointInSquare(firstCord, secondCord)
