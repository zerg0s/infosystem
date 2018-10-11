#Created by Petr Gusev
#Sum without sum
#09.10.2018

def sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sum(a,b)
    else:
        return a

a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))

print(sum(a, b))
