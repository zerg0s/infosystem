a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = int(input("Введите четвёртое число: "))

if (a == 0 and b == 0):
    print("INF")
elif (c == 0 and d == 0) or (a == 0):
    print("NO")
else:
    x = (-b//a)
    if (c * x + d) == 0:
        print("NO")
    elif (a * x + b) / (c * x + d) == 0:
        print(x)
    else:
        print("NO")
