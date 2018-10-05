#Created by Petr Gusev
#Change h letter to H
#02.10.2018

stroka = "In the hole in the ground there lived a hobbit."

hFirst = stroka.find("h")
hLast = stroka.rfind("h")

final = stroka[:hFirst + 1:] + stroka[hFirst + 1:hLast:].replace("h", "H") + stroka[hLast::]

print(final)
