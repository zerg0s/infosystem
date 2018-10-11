# Created by Olesya Bandurina
# Date 9.10.2018
# Task Description: Сжать список, переместив все ненулевые элементы в левую часть списка

lst = input().split()
for i in reversed(range(len(lst))):
    if lst[i] == '0':
        lst.append(lst.pop(i))
print(*lst)
