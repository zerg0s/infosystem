# Created by Mikhail Fadeev
# Task Description: Идеальный исполнитель

inputValue = input("Enter \"a\" value = ")
if inputValue.isdigit():
    a = int(inputValue)
    if a < 0:
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter \"b\" value = ")
if inputValue.isdigit():
    b = int(inputValue)
    if b < 0:
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

if a < b:
    print("Invalid input values (\"a\" < \"b\")")
elif a > b:
    while a != b:
        if (a % 2) == 0 and (a / 2) >= b:
            a = a / 2
            print(":2")
        else:
            a = a - 1
            print("-1")
