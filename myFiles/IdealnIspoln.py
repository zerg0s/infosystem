# Аверина Мария
# Идеальный_исполнитель
# 19.09.2018

a = int(input("Введите A: "))
b = int(input("Введите B: "))

if a > b:
    while a != b:
        if a % 2 == 0 and a/2 >= b:
            print(":2")
            a = a / 2
        else:
            print("-1")
            a -= 1
else:
    pass
