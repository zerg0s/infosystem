import re


def getDates():
    d1 = ""
    s = open('input.txt')
    for line in s.readlines():
        d = re.findall(r'(1\d{3}|200\d|201[0-2])[/](0[1-9]|1[012])[/](0[1-9]|[12]\d|30)'
                       r'(\s+\d[0-24]\:\d[0-59]\:?\d?[0-59]?)?', line)

        if len(d) != 0:
            if d[0][3] == "":
                d1 += "/".join(d[0][:3]) + '\n'
            else:
                d1 += "/".join(d[0][:-1])
                d1 += " " + d[0][-1] + '\n'
                d1 = d1.replace('  ', ' ')
        else:
            continue
    return d1


str1 = getDates()
print(str1)
