# Created by Samohin Artem
# Date 2018-11-14
# Task Description: http://www.hostedredmine.com/issues/782447


def functionDeposit(clientName, sumAccount, clientDict):
    if not clientDict.get(clientName) is None:
        updateClient = {clientName: int(clientDict.get(clientName)) + int(sumAccount)}
        clientDict.update(updateClient)
    else:
        addClient = {clientName: sumAccount}
        clientDict.update(addClient)

    return clientDict


def functionWithdraw(clientName, sumAccount, clientDict):
    if not clientDict.get(clientName) is None:
        updateClient = {clientName: int(clientDict.get(clientName)) - int(sumAccount)}
        clientDict.update(updateClient)
    else:
        addClient = {clientName: int(sumAccount)*(-1)}
        clientDict.update(addClient)

    return clientDict


def functionBalance(clientName, clientDict, clientData):
    if not clientDict.get(clientName) is None:
        clientData.append(clientDict.get(clientName))
    else:
        clientData.append("ERROR")


def functionTransfer(clientName1, clientName2, sumAccount, clientDict):
    if not clientDict.get(clientName1) is None and not clientDict.get(clientName2) is None:
        updateClient = {clientName1: int(clientDict.get(clientName1)) - int(sumAccount)}
        clientDict.update(updateClient)
        updateClient = {clientName2: int(clientDict.get(clientName2)) + int(sumAccount)}
        clientDict.update(updateClient)
    if clientDict.get(clientName1) is None and not clientDict.get(clientName2) is None:
        addClient = {clientName1: int(sumAccount)*(-1)}
        clientDict.update(addClient)
        updateClient = {clientName2: int(clientDict.get(clientName2)) + int(sumAccount)}
        clientDict.update(updateClient)
    if not clientDict.get(clientName1) is None and clientDict.get(clientName2) is None:
        updateClient = {clientName1: int(clientDict.get(clientName1)) - int(sumAccount)}
        clientDict.update(updateClient)
        addClient = {clientName2: sumAccount}
        clientDict.update(addClient)
    if clientDict.get(clientName1) is None and clientDict.get(clientName2) is None:
        addClient = {clientName1: int(sumAccount)*(-1)}
        clientDict.update(addClient)
        addClient = {clientName2: sumAccount}
        clientDict.update(addClient)

    return clientDict


def functionIncome(allDeposit, clientDict):
    for key in clientDict:
        clientDict[key] = int(clientDict[key]) + int(allDeposit)
    return clientDict


def inputCommand(clientData):
    clientDict = {}
    inData = input()
    while inData != "":
        seqList = inData.split(" ")
        if seqList[0] == "DEPOSIT":
            functionDeposit(seqList[1], seqList[2], clientDict)
        if seqList[0] == "WITHDRAW":
            functionWithdraw(seqList[1], seqList[2], clientDict)
        if seqList[0] == "BALANCE":
            functionBalance(seqList[1], clientDict, clientData)
        if seqList[0] == "TRANSFER":
            functionTransfer(seqList[1], seqList[2], seqList[3], clientDict)
        if seqList[0] == "INCOME":
            functionIncome(seqList[1], clientDict)
        inData = input()
    return clientData

clientBalance = list()
clientBalance = inputCommand(clientBalance)
print("\n".join(str(x) for x in clientBalance))
