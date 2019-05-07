
# Created by Anita Kuzmina
# time2
# 16.03.2019
import re
def getDates():
    strings = open('input.txt', 'r', encoding='utf-8')
    for sentence in strings.readlines():
        number = re.findall(r'([0-9]{4})/(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])'
                            r'( (2[0-3]|[01][0-9]):([0-5][0-9])(:([0-5][0-9]))?)?', sentence)
        for num in number:
            if 1000 <= int(num[0]) <= 2012:
                print(num[0] + '/' + num[1] + '/' + num[2]
                      + (' ' + num[3] if num[3] else ''))
    strings.close()
getDates()