# Автор: Ира Данилова
# Задача: Сумма без суммы

def Sum(a, b):
    if b != 0:
        return Sum(a + 1, b - 1)
    else:
        return a

a = int(input())
b = int(input())

print(Sum(a, b))
