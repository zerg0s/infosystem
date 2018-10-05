# Ильдар Галиуллин.
# Перестановка слов.
# 23.09.2018.


def wordReplace(str1):
    list1 = str1.split()
    str2 = ""
    str2 = list1[1] + " " + list1[0]
    return str2

strRep = "Hello, world!"
print(wordReplace(strRep))
