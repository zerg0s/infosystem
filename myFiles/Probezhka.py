# Ильдар Галиуллин.
# Задача: пробежка по утрам.
# 16.09.2018.

x = int(input("Введите x: "))
y = int(input("Введите y: "))
day = 1
z = x
if x <= y and x > 0 and y > 0:
    while z < y:
        day = day + 1
        z = 1.1*z
    print(day)
else:
    print("Введены неккоректные данные")
