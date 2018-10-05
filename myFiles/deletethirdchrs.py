#Мария Евсеева
#Удаление каждого третьего

inputString = input("Введите строку: ")

outputString = ""
charIndex = 0
while charIndex < len(inputString):
    if (charIndex % 3) != 0:
        outputString = outputString + inputString[charIndex]
    charIndex = charIndex + 1
print(outputString)
