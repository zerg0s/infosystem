import re
def getDates(filename):
    inText = ""
    for line in open(filename, 'r', encoding='utf8'):
        inText = inText + line
    regexp =\
        r'\d{4}/\d{2}/\d{2}\s\d\d:\d\d:\d\d|\d{4}/\d\d/\d\d\s\d\d:\d\d|\d{4}/\d\d/\d\d'
    searchList = re.findall(regexp, inText)
    outputList = list()
    for i in range(0, len(searchList)):
        if int(searchList[i][0:4]) >= 1000 and int(searchList[i][0:4]) <= 2012:
            outputList.append(searchList[i])
    return outputList
if __name__ == "__main__":
    print("\n".join(str(x) for x in getDates('input.txt')))
	