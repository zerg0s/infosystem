# Created by Alexey Maltsev
# 3.10.18
# Заменить все на , кроме первого и последнего

stroka1 = "In the hole in the ground there lived a hobbit."
First = stroka1.find("h")
End = stroka1.rfind("h")
stroka2 = stroka1[:First + 1] + stroka1[First + 1: End].replace('h', 'H') + stroka1[End:]
print(stroka2)
