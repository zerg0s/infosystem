# Ильдар Галиуллин.
# Задача: минимальное расстояние между локальными максимумами.
# 16.09.2018.

num1 = 1
num2 = 0
num3 = 0
locMaxNum1 = 0
locMaxNum2 = 0
idx = 0
minLengh = 1000
while num1 != 0:
    idx = idx + 1
    num3 = num2
    num2 = num1
    num1 = int(input("Введите число: "))
    if num2 > num1 and num2 > num3 and num1 != 0:
        locMaxNum2 = locMaxNum1
        locMaxNum1 = idx
        if locMaxNum1 > 0 and locMaxNum2 > 0 and \
           locMaxNum1 - locMaxNum2 < minLengh:
            minLengh = locMaxNum1 - locMaxNum2
if minLengh == 1000:
    minLengh = 0
print(minLengh)
