# Created by Mikhail Fadeev
# Task Description: Проверка хода шахматного короля

inputValue = input("Enter x of first cell = ")
if inputValue.isdigit():
    xFirstCell = int(inputValue)
    if (xFirstCell < 1) or (xFirstCell > 8):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter y of first cell = ")
if inputValue.isdigit():
    yFirstCell = int(inputValue)
    if (yFirstCell < 1) or (yFirstCell > 8):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter x of second cell = ")
if inputValue.isdigit():
    xSecondCell = int(inputValue)
    if (xSecondCell < 1) or (xSecondCell > 8):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter y of second cell = ")
if inputValue.isdigit():
    ySecondCell = int(inputValue)
    if (ySecondCell < 1) or (ySecondCell > 8):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

if (abs(xSecondCell - xFirstCell) <= 1) and (abs(ySecondCell - yFirstCell) <= 1):
    print("YES")
else:
    print("NO")