def isPointInArea(X, Y):
    inCircle = 2 * 2 >= abs(X + 1) * abs(X + 1) + abs(Y - 1) * abs(Y - 1)
    aboveLine1 = Y >= 2 * X + 2
    aboveLine2 = Y >= -X
    belowLine1 = Y <= 2 * X + 2
    belowLine2 = Y <= -X
    onCircle = 2 * 2 == abs(X + 1) * abs(X + 1) + abs(Y - 1) * abs(Y - 1)
    return inCircle and aboveLine1 and aboveLine2 or \
    (onCircle or not inCircle) and belowLine1 and belowLine2

A = float(input("Введите координату х: "))
B = float(input("Введите координату у: "))
if isPointInArea(A, B):
    print("YES")
else:
    print("NO")
