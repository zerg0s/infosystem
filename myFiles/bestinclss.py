# Created by Anita Kuzmina
# best_in_class
# 23.10.2018

from collections import defaultdict

schoolStatistics = defaultdict(list)
data = open('input.txt', 'r', encoding='utf-8')

for line in data.readlines():
    info = line.split()[-2:]
    classNo = info[0]
    score = info[1]
    schoolStatistics[classNo].append(score)

print(*(max(schoolStatistics[k]) for k in sorted(schoolStatistics.keys())))
