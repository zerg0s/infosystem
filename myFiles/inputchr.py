#Мария Евсеева
#Вставка символа

inputString = input("Введите строку: ")

outputString = inputString[0]
charIndex = 1
while charIndex < len(inputString):
    outputString = outputString + "*" + inputString[charIndex]
    charIndex = charIndex + 1

print(outputString)
