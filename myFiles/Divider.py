# Мария Евсеева
# Идеальный исполнитель

a = int(input("A = "))
b = int(input("B = "))

if a > b:
    while a != b:
        if a % 2 == 0 and a / 2 >= b:
            print(":2")
            a = a / 2
        else:
            print("-1")
            a = a - 1
else:
    print("Неправильный ввод. A должно быть больше B!")
