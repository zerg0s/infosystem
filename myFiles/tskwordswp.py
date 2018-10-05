# Created by Mikhail Fadeev
# Task Description: Перестановка слов

sourceString = input("Enter two words: ")
print (sourceString[sourceString.find(' ') + 1:]\
       + ' ' +  sourceString[:sourceString.find(' ')])
