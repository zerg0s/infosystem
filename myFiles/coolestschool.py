# Created by Anita Kuzmina
# coolest_school
# 23.10.2018

schoolStatistics = {}
data = open('school.txt', 'r', encoding='utf-8')

for line in data.readlines():
    info = line.split()[-2:]
    school = info[0]
    score = info[1]
    if school in schoolStatistics:
        schoolStatistics[school][0] += 1
        schoolStatistics[school][1] += score
    else:
        schoolStatistics[school] = [1, score]

maxScore = max(schoolStatistics.items(), key=lambda x: x[1][0])[1][0]
filterMaxScore = list(filter(lambda x: x[1][0] == maxScore, schoolStatistics.items()))

for result in sorted(filterMaxScore, reverse=True):
    print(result[0], end=' ')
