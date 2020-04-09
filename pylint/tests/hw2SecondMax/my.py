maxVal = 0
maxSecVal = 0
i = -1
while True:
    i = int(input())
    if i == 0:
        break
    if i >= maxVal:
        maxSecVal = maxVal
        maxVal = i
    elif i > maxSecVal:
        maxSecVal = i
print(maxSecVal)
