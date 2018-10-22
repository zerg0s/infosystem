# Created by Olesya Bandurina
# Date 20.10.2018
# Task Description:  Разверните последовательность символов, заключенную между первым и последнием появлением буквы h, в противоположном порядке

str1 = input("Введите строку:")
A = str1[:str1.find("h")]
B = str1[str1.find("h"):str1.rfind("h") + 1]
C = str1[str1.rfind("h") + 1:]
str1 = A + B[::-1] + C
print(str1)
