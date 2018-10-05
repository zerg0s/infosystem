#Мария Евсеева
#Замена фрагмента

inputString = input("Введите строку: ")

firstPart = inputString[:inputString.find('h') + 1] 
replacedPart = inputString[inputString.find('h') + 1:inputString.rfind('h')]
lastPart = inputString[inputString.rfind('h'):]

outputString = firstPart + replacedPart.replace('h', 'H') + lastPart

print(outputString)
