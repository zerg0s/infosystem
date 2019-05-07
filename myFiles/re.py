#Created by Petr Gusev
#Area belong
#12.10.2018

def isPointInArea(xPoint, yPoint):
    return ((-2*xPoint + yPoint - 2 <= 0 and 2*xPoint + 2*yPoint <= 0 and \
    (xPoint + 1)**2 + (yPoint - 1)**2 - 4 >= 0) or \
    (-2*xPoint + yPoint - 2 >= 0 and 2*xPoint + 2*yPoint >= 0 and \
   	(xPoint + 1)**2 + (yPoint - 1)**2 - 4 <= 0))


a = float(input("Введите первую точку: "))
b = float(input("Введите вторую точку: "))

if isPointInArea(a, b):
    print("YES")
else:
    print("NO")
