# Created by Fedyuk Yuliya
# desk
# 18.10.2018
classOne = float(input("Введите количество учеников в первом классе: "))
classTwo = float(input("Введите количество учеников во втором классе: "))
classThree = float(input("Введите количество учеников в третьем классе: "))
print("Нужно парт:", ((classOne + 1) // 2) + ((classTwo + 1) // 2) +
      ((classThree + 1) // 2))
