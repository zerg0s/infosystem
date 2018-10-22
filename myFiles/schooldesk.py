# Евсеева Мария
# Парты

numStudent = int(input("Введите число студентов: "))
numStudent2 = int(input("Введите число студентов: "))
numStudent3 = int(input("Введите число студентов: "))

classOne = (numStudent // 2) + (numStudent % 2)
classTwo = (numStudent2 // 2) + (numStudent2 % 2)
classThree = (numStudent3 // 2) + (numStudent3 % 2)

sumStudent = classOne + classTwo + classThree

print(sumStudent)
