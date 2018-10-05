#Мария Евсеева
#Сложение без сложения

def Sum(a, b):
    if b == 0:
        return a
    else:
        incA = a + 1
        decB = b - 1
        return Sum(incA, decB)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

print("Сумма:", Sum(a, b))
