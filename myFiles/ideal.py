#Created by Petr Gusev
#Idealny ispolnitel
#25.09.2018

print("Введите 2 числа:")
a = int(input("A: "))
b = int(input("B: "))

if b > a:
    print("Ошибка. В больше А.")
    exit(1)


while a != b:
    if a/2 > b and a % 2 == 0:
        print(":2")
        a /= 2
    else:
        print("-1")
        a -= 1
