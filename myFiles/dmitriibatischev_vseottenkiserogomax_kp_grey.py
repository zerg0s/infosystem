import re

myStr = input()
myStr = myStr.lower()

if myStr[0] == "#" and len(myStr) == 6:
    newStr = "#0" + myStr[1:6]
    myStr = newStr

if myStr[0] == "#" and len(myStr) == 7:
    if myStr[1:7] == "000000" or myStr[1:7] == "ffffff":
        print("False")
        exit()
    if myStr[1:3] == myStr[3:5] == myStr[5:7]:
        print("True")
        exit()
    else:
        print("False")
        exit()
elif myStr[0] == "#" and len(myStr) == 4:
    if myStr[1:7] == "000" or myStr[1:7] == "fff":
        print("False")
        exit()
    if myStr[1] == myStr[2] == myStr[3]:
        print("True")
        exit()
    else:
        print("False")
        exit()

myType = re.findall(r'rgba', myStr)
if myType == []:
    myType = re.findall(r'rgb', myStr)
if myType == []:
    myType = re.findall(r'hsla', myStr)
if myType == []:
    myType = re.findall(r'hsl', myStr)

    # print("1234")
# print(myType)


if myType[0] != "hsl" and myType[0] != "hsla":
    if myType[0] == "rgba":
        res = re.findall(r'(\s*\d+(\.\d+)?\s*)\,(\s*\d+(\.\d+)?\s*)\,(\s*\d+(\.\d+)?\s*)\,(\s*\d+(\.\d+)?\s*)', myStr)
        # print(res)
    else:
        res = re.findall(r'(\s*\d+(\.\d+)?\s*)\,(\s*\d+(\.\d+)?\s*)\,(\s*\d+(\.\d+)?\s*)', myStr)
    # print(res)
    res1 = (float(res[0][0]))
    res2 = (float(res[0][2]))
    res3 = (float(res[0][4]))
    if res1 == 0 or res1 == 255:
        print("False")
    elif res1 == res2 == res3:
        print("True")
    else:
        print("False")
else:
    if myType[0] == "hsla":
        res = re.findall(r'(\s*\d+\s*)\,(\s*\d+%\s*)\,(\s*\d+%\s*)\,(\s*\d+%?\s*)', myStr)
        # print(res)
    else:
        res = re.findall(r'(\s*\d+\s*)\,(\s*\d+%\s*)\,(\s*\d+%\s*)', myStr)
    # print(res)
    res1 = (int(res[0][0]))
    res2 = (int(res[0][1][:-1]))
    res3 = (int(res[0][2][:-1]))
    if res1 != 0 or res2 != 0:
        print("False")
    elif res3 == 0 or res3 == 100:
        print("False")
    else:
        print("True")
