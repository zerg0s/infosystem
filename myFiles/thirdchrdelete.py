# Автор: Ира Данилова
# Задача: Удаление каждого третьего символа в строке

srcStr = input("Введите строку: ")

modifedStr = ""
i = 0
while i < len(srcStr):
    if (i % 3) != 0:
        modifedStr = modifedStr + srcStr[i]
    i += 1
print("Строка без каждого третьего символа: " + modifedStr)
