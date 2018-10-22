# Аверина Мария
# Принадлежит ли точка области
# 12.10.2018


def IsPointInArea(num1, num2):
    inCircle = 2 * 2 >= abs(num1 + 1) * abs(num1 + 1) + abs(num2 - 1) * abs(num2 - 1)
    aboveLine1 = num2 >= 2 * num1 + 2
    aboveLine2 = num2 >= -num1
    belowLine1 = num2 <= 2 * num1 + 2
    belowLine2 = num2 <= -num1
    onCircle = 2 * 2 == abs(num1 + 1) * abs(num1 + 1) + abs(num2 - 1) * abs(num2 - 1)
	
    return inCircle and aboveLine1 and aboveLine2 or (onCircle or not inCircle) and belowLine1 and belowLine2

	
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if IsPointInArea(a, b):
    print("YES")
else:
    print("NO")
