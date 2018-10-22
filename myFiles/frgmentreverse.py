# Created by Anita Kuzmina
# fragment_reverse
# 16.09.2018

string = input("Enter string: ")

firstH = string[:string.find('h')]
betweenH = string[string.find('h'):string.rfind('h') + 1]
lastH = string[string.rfind('h') + 1:]

print(firstH + betweenH[::-1] + lastH)
