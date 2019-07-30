# Created by Mikhail Fadeev
# Task Description: Контрольная по ударениям

rightDict = {}
dictionarySize = int(input())
dictionaryIndex = 0
for index in range(dictionarySize):
    newRight = input()
    rightStress = rightDict.setdefault(newRight.lower(), [])
    rightStress.append(newRight)

text = input()
error = 0
for word in text.split():
    if word.islower():
        error += 1
    else:
        rightStress = rightDict.get(word.lower())
        if rightStress is not None and not word in rightStress:
            error += 1
        elif rightStress is None:
            hasUpCaseChar = False
            for char in word:
                if hasUpCaseChar:
                    error += 1
                    break
                else:
                    hasUpCaseChar = True
print(error)
