#Created by Olesya Bandurina
#Date 25.09.2018
#Task Description: Удалите из строки все символы, чьи индексы делятся на 3

a = input()
s = str()
j = 0
for i in a:
    if j % 3 == 0:
        j += 1
    else:
        s += i
        j += 1
print(s)

