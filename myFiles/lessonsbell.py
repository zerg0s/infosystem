# Евсеева Мария
# Расписание звонков

lessons = int(input("Введите номер урока: "))

findTimeM = (45 * lessons) + (5 * (lessons - 1)) + (10 * ((lessons - 1) // 2))

resultTimeH = 9 + (findTimeM // 60)
resultTimeM = findTimeM % 60

print(str(resultTimeH) + " " + str(resultTimeM))
