# Автор: Ира Данилова
# Задача: Замена фрагмента

srcStr = input("Введите строку: ")

beforeStrPart = srcStr[:srcStr.find('h') + 1] 
replacedStrPart = srcStr[srcStr.find('h') + 1:srcStr.rfind('h')]\
                  .replace('h', 'H')
pastStrPart = srcStr[srcStr.rfind('h'):]

print(beforeStrPart + replacedStrPart + pastStrPart)
