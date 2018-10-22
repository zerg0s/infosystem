# Author: Danilova Irina
# Task: Sum of decimal numbers

digit = int(input("Введите десятичное число: "))
sumOfDigit = 0
while digit > 0:
    sumOfDigit += digit % 10
    digit = digit//10

print("Сумма: ", sumOfDigit)
