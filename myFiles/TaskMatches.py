# Created by Mikhail Fadeev
# Task Description: Спички

inputValue = input("Enter left position of first match = ")
if (inputValue.isdigit()):
    leftFirstMatch = int(inputValue)
    if (leftFirstMatch < 0) or (100 < leftFirstMatch):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter right position of first match = ")
if (inputValue.isdigit()):
    rightFirstMatch = int(inputValue)
    if (rightFirstMatch < leftFirstMatch) or (100 < rightFirstMatch):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter left position of second match = ")
if (inputValue.isdigit()):
    leftSecondMatch = int(inputValue)
    if (leftSecondMatch < 0) or (100 < leftSecondMatch):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter right position of second match = ")
if (inputValue.isdigit()):
    rightSecondMatch = int(inputValue)
    if (rightSecondMatch < leftSecondMatch) or (100 < rightSecondMatch):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter left position of third match = ")
if (inputValue.isdigit()):
    leftThirdMatch = int(inputValue)
    if (leftThirdMatch < 0) or (100 < leftThirdMatch):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

inputValue = input("Enter right position of third match = ")
if (inputValue.isdigit()):
    rightThirdMatch = int(inputValue)
    if (rightThirdMatch < leftThirdMatch) or (100 < rightThirdMatch):
        print("Invalid input value!")
        exit()
else:
    print("Invalid input value!")
    exit()

isFirstAndSecondMatchesNearby = leftSecondMatch <= rightFirstMatch\
    and rightSecondMatch >= leftFirstMatch
isFirstAndThirdMatchesNearby = leftThirdMatch <= rightFirstMatch\
    and rightThirdMatch >= leftFirstMatch
isSecondAndThirdMatchesNearby = leftThirdMatch <= rightSecondMatch\
    and rightThirdMatch >= leftSecondMatch

if (isFirstAndSecondMatchesNearby and (isFirstAndThirdMatchesNearby\
        or isSecondAndThirdMatchesNearby)) or (isFirstAndThirdMatchesNearby\
        and (isFirstAndSecondMatchesNearby or isSecondAndThirdMatchesNearby))\
        or (isSecondAndThirdMatchesNearby and (isFirstAndSecondMatchesNearby\
        or isFirstAndThirdMatchesNearby)):
    print(0)
else:
    if rightFirstMatch < leftSecondMatch:
        spaceBetweenFirstAndSecondMatches = leftSecondMatch - rightFirstMatch
    else:
        spaceBetweenFirstAndSecondMatches = leftFirstMatch - rightSecondMatch
    
    if rightFirstMatch < leftThirdMatch:
        spaceBetweenFirstAndThirdMatches = leftThirdMatch - rightFirstMatch
    else:
        spaceBetweenFirstAndThirdMatches = leftFirstMatch - rightThirdMatch
    
    if rightSecondMatch < leftThirdMatch:
        spaceBetweenSecondAndThirdMatches = leftThirdMatch - rightSecondMatch
    else:
        spaceBetweenSecondAndThirdMatches = leftSecondMatch - rightThirdMatch
    
    if isSecondAndThirdMatchesNearby or (not isSecondAndThirdMatchesNearby\
            and spaceBetweenSecondAndThirdMatches\
            <= (rightFirstMatch - leftFirstMatch)):
        print(1)
    elif isFirstAndThirdMatchesNearby or (not isFirstAndThirdMatchesNearby\
            and spaceBetweenFirstAndThirdMatches\
            <= (rightSecondMatch - leftSecondMatch)):
        print(2)
    elif isFirstAndSecondMatchesNearby or (not isFirstAndSecondMatchesNearby\
            and spaceBetweenFirstAndSecondMatches\
            <= (rightThirdMatch - leftThirdMatch)):
        print(3)
    else:
        print(-1)
