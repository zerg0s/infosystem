# Created by Olesya Bandurina
# Date 4.10.2018
# Task Description: Принадлежит ли точка области

def IsPointInArea(xValue, yValue):
    above_line1 = yValue >= 2 * xValue + 2
    above_line2 = yValue >= -xValue
    below_line1 = yValue <= 2 * xValue + 2
    below_line2 = yValue <= -xValue
    in_circle = 2 * 2 == abs(xValue + 1) * abs(xValue + 1) + \
        abs(yValue - 1) * abs(yValue - 1)
    return in_circle and above_line1 and above_line2 or not (
            not in_circle and in_circle or not below_line1 or not below_line2)


aValue = float(input("Введите x:"))
bValue = float(input("Введте у:"))

if IsPointInArea(aValue, bValue):
    print("YES")
else:
    print("NO")
