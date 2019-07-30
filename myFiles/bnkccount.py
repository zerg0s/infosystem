# Created by Fedyuk Yuliya
# bankAccount
# 11.11.2018


def depositAcc(dict, nam, amoun):
    if nam in dict.keys():
        dict[nam] += amoun
    else:
        dict = {nam: amoun}
    return dict


def withdrawAcc(dict, nam, amoun):
    if nam in dict.keys():
        dict[nam] -= amoun
    else:
        dict = {nam: 0}
        dict[nam] -= amoun
    return dict


def balanceAcc(dict, nam):
    if nam in dict.keys():
        return dict[nam]
    else:
        return "ERROR"


def transferAcc(dict, nam1, nam2, amoun):
    if nam1 in dict.keys():
        dict[nam1] -= amoun
        if nam2 in dict.keys():
            dict[nam2] += amoun
        else:
            dict.update(depositAcc(dict, nam2, 0))
            dict[nam2] += amoun
    else:
        dict.update(depositAcc(dict, nam1, 0))
        dict[nam1] -= amoun
        if nam2 in dict.keys():
            dict[nam2] += amoun
        else:
            dict.update(depositAcc(dict, nam2, 0))
            dict[nam2] += amoun
    return dict


def incomeAcc(dict, amoun):
    for k in dict.keys():
        dict[k] += amoun
    return dict


myDict = {}
str1 = "start"
endList = []
while str1 != '':
    str1 = input()
    action = ""
    name = ""
    name1 = ""
    name2 = ""
    amount = ""
    it = 0
    for i in range(len(str1)):
        if str1[i] == ' ':
            action = str1[:i]
            it = i + 1
            break
    if action != "TRANSFER":
        if action != "INCOME" or action != "BALANCE":
            for i in range(it, len(str1)):
                if str1[i] == ' ' or str1[i] == str1[-1]:
                    name = str1[it:i]
                    break
        if action == "BALANCE":
            for i in range(it, len(str1)):
                if str1[i] == ' ' or str1[i] == str1[-1]:
                    name = str1[it:]
                    break
        if action != "BALANCE":
            for i in range(len(str1)):
                if str1[-i] == ' ':
                    amount = int(str1[-i+1:])
                    break
        if action == "DEPOSIT":
            myDict.update(depositAcc(myDict, name, amount))
        elif action == "WITHDRAW":
            myDict.update(withdrawAcc(myDict, name, amount))
        elif action == "BALANCE":
            endList.append(balanceAcc(myDict, name))
        elif action == "INCOME":
            myDict.update(incomeAcc(myDict, amount))
    else:
        for i in range(it, len(str1)):
            if str1[i] == ' ':
                name1 = str1[it:i]
                it = i + 1
                break
        for i in range(it, len(str1)):
            if str1[i] == ' ':
                name2 = str1[it:i]
                it = i + 1
                break
        for i in range(len(str1)):
            if str1[-i] == ' ':
                amount = int(str1[-i+1:])
                break
        myDict.update(transferAcc(myDict, name1, name2, amount))
for i in endList:
    print(i)
