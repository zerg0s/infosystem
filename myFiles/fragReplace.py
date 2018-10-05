# Ильдар Галиуллин.
# Замена фрагмента.
# 23.09.2018.


def fragReplace(str1):
    start = str1[:str1.find('h') + 1]
    end = str1[str1.rfind('h'):]
    replace = str1[str1.find('h') + 1:str1.rfind('h')].replace('h', 'H')
    str1 = start + replace + end
    return str1

strRep = input("Enter the string: ")
count = 0
for i in range(len(strRep)):
    if strRep[i] == 'h':
        count += 1
if count <= 1:
    print(strRep)
else:
    print(fragReplace(strRep))
