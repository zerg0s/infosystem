# Created by Mikhail Fadeev
# Task Description: Пробежка по утрам

inputValue = input("Enter \"x\" value = ")
if inputValue.replace(r".", "").isdigit() and inputValue.count(".") <= 1:
    x = float(inputValue)
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter \"y\" value = ")
if inputValue.replace(r".", "").isdigit() and inputValue.count(".") <= 1:
    y = float(inputValue)
else:
    print("Invalid input value!")
    exit()

daysNumber = 1
while x < y:
    x = x + (x * 0.1)
    daysNumber = daysNumber + 1
print(daysNumber)
