#Created by Petr Gusev
#Reverse
#09.10.2018

def reverse():
    a = int(input("Введите число:"))
    if a != 0:
        reverse()
    print (a)

reverse()
