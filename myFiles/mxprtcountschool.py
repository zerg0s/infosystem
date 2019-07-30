# Ильдар Галиуллин.
# Школа с наибольшим количеством участников.
# 19.10.2018.

file = open('Schools.txt', 'r')
schools = []
scores = []
maxSchool = []
maxScore = []
maxPosScore = []
schoolNumber = []
count = 0
score = 0
for line in file.readlines():
    schools.append(int(line.split()[2]))
    scores.append(int(line.split()[3]))
for i in range(len(schools)):
    for j in range(i + 1, len(schools)):
        if schools[i] == schools[j]:
            score = scores[i]
            score += scores[j]
            count += 1
    maxSchool.append(count)
    maxScore.append(score)
    score = 0
    count = 0
maxPositions = [i for i, j in enumerate(maxSchool) if j == max(maxSchool)]
for i in maxPositions:
    schoolNumber.append(schools[i])
for i in maxPositions:
    maxPosScore.append(maxScore[i])
schoolsNscores = zip(schoolNumber, maxPosScore)
sNs = sorted(schoolsNscores, key=lambda tup: tup[1])
print([schoolsNscores[0] for schoolsNscores in sNs])
