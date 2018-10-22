# Аверина Мария
# Обращение фрагмента
# 20.10.2018


lst = input("Введите строку: ")

lst1 = lst[:lst.find('h') + 1] + lst[lst.rfind('h') -\
    1:lst.find('h'):-1] + lst[lst.rfind('h'):]

print("Ответ: ", lst1)
