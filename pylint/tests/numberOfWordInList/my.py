inFile = open('input.txt', 'r', encoding='utf8')


def printNumbers(line, wordsDict):
    words = list(map(str, line.split()))
    for word in words:
        if word not in wordsDict:
            wordsDict[word] = 0
        print(wordsDict[word], end=' ')
        wordsDict[word] += 1


def main():
    wordsDict = {}
    lines = inFile.readlines()
    for line in lines:
        line = line.strip()
        printNumbers(line, wordsDict)
    inFile.close()

if __name__ == "__main__":
    main()
