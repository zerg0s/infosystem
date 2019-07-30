# Created by Samohin Artem
# Date 2018-11-15
# Task Description: http://www.hostedredmine.com/issues/782468


# Функция wordInput() служит для инициализации словаря Васи


def wordInput(dWord):
    inData = input()
    upperLetter = list()
    letterList = {}
    i = 0
    while i != int(inData):
        inWord = input()
        for j in range(0, len(inWord)):
            if inWord[j].isupper():
                letterList = {inWord[j]: j}
                upperLetter.append(letterList)
        addWord = {inWord: upperLetter.copy()}
        dWord.update(addWord)
        upperLetter.clear()
        i += 1


def checkUpper(inString):
    upperList = list()
    for k in range(0, len(inString)):
        if inString[k].isupper():
            upperList.append(inString[k])
    return upperList


wordDictionary = {}
errorCounter = 0

wordInput(wordDictionary)

inText = input()
textList = list(inText.split(" "))

errorCheck = True
for index in range(0, len(textList)):
    upperLetters = list(checkUpper(textList[index]))
    for keyWord in wordDictionary:
        if textList[index].lower() == keyWord.lower() and len(upperLetters) == 1:
            if upperLetters[0] in wordDictionary.get(keyWord):
                errorCheck = True
                break
        elif len(upperLetters) == 1:
            errorCheck = True
            break
        else:
            errorCheck = False

    if not errorCheck:
        errorCounter += 1
        errorCheck = True

print(errorCounter)
