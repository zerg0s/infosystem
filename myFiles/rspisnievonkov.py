# Created by Olesya Bandurina
# Date 20.10.2018
# Task Description: Определите, когда заканчивается урок

a = int(input("Введите номер урока:"))
b = a * 45 + (a // 2) * 5
c = ((a + 1) // 2 - 1) * 15
a = b + c
print(a // 60 + 9, a % 60)
