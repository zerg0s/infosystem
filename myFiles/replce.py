# Аверина Мария
# Замена фрагмента
# 02.10.2018

a = input("Введите исходную строку: ")

b = a[:a.find('h') + 1]
c = a[a.find('h') + 1:a.rfind('h')]
d = a[a.rfind('h'):]
a = b + c.replace("h", 'H') + d

print("Строка с заменой h на H: ", a)
