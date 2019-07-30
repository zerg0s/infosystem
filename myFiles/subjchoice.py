# Created by Fedyuk Yuliya
# subjChoice
# 02.11.2018

surnames = input("Введите свою фамилию: ").split()
subjects = ['страдания', 'мемология', 'зельеварение', 'литрбол', 'кошководство']
print("Выберите предмет: ", subjects)
choices = []
while True:
    choose = input().split()
    if len(choose) == 0:
        break
    choose = set(choose)
    subjects = set(subjects)
    if len(choose.intersection(subjects)) != len(choose):
        print("Неверно введен предмет!")
        continue
    choices.append(choose)
for i in range(len(surnames)):
    choices[i].add(surnames[i])
print(choices)
