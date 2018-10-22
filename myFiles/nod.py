# Ильдар Галиуллин.
# Алгоритм Евклида.
# 26.09.2018.


def gcd(num1, num2):
    if num1 == 0 or num2 == 0:
        return num1 + num2
    else:
        if num1 > num2:
            return gcd(num1 % num2, num2)
        else:
            return gcd(num1, num2 % num1)


number1 = abs(int(input("Введите первое число: ")))
number2 = abs(int(input("Введите второе число: ")))
print(gcd(number1, number2))
