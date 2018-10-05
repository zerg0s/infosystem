# Created by Fedyuk Yuliya
# SwapWords
# 3.10.2018
s = input("Введите 2 слова через пробел: ")
firstWord = s[:s.find(' ')]
secondWord = s[s.find(' ') + 1:]
print(secondWord + ' ' + firstWord)
