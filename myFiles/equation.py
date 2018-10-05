#Created by Petr Gusev
#Difficult equation
#11.09.2018

print("Введите данные для уравнение (ax + b)/(cx + d) = 0")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))

if c == d == 0:
    print("NO")
elif b == 0 and a == 0:
    print("INF")
elif a == 0 and b != 0:
    print("NO")
elif c == 0:
    res = (-b / a)
    print(res)
elif b/a == d/c:
    print("NO")
else:
    res = (-b / a)
    print("Result is ", res)