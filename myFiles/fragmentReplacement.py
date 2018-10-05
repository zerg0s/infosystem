# Created by Anita Kuzmina
# fragment_replacement
# 23.09.2018

string = input("Enter string: ")

leftH = string.find('h')
rightH = string.rfind('h')

if leftH >= 0 and rightH >=0 and leftH < rightH:
    print(string[:leftH + 1] + string[leftH + 1:rightH].replace('h', 'H') + string[rightH:])
else:
    print(string)
