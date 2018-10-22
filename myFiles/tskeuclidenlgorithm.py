# Created by Mikhail Fadeev
# Task Description: Алгоритм Евклида

def gcd(aValue, bValue):
    if aValue > bValue:
        return gcd(aValue - bValue, bValue)
    if aValue < bValue:
        return gcd(aValue, bValue - aValue)
    return aValue

aInputValue = int(input("Enter \"a\" value = "))
bInputValue = int(input("Enter \"b\" value = "))

print(str(gcd(aInputValue, bInputValue)))
