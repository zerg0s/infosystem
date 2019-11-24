import math

squares = ""

def innumb(somestr):
    numb = int(input())
    if (numb == 0):
        return somestr
    if (math.fabs(math.sqrt(numb) - int(math.sqrt(numb))) < 0.00001):
        return innumb("") + str(numb) + " "
    return somestr + innumb("")

squares = innumb(squares)

if (squares):
    squares = squares.rstrip(' ')
    print(squares)
else:
    print("0")
