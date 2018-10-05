# Created by Anita Kuzmina
# is_point_in_square
# 30.09.2018


def is_point_in_square(x, y):
    if abs(x) + abs(y) <= 1:
        print("YES")
    else:
        print("NO")


firstCord = int(input("Enter first number: "))
secondCord = int(input("Enter second number: "))

is_point_in_square(firstCord, secondCord)
