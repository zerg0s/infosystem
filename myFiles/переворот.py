def pr(str1):
    tt = []
    s = str1.split(' ')
    s[0],s[1] = s[1],s[0]
    tt.append(s[0])
    tt.append(' ')
    tt.append(s[1])
    ss = ''.join(tt)
    print(ss)
