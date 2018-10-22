# Евсеева Мария
# Сумма десятичных цифр

sourceNumber = int(input("Введи число: "))
sumNumber = 0

while sourceNumber > 0:
    digit = sourceNumber % 10
    sumNumber += digit
    sourceNumber = sourceNumber // 10

print(sumNumber)
