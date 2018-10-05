# Created by Anita Kuzmina
# *_adding
# 23.09.2018

string = input("Enter string: ")
newString = ""

for i in range(len(string)-1):
    newString = newString + string[i] + "*"

newString = newString + string[len(string)-1]

print("String with *: ", newString)
