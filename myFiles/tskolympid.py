from collections import Counter

schoolNum = list()
schoolMark = list()
for line in open('for_task3\olympaid_res.txt', encoding='utf8'):
    line = line.replace('\n', '').split(' ')
    schoolNum.append(line[2])
    line.pop(1)
    line.pop(0)
    schoolMark.append(line)

count = Counter(schoolNum)
max_cnt = max(schoolNum)
total = schoolNum.count(max_cnt)
most_common = count.most_common(total)

i = 0
while i != len(schoolMark):
    if not (schoolMark[i][0] in
            [most_common[index][0] for index in range(0, len(most_common))]):
        schoolMark.pop(i)
        continue
    i += 1

finalList = list()
i = 0
j = 0
while i != len(schoolMark) - 1:
    j = i + 1
    while j != len(schoolMark):
        if int(schoolMark[i][0]) == int(schoolMark[j][0]):
            finalList.append([int(schoolMark[i][0]), int(schoolMark[i][1]) +
                              int(schoolMark[j][1])])
        j += 1
    i += 1

finalList = sorted(finalList, key=lambda k: k[1])
print(" ".join(str(x) for x in
               set(finalList[i][0]for i in range(len(finalList) - 1, -1, -1))))
