#Исхаков Дамир
#Алгоритм Евклида
#02.10.2018
aone = int(input())
btwo = int(input())
def gcd(aone, btwo):
    if aone == 0:
        return btwo
    elif btwo == 0:
        return aone
    elif aone > btwo:
        return gcd(aone % btwo, btwo)
    else:
        return gcd(aone, btwo % aone)
print(gcd(aone, btwo))
