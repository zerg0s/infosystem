# Created by Olesya Bandurina
# Date 4.10.2018
# Task Description: Принадлежит ли точка области

def IsPointInArea(x, y):
    in_circle = 2 * 2 >= abs(x + 1) * abs( x + 1 ) +abs( y - 1 ) * abs( y - 1 )
    above_line1 = y >= 2 * x + 2
    above_line2 = y >= -x
    below_line1 = y <= 2 * x + 2
    below_line2 = y <=- x
    on_circle = 2 * 2 == abs(x + 1) * abs( x + 1 ) +abs( y - 1 ) * abs( y - 1 )
    return in_circle and above_line1 and above_line2 or (on_circle or not in_circle) and below_line1 and below_line2

a = float(input("Введите x:"))
b = float(input("Введте у:"))

if IsPointInArea(a, b):
    print("YES")
else:
    print("NO")