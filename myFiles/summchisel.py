n = int(input())
b = 0
while n > 0:
	b = b + n%10
	n = n // 10
print("Сумма цифр:", b )
