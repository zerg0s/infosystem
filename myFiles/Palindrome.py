# Аверина Мария
# Количество_палиндромов
# 19.09.2018

def palindrome(num):
    m = num
    p = 0
    while m > 0:
        i = int(m % 10)
        p = int(p * 10 + i)
        m = int(m / 10)
    if p == num:
        return True
    else:
        return False

k = int(input("Введите К: "))
count = 0
for i in range(1, k + 1):
    if palindrome(i):
        count = count + 1

print("Количество палиндромов: ", count)
