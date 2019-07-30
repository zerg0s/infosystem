#Created by Petr Gusev
#Number of appeared word
#07.11.2018

file = open("input.txt", "r", encoding = "utf-8")

dictWords = {}

for line in file:
    words = line.strip().split()
    for word in words:
        dictWords[word] = dictWords.get(word, -1) + 1

counts = dictWords.values()
print(*counts)
