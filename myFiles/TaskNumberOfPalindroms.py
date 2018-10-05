# Created by Mikhail Fadeev
# Task Description: Количество палиндромов

inputValue = input("Enter \"k\" value = ")
if inputValue.isdigit():
    k = int(inputValue)
    if k < 1 and k > 100000:
        print("Invalid input value!")
else:
    print("Invalid input value!")
    exit()

counterPalindroms = 0
for num in range(1, k):
    strNum = str(num)
    if strNum == strNum[::-1]:
        counterPalindroms = counterPalindroms + 1
print(counterPalindroms)
