# Фадеев Михаил
# Сумма десятичных цифр

sourceNumber = int(input("Введи число: "))
sumNumber = 0

for stringNumber in str(sourceNumber):
    sumNumber += int(stringNumber)

print(sumNumber)
