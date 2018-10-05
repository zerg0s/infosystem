#Created by Petr Gusev
#Running in the morning
#18.09.2018

first = float(input("Введите расстояние в км в первый день: "))
second = int(input("Введите расстояние в км в первый день: "))
count = 1										#Считаем с первого дня

if first > second:
    print("Ошибка!")
    exit(1)

while int(first) < second:
    first *= 1.1
    count += 1

print(count, " дней")