# Created by Mikhail Fadeev
# Task Description: Определить максимальное количество ноутбуков,
#     которое может быть размещено на складе

inputValue = input("Enter length of storage = ")
if (inputValue.isdigit()):
    storageLength = int(inputValue)
    if storageLength <= 0:
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter width of storage = ")
if (inputValue.isdigit()):
    storageWidth = int(inputValue)
    if storageWidth <= 0:
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter height of storage = ")
if (inputValue.isdigit()):
    storageHeight = int(inputValue)
    if storageHeight <= 0:
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter length of box = ")
if (inputValue.isdigit()):
    boxLength = int(inputValue)
    if boxLength <= 0:
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter width of box = ")
if (inputValue.isdigit()):
    boxWidth = int(inputValue)
    if boxWidth <= 0:
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter height of box = ")
if (inputValue.isdigit()):
    boxHeight = int(inputValue)
    if boxHeight <= 0:
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

storageSize = storageLength * storageWidth * storageHeight
boxSize = boxLength * boxWidth * boxHeight

print(storageSize // boxSize)
