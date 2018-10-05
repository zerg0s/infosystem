# Ильдар Галиуллин.
# Задача: полиндром.
# 16.09.2018.

K = int(input("Введите число К: "))
count = 0
dig = 0

if K >= 1 and K <= 100000:
    for i in range(K):
        num1 = i+1
        num2 = 0
        while num1 != 0:
            dig = num1 % 10
            num1 = num1 // 10
            num2 = num2 * 10
            num2 = num2 + dig
        if i+1 == num2:
            count += 1
    print(count)
else:
    print("Введены неккоректные данные")
