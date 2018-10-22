# Created by Mikhail Fadeev
# Task Description: Ферзи

def checkQueensSet(queensList):
    for chessIndex in range(8):
        for extIndex in range(8):
            if chessIndex == extIndex:
                continue
            if queensList[chessIndex][0] == queensList[extIndex][0] or\
               queensList[chessIndex][1] == queensList[extIndex][1] or\
               (abs(queensList[extIndex][0] - queensList[chessIndex][0]) ==\
                abs(queensList[extIndex][1] - queensList[chessIndex][1])):
                return True
    return False

queens = []
for inputCount in range(8):
    values = input()
    values = values.split()
    queens.append((int(values[0]), int(values[1])))

if checkQueensSet(queens):
    print("YES")
else:
    print("NO")

