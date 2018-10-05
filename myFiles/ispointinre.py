# Created by Anita Kuzmina
# is_point_in_area
# 30.09.2018


def is_point_in_area(x, y):
    circle_core = 2 * 2 >= abs(x + 1) * abs(x + 1) + abs(y - 1) * abs(y - 1)
    over_lines = y >= 2 * x + 2 and y >= -x
    under_lines = y <= 2 * x + 2 and y <= -x
    circle_border = 2 * 2 == abs(x + 1) * abs(x + 1) + abs(y - 1) * abs(y - 1)

    if circle_core and over_lines or (circle_border or not circle_core) and under_lines:
        print("YES")
    else:
        print("NO")


firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))

is_point_in_area(firstNum, secondNum)
