# Аверина Мария
# Алгоритм Евклида
# 12.10.2018


def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print("Наибольший общий делитель: ", gcd(a, b))
