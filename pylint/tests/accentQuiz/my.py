n1 = int(input())
stressDict = {}
for i in range(n1):
    word = input()
    if word.lower() not in stressDict:
        stressDict[word.lower()] = [word]
    else:
        stressDict[word.lower()].append(word)
amountMistakes = 0
petText = list(input().split())
for word in petText:
    if word.lower() in stressDict:
        isMistake = True
        for i in stressDict[word.lower()]:
            if word == i:
                isMistake = False
        if isMistake:
            amountMistakes += 1
    else:
        amountStressed = 0
        for now in list(word):
            if now.isupper():
                amountStressed += 1
        if amountStressed != 1:
            amountMistakes += 1
print(amountMistakes)
