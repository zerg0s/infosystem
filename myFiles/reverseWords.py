# Created by Anita Kuzmina
# reverse_words
# 23.09.2018

string = input("Enter two words: ")
words = string.split()
string = words[1] + ' ' + words[0]
print("Reversed words: ", string)
