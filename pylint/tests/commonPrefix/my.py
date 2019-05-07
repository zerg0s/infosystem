str1 = input()
str2 = input()
i = 0
common = 0
while i < min(len(str1), len(str2)):
    if str1[i].lower() == str2[i].lower():
        common += 1
    else:
        break
    i += 1
print(common)
