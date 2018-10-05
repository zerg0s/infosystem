# Аверина Мария
# Складирование ноутбуков
# 12.09.2018

sLength = int(input("Введите длину склада: "))
sWidth = int(input("Введите ширину склада: "))
sHeight = int(input("Введите высоту склада: "))

bLength = int(input("Введите длину коробки с ноутбуком: "))
bWidth = int(input("Введите ширину коробки с ноутбуком: "))
bHeight = int(input("Введите высоту коробки с ноутбуком: "))

sSquare = sLength * sWidth * sHeight
bSquare = bLength * bWidth * bHeight

lCapacity = sSquare / bSquare

print(int(lCapacity), " - максимальное количество ноутбуков, которое может быть размещено на складе.")
