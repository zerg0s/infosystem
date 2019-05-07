# Created  by Maltsev Alexey
# 09.10.18
# Алгоритм Евклида

theA = int(input("Введите a: "))
theB = int(input("Введите b: "))
def gcd(theA, theB):
    if theA == 0 or theB == 0:
        return max(theA, theB)
    if theA > theB:
        return gcd(theA % theB, theB)
    if theA < b:
        return gcd(theA, theB % theA)
print(gcd(theA, theB))
