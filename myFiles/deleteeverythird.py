# Created by Fedyuk Yuliya
# DeleteEveryThird
# 02.10.2018

s = input("Введите строку: ")
strNew = list(s)
del strNew[::3]
print("Новая строка: ", ''.join(strNew))
