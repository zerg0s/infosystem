# Ильдар Галиуллин.
# Вставка символа.
# 23.09.2018.

str1 = "Python"
str2 = ""
for i in range(len(str1)):
    if i % 3 != 0:
        str2 += str1[i]
print(str2)
