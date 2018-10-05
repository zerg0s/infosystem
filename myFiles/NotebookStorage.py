# Мария Евсеева
# Складирование ноутбуков

storehouseLength = int(input("Введите длинну склада = "))
storehouseWidth = int(input("Введите ширину склада = "))
storehouseHeight = int(input("Введите высоту склада = "))
boxLength = int(input("Введите длинну коробки = "))
boxWidth = int(input("Введите ширину коробки = "))
boxHeight = int(input("Введите высоту коробки = "))

print((storehouseLength * storehouseWidth * storehouseHeight)\
      // (boxLength * boxWidth * boxHeight))
