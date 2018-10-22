# Фадеев Михаил
# Обращение фрагмента

sourceString = input("Введите строку: ")
beforePart = sourceString[:sourceString.find('h')]
miidlePart = sourceString[sourceString.find('h'):sourceString.rfind('h') + 1]
afterPart = sourceString[sourceString.rfind('h') + 1:]

print(beforePart + miidlePart[::-1] + afterPart)
