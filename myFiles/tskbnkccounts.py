# Created by Mikhail Fadeev
# Task Description: Банковские счета

accounts = {}

file = open('input.txt', 'r', encoding='utf-8')
for line in file.readlines():
    linePart = line.split()

    if linePart[0] == "DEPOSIT":
        amount = accounts.setdefault(linePart[1], 0)
        accounts[linePart[1]] = amount + int(linePart[2])
    elif linePart[0] == "WITHDRAW":
        amount = accounts.setdefault(linePart[1], 0)
        accounts[linePart[1]] = amount - int(linePart[2])
    elif linePart[0] == "BALANCE":
        amount = accounts.get(linePart[1])
        if amount is not None:
            print(amount)
        else:
            print("ERROR")
    elif linePart[0] == "TRANSFER":
        accountAmountSrc = accounts.setdefault(linePart[1], 0)
        accounts[linePart[1]] = accountAmountSrc - int(linePart[3])
        accountAmountDest = accounts.setdefault(linePart[2], 0)
        accounts[linePart[2]] = accountAmountDest + int(linePart[3])
    elif linePart[0] == "INCOME":
        for accountFolder, amount in accounts.items():
            if amount > 0:
                accounts[accountFolder] = amount + int((amount / 100)\
                                                       * float(linePart[1]))
file.close()
