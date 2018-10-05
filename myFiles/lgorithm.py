#Исхаков Дамир
#Алгоритм Евклида
#02.10.2018
a = int(input())
b = int(input())
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)
print(gcd(a, b))
