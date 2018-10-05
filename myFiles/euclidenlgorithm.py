#Мария Евсеева
#Алгоритм Евклида

def gcd(a, b):
    if a == b:
        return a
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print("НОД введённых чисел: " + str(gcd(a, b)))
