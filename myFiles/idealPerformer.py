# Ильдар Галиуллин.
# Задача: идеальный исполнитель.
# 16.09.2018.

A = int(input("Введите число А: "))
B = int(input("Введите число B: "))

if A == B:
    print("A = B")
elif A > 0 and B > 0 and A > B:
    while A != B:
        if A >= 2*B and A % 2 == 0:
            A = A // 2
            print(":2")
        else:
            A = A - 1
            print("-1")
else:
    print("Введены неккоректные данные")
