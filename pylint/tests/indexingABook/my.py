import re, sys

dictWord = {}
lst = []
for tmp in sys.stdin.readlines():
    lst.append(tmp)
word = ''
pWord = re.compile(r"[0-9]+")
pPage = re.compile(r"[^0-9]+")
counter = 0
for i in lst:
    word = pWord.split(i)[0].strip()
    page = int(pPage.split(i)[1])
    if page not in dictWord:
        dictWord[page] = [word]
    else:
        dictWord[page].append(word)
    counter += 1

dictWordSorted = sorted(dictWord.items(), key=lambda x: x[0])

for i, j in dictWordSorted:
    print(i, *sorted(set(j)))
