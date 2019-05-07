import os


def getListFromSource(openedFile):
    tmpList = list()
    for line in openedFile.readlines():
        for elem in line.split("\t"):
            if elem.strip() is not "":
                tmpList.append(elem)
    return tmpList


def writeToFile(fileName, whatToWrite):
    fTest = open(fileName, "w+")
    fTest.write(whatToWrite)
    fTest.close()


if __name__ == "__main__":
    dictOfTests = {}
    tempList = list()
    file = open("source.txt")
    #parse source file and return list
    tempList = getListFromSource(file)
    i = 0
    # create dictionary based on tests
    while i < len(tempList):
        dictOfTests[tempList[i]] = tempList[i+1]
        i += 2
    # print(*dictOfTests.items())
    i = 1
    dirTests = ".\\tests\\"
    
    for (testItem, testAnswer) in dictOfTests.items():
        writeToFile(f"{dirTests}test{i}.t", testItem)
        writeToFile(f"{dirTests}test{i}.a", testAnswer)
        i += 1

