def sumw():
    numn = input()
    numn = int(numn)
    i = 0
    num = 0
    ssu = []
    while(numn > 0):
        ssu.append(numn % 10)
        numn = numn // 10
    while(i < len(ssu)):
        num += ssu[i]
        i += 1
    print(num)
