# Created by Fedyuk Yuliya
# ChangePart
# 3.10.2018
s = input("Введите строку: ")
a = s[:s.find('h') + 1]
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
str1 = a + b.replace('h', 'H') + c
print(str1)
