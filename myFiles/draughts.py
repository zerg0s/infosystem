#Done by Danilova Irina
#When 18.09.2018
#Task: If checker can reach a set cell without becoming a 'queen'

startCellVertical = int(input("Set first cell vertical: "))
startCellHorizontal = int(input("Set first cell horizontal: "))
endCellVertical = int(input("Set end cell vertical: "))
endCellHorizontal = int(input("Set end cell horizontal: "))

if (startCellHorizontal < endCellHorizontal and
    (endCellHorizontal-startCellHorizontal >= abs(endCellVertical-startCellVertical)) and
    ((startCellVertical % 2 == endCellVertical % 2 and (endCellHorizontal-startCellHorizontal) % 2 == 0) or
    (startCellVertical % 2 != endCellVertical % 2 and (endCellHorizontal-startCellHorizontal) % 2 != 0))
):
    print("YES")
else:
    print("NO")