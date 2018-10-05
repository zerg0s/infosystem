# Created by Mikhail Fadeev
# Task Description: Вставка символа

sourceString = input("Enter string: ")

extString = sourceString[0]
i = 1
while i < len(sourceString):
    extString = extString + "*" + sourceString[i]
    i = i + 1

print(extString)
