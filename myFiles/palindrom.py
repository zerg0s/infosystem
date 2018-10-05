#Created by Olesya Bandurina
#Date 20.09.2018
#Task Description: Вывести количество натуральных палиндромов

a = int(input("Введите число: "))
value = 0
for i in range(1, a + 1):
    l = i
    r = 0
    while i > 0:
        r = r * 10 + i % 10
        i = int(i / 10)
        if l == r:
            value += 1
print(value)

