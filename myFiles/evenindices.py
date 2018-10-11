# Created by Olesya Bandurina
# Date 9.10.2018
# Task Description: Выведите все элементы списка с четными индексами

a = input().split()
for i in range(0, len(a), 2):
    print(a[i], end=" ")
