# Created by Mikhail Fadeev
# Task Description: Решить в целых числах уравнение (ax+b)/(cx+d) = 0

inputValue = input("Enter \"a\" value = ")
if (inputValue.lstrip("-").isdigit()):
    a = int(inputValue)
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter \"b\" value = ")
if (inputValue.lstrip("-").isdigit()):
    b = int(inputValue)
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter \"c\" value = ")
if (inputValue.lstrip("-").isdigit()):
    c = int(inputValue)
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter \"d\" value = ")
if (inputValue.lstrip("-").isdigit()):
    d = int(inputValue)
else:
    print("Invalid input value!")
    exit()

if ((c == 0) and (d == 0)):
    print("NO")
    exit()

if ((a == 0) and (b == 0)):
    print("INF")
elif (a == 0):
    print("NO")
else:
    result = -b // a
    if (c * result + d) == 0:
        print("NO")
    elif (a * result + b) / (c * result + d) == 0:
        print(result)
    else:
        print("NO")
