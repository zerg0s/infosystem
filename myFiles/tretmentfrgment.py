# Мария Евсеева
# Обращение фрагмента

inputString = input("Введите строку: ")

findLetter = inputString[:inputString.find('h')]
findLetter2 = inputString[inputString.find('h'):inputString.rfind('h') + 1]
findLetter3 = inputString[inputString.rfind('h') + 1:]

outputString = findLetter + findLetter2[::-1] + findLetter3

print(outputString)
