K = int(input("Введите число К: "))
value = 0
for i in range(1, K + 1):
    L = i
    R = 0
    while i > 0:
        R = R * 10 + i % 10
        i = int(i / 10)
        if L == R:
            value += 1
print(value)
