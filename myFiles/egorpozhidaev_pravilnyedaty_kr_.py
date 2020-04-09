import re

def getDates(filename):
    result = []
    filein = open(filename, 'r', encoding='utf8')
    patt = re.compile(r"(\d\d\d\d)[/]\d\d[/]\d\d(?:\s(?:\d\d)?(?:[:]\d\d)?(?:[:]\d\d)?)?")
    for line in filein:
        respat = patt.finditer(line)
        if respat:
            for respats in respat:
                dateif = int(respats.group(1))
                if (dateif <= 2012 and dateif >= 1000):
                    result.append(respats.group())
    filein.close()
    return result

if __name__ == '__main__':
    dateresult = getDates('input.txt')
    for resd in dateresult:
        print(resd)
