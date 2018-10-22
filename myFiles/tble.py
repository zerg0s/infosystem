# Мальцев Алексей
# Контрольная работа 20.10.18
# Парты

import math

first = input("Введите число студентов в 1 кабинете :")
if first.isdigit():
    first = int(first)
    if first < 1 or first > 1000:
        print("error")
else:
    first = int(input("Введите число студентов в 1 кабинете :"))

second = input("Введите число студентов в 2 кабинете :")
if second.isdigit():
    second = int(second)
    if second < 1 or second > 1000:
        print("error")
else:
    second = int(input("Введите число студентов в 2 кабинете :"))

third = input("Введите число студентов в 3 кабинете :")
if third.isdigit():
    third = int(third)
    if third < 1 or third > 1000:
        print("error")
else:
    third = int(input("Введите число студентов в 3 кабинете :"))

fp = math.ceil(first/2)
sp = math.ceil(second/2)
tp = math.ceil(third/2)
res = fp + sp + tp
print(res)
