# Created by Mikhail Fadeev
# Task Description: Проверка хода шашки

inputValue = input("Enter x of first cell = ")
if (inputValue.isdigit()):
    xFirstCell = int(inputValue)
    if (xFirstCell < 1) or (8 < xFirstCell):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter y of first cell = ")
if (inputValue.isdigit()):
    yFirstCell = int(inputValue)
    if (yFirstCell < 1) or (8 < yFirstCell):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter x of second cell = ")
if (inputValue.isdigit()):
    xSecondCell = int(inputValue)
    if (xSecondCell < 1) or (8 < xSecondCell):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter y of second cell = ")
if (inputValue.isdigit()):
    ySecondCell = int(inputValue)
    if (ySecondCell < 1) or (8 < ySecondCell):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

xOffset = abs(xSecondCell - xFirstCell)
yOffset = ySecondCell - yFirstCell

xFirstCellParity = xFirstCell % 2
xSecondCellParity = xSecondCell % 2
ySummaryCellParity = yOffset % 2

if (ySecondCell > yFirstCell) and (xOffset <= yOffset)\
      and ((xFirstCellParity == xSecondCellParity and not ySummaryCellParity)\
      or (xFirstCellParity != xSecondCellParity and ySummaryCellParity)):
    print("YES")
else:
    print("NO")
