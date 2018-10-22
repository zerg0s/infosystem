# Created by Olesya Bandurina
# Date 20.10.2018
# Task Description: Вычислите сумму цифр натурального числа

N = int(input("Введите число:"))
print((N // 100) + ((N // 10) % 10) + (N - (N // 10) * 10))
