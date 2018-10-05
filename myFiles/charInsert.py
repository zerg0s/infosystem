# Ильдар Галиуллин.
# Вставка символа.
# 23.09.2018.


def charInsert(strCh):
    str2 = ""
    for i in range(len(strCh)):
        str2 += strCh[i]
        if i != len(strCh) - 1:
            str2 += '*'
    return str2

str1 = "Python"
print(charInsert(str1))
