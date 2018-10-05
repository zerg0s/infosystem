#Created by Petr Gusev
#Delete every third symbol
#02.10.2018

stroka = "Клюшка,краги,коньки,визор,ракушка,гамаши"
newStroka = ""
i = 0
while i < len(stroka):
    if i % 3 != 0:
        newStroka += stroka[i]
    i += 1

print(newStroka)
