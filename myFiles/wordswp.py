# Автор: Ира Данилова
# Задача: Перестановка двух слов

twoWordStr = input("Введите два слова через пробел: ")
firstWord = twoWordStr[:twoWordStr.find(' ')]
secondWord = twoWordStr[twoWordStr.rfind(' ') + 1:]
print(secondWord + ' ' + firstWord)
