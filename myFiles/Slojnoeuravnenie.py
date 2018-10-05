#Created by Olesya Bandurina
#Date 09.09.2018
#Task Description: Решить в целых числах уравнение

a: int = int(input("Введите число а:"))
b: int = int(input("Введите число b:"))
c: int = int(input("Введите число c:"))
d: int = int(input("Введите число d:"))

if c == 0 and d == 0:
    print("NO")
elif a == 0 and b == 0:
    print("INF")
elif a == 0:
    print("NO")
elif c == 0:
    print(-b/a)
elif b/a == d/c:
    print("NO")
else:
    print(-b/a)

