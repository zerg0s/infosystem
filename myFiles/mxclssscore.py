# Ильдар Галиуллин.
# Максимальный балл по классам.
# 18.10.2018.

file = open('ClassScore.txt', 'r')
file2 = open('ClassScore.txt', 'a')
classVals = []
scores = []
classMaxScore = 0
maxScore = 0
for line in file.readlines():
    classVals.append(int(line.split()[2]))
    scores.append(int(line.split()[3]))
for i in range(len(classVals)):
    if classVals[i] == 9:
        if maxScore < scores[i]:
            maxScore = scores[i]
print(maxScore)
maxScore = 0
for i in range(len(classVals)):
    if classVals[i] == 10:
        if maxScore < scores[i]:
            maxScore = scores[i]
print(maxScore)
maxScore = 0
for i in range(len(classVals)):
    if classVals[i] == 11:
        if maxScore < scores[i]:
            maxScore = scores[i]
print(maxScore)
