# Created by Olesya Bandurina
# Date 9.10.2018
# Task Description: Сколько в списке пар элементов, равных друг другу

a = input().split()
b = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            b += 1
print(b)



