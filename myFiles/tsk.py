# Created by Samohin Artem
# Date 2018-10-20
# Task Description: http://www.hostedredmine.com/issues/780861

firstStr = input()
secondStr = input()
fList = firstStr.split(' ')
sList = secondStr.split(' ')
fLot = set(fList)
sLot = set(sList)
finalList = sLot.intersection(fLot)
print(len(finalList))
