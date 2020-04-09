import re

myStr = "myMail@gmail.com, company@xerox.co.uk"
'''
myStr1=myStr.split(',')
print(myStr1)
myStr2=[]
for i in range(len(myStr1)):
    myStr2.append(myStr1[i].split('@'))
print(myStr2)
print(len(myStr2))
myStr3=[]
for i in range(len(myStr2)):
    myStr3.append(myStr2[i][1])
print(myStr3)
res = re.findall(r'\w+\.\w+$', myStr1[0])
'''
print(myStr)
# res=re.findall(r'(@\w+\.\w+)+(\.\w+)?', myStr)
res = re.findall(r'(@(\w+)?(\.\w+)?(\.\w+)?(\.\w+)?)', myStr)
# print(res)
for i in range(len(res)):

    if res[i][4] != "":
        print(res[i][4][1:len(res[i][4])])
        print(res[i][3][1:len(res[i][3])] + res[i][4])
    elif res[i][3] != "":
        print(res[i][3][1:len(res[i][3])])
        print(res[i][2][1:len(res[i][2])] + res[i][3])
    elif res[i][2] != "":
        print(res[i][2][1:len(res[i][2])])
        print(res[i][1][0:len(res[i][1])] + res[i][2])
    else:
        print(res[i][1][1:len(res[i][1])])
'''
for i in range(0, len(res)):
    print(res[i][:-1])
'''
