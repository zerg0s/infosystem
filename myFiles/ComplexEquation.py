# Мария Евсеева
# Сложное уравнение

a = int(input("Введите значение a = "))
b = int(input("Введите значение b = "))
c = int(input("Введите значение c = "))
d = int(input("Введите значение d = "))

if a == 0 and b == 0:
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
