# Задача #889992: Сортировка подсчетом
# сделана студентом группы М3О-109М-20 Кремешной Марией
# Дата выполнения 16.10.2020
# Сколько в списке пар элементов, равных друг другу

def numberCheck(numberet):
    if numberet.lstrip('-+').isdigit():
        return int(numberet)
    else:
        print("параметр введены неверно")
        exit()

print("Введите строку через пробел")
roster = list(map(numberCheck, input().split(' ')))
sortedRoster = [0 for x in range(101)]

for i in range(len(roster)):
    sortedRoster[roster[i]] += 1

roster = []

for j in range(101):
    for k in range(sortedRoster[j]):
        roster.append(j)

print(*roster)