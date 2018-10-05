# Created by Anita Kuzmina
# each_third_symbol_deleting
# 23.09.2018

string = input("Enter string: ")
newString = ""

for i in range(len(string)):
    if i % 3 != 0:
        newString = newString + string[i]

print("New string: ", newString)