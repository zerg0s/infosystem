#Created by Petr Gusev
#Change 2 words
#01.10.2018

strWord = "Введите слово"

let = strWord.find(" ")

strNew = strWord[let + 1::] + strWord[let] + strWord[:let:]

print(strNew)
