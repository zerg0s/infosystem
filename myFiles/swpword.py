#Мария Евсеева
#Перестановка слов

inputString = input("Введите два слова через пробел: ")
firstWord = inputString[:inputString.find(' ')]
secondWord = inputString[inputString.find(' ') + 1:]
print (secondWord + ' ' + firstWord)
