def find_schools():
    f = open('school1.txt', 'r')
    ss = f.read()
    st = ss.split('\n')
    sst = []
    i = 0
    j = 0
    sc2 = []
    mm  = 0
    schools = []
    while(i < len(st)):
        ty = st[i].split(' ')
        if(len(ty) > 2):
            sst.append(ty[2])
        i+=1
    i = 0
    while(i < len(sst)):
        sc2.append(sst.count(sst[i]))
        i += 1
    i = 0
    j = 0
    mm = max(sc2)
    schools.append(sst[sc2.index(max(sc2))])
    while(i < len(sc2)):
        while(j < len(sst)):
            if(sst[sc2.index(max(sc2))] != sst[j] and sst.count(sst[j]) == mm):
                schools.append(sst[j])
            j += 1
        i += 1
    result = set(schools)  
    print(result)
    f.close()
