# Created by Anita Kuzmina
# each_third_symbol_deleting
# 23.09.2018

string = input("Enter string: ")
newString = ""
strLen = len(string)

for i in range(strLen):
    if i % 3 != 0:
        newString = newString + string[i]

print("New string: ", newString)
