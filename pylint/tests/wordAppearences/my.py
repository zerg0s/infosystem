listOfStr = input().split()
listOfDigits = []
for item in listOfStr:
    if item.isdigit():
        listOfDigits.append(int(item))
print(*listOfDigits)
print(len(set(listOfDigits)))
listOfDigits2 = []
for i in listOfDigits:
    listOfDigits2.append([i, 0])

for i in range(len(listOfDigits2)):
    for j in range(i):
        if listOfDigits2[i][0] == listOfDigits2[j][0]:
            listOfDigits2[i][1] += 1

for item in listOfDigits2:
    print(f"{item[0]} - {item[1]}")
