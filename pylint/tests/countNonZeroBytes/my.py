#Z2
a = int(input("Введите число (a < 16): "))
print("Число в двоичном виде", bin(a))
sum1 = 0
sum1 += a % 2
a = a // 2
sum1 += a % 2
a //= 2
sum1 += a % 2
a //= 2
sum1 += a % 2
print("Количество единиц в двоичном представлении = ", sum1)
