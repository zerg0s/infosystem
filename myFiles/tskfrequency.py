# Created by Samohin Artem
# Date 2018-11-10
# Task Description: http://www.hostedredmine.com/issues/782531


def getKey(myDict, checkValue):
    for keyDict, valueDict in myDict.items():
        if valueDict == checkValue:
            return keyDict
    return ""


inText = ""
for line in open('input.txt', 'r', encoding='utf8'):
    inText = inText + line

wordList = list(inText.split())
dicList = {}
for i in range(0, len(wordList)):
    if dicList.get(wordList[i]) is None:
        addData = {wordList[i]: int(1)}
        dicList.update(addData)
    else:
        updData = {wordList[i]: int(dicList.get(wordList[i])) + int(1)}
        dicList.update(updData)

filterDict = {}
for key in dicList:
    if getKey(filterDict, dicList[key]) != "":
        updData = {key + " " + getKey(filterDict, dicList[key]): dicList[key]}
        filterDict.update(updData)
        del filterDict[getKey(filterDict, dicList[key])]
    else:
        addData = {key: dicList[key]}
        filterDict.update(addData)

sortedList = sorted(filterDict.items(), key=lambda kv: kv[1], reverse=True)

for j in range(0, len(sortedList)):
    print("\n".join(str(x) for x in sorted(sortedList[j][0].split(" "))))
