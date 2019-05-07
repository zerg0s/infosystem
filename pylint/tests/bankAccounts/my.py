inFile = open('input.txt', 'r', encoding='utf-8')
outFile = open('output', 'w', encoding='utf-8')


def deposit(dic, name, summ):
    if(name in dic):
        dic[name] += int(summ)
    else:
        dic[name] = int(summ)
    return dic


def withdraw(dic, name, summ):
    if(name in dic):
        dic[name] -= int(summ)
    else:
        dic[name] = -int(summ)
    return dic


def balance(dic, name):
    if name in dic:
        print(dic[name])
    else:
        print('ERROR')
    return dic


def income(dic, profit):
    for i in dic:
        if dic[i] > 0:
            dic[i] += dic[i] * profit / 100
            dic[i] = int(dic[i])
    return dic


def main():
    dic = {}
    for line in inFile:
        mlist = line.split()
        if mlist[0] == 'DEPOSIT':
            dic = deposit(dic, mlist[1], int(mlist[2]))
        if mlist[0] == 'WITHDRAW':
            dic = withdraw(dic, mlist[1], int(mlist[2]))
        if mlist[0] == 'BALANCE':
            dic = balance(dic, mlist[1])
        if mlist[0] == 'TRANSFER':
            dic = deposit(dic, mlist[2], int(mlist[3]))
            dic = withdraw(dic, mlist[1], int(mlist[3]))
        if mlist[0] == 'INCOME':
            dic = income(dic, int(mlist[1]))


main()
inFile.close()
outFile.close()
