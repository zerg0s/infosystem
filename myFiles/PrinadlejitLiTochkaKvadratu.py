def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1

a = float(input("Введите координату х: "))
b = float(input("Введите координату у: "))
if IsPointInSquare(a, b):
    print("YES")
else:
    print("NO")
