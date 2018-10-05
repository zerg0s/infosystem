# Мария Евсеева
# Спички

m1l = int(input("Введите левую позицию первой спички: "))
m1r = int(input("Введите правую позицию первой спички: "))

m2l = int(input("Введите левую позицию второй спички: "))
m2r = int(input("Введите правую позицию второй спички: "))

m3l = int(input("Введите левую позицию третьей спички: "))
m3r = int(input("Введите правую позицию третьей спички: "))

if (m1r < m1l) or (m1l < 0) or (m1r > 100):
    print(-1)
elif (m2r < m2l) or (m2l < 0) or (m2r > 100):
    print(-1)
elif (m3r < m3l) or (m3l < 0) or (m3r > 100):
    print(-1)
else:
    lengthM1 = m1r - m1l
    lengthM2 = m2r - m2l
    lengthM3 = m3r - m3l

    isContactM1M2 = m2l <= m1r and m2r >= m1l
    isContactM1M3 = m3l <= m1r and m3r >= m1l
    isContactM2M3 = m3l <= m2r and m3r >= m2l

    if isContactM1M2:
        distanceM1M2 = 0
    elif m1r < m2l:
        distanceM1M2 = m2l - m1r
    else:
        distanceM1M2 = m1l - m2r

    if isContactM1M3:
        distanceM1M3 = 0
    elif m1r < m3l:
        distanceM1M3 = m3l - m1r
    else:
        distanceM1M3 = m1l - m3r

    if isContactM2M3:
        distanceM2M3 = 0
    elif m2r < m3l:
        distanceM2M3 = m3l - m2r
    else:
        distanceM2M3 = m2l - m3r

    if isContactM1M2 and (isContactM2M3 or isContactM1M3):
        print(0)
    elif isContactM1M3 and (isContactM1M2 or isContactM2M3):
        print(0)
    elif isContactM2M3 and (isContactM1M2 or isContactM1M3):
        print(0)
    elif isContactM2M3 or ((not isContactM2M3) and distanceM2M3 <= lengthM1):
        print(1)
    elif isContactM1M3 or ((not isContactM1M3) and distanceM1M3 <= lengthM2):
        print(2)
    elif isContactM1M2 or ((not isContactM1M2) and distanceM1M2 <= lengthM3):
        print(3)
    else:
        print(-1)
