# Created by Mikhail Fadeev
# Task Description: Алгоритм Евклида

def gcd(a, b):
    if a > b:
        return gcd(a - b, b)
    elif a < b:
        return gcd(a, b - a)
    else:
        return a

a = int(input("Enter \"a\" value = "))
b = int(input("Enter \"b\" value = "))

print(str(gcd(a, b)))
