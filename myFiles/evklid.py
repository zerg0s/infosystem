# Created  by Maltsev Alexey
# 09.10.18
# Алгоритм Евклида

a = int(input("Введите a: "))
b = int(input("Введите b: "))
def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        if a > b:
            return gcd(a % b, b)
        else:
            return gcd(a, b % a)
print(gcd(a, b))
