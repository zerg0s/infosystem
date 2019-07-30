def bank():
    text = input()
    dicti = {}
    balance = []
    i = 0
    while(text != ''):
        mas = text.split()
        if(mas[0] == 'DEPOSIT'):
            dicti[mas[1]] = int(mas[2])
        if(mas[0] == 'TRANSFER'):
            if(dicti.get(mas[1]) is None and dicti.get(mas[2]) is None):
                dicti[mas[2]] = int(mas[3])
                dicti[mas[1]] = -int(mas[3])
            elif(dicti.get(mas[1]) is None and dicti.get(mas[2]) is not None):
                dicti[mas[1]] = -int(mas[3])
                dicti[mas[2]] = dicti.get(mas[2]) + int(mas[3])
            elif(dicti.get(mas[2]) is None and dicti.get(mas[1]) is not None):
                dicti[mas[2]] = int(mas[3])
                dicti[mas[1]] = int(dicti.get(mas[1])) - int(mas[3])
            else:
                dicti[mas[1]] = dicti.get(mas[1]) + int(mas[3])
                dicti[mas[2]] = dicti.get(mas[2]) - int(mas[3])
        if(mas[0] == 'WITHDRAW'):
            if(dicti.get(mas[1]) is None):
                dicti[mas[1]] = - int(mas[2])
            else:
                dicti[mas[1]] = dicti.get(mas[1]) - int(mas[2])
        if(mas[0] == 'INCOME'):
            for key in dicti:
                dicti[key] = dicti.get(key) + int(mas[1])
        if(mas[0] == 'BALANCE'):
            if(dicti.get(mas[1]) is None):
                balance.append('ERROR')
            else:
                balance.append(dicti.get(mas[1]))
        text = input()
    while(i < len(balance)):
        print(balance[i])
        i += 1

if __name__ == "__main__":
    bank()
