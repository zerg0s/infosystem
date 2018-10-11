# Автор: Ира Данилова
# Задача: Алгоритм Евклида

def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    elif a < b:
        return gcd(a, b - a)

a = int(input())
b = int(input())

print(gcd(a, b))
