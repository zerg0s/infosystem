# Created by Mikhail Fadeev
# Task Description: Замена фрагмента

sourceString = input("Enter string: ")

replacedString = sourceString[:sourceString.find('h') + 1]\
               + sourceString[sourceString.find('h')\
                              + 1:sourceString.rfind('h')].replace('h', 'H')\
                              + sourceString[sourceString.rfind('h'):]

print(replacedString)
