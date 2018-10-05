# Created by Anita Kuzmina
# Perfect performer
# 16.09.2018

a = int(input("Enter A: "))
b = int(input("Enter B: "))

while a != b:
    if a%2 == 0 and a/2 >= b:
        print(":2")
        a = a / 2
    else:
        print("-1")
        a = a - 1