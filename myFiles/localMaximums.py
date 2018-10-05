# Created by Anita Kuzmina
# Local maximums
# 16.09.2018

print("Enter numbers: ")

prevNum = int(input())
dist = 0
currDist = 0
minDist = 0

if prevNum != 0:
    currNum = int(input())
    if currNum != 0:
        nextNum = int(input())
        pos = 2
        while nextNum:
            if prevNum < currNum and currNum > nextNum:
                if dist != 0:
                    currDist = pos - dist
                    if minDist == 0:
                        minDist = currDist
                    else:
                        minDist = min(currDist, minDist)
                dist = pos
            pos = pos + 1
            prevNum = currNum
            currNum = nextNum
            nextNum = int(input())

print("Minimal distance: ", minDist)