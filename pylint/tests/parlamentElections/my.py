fin = open("input.txt")
dS = {}
d1 = {}
cnt = 0
i = 0
for s1 in fin.readlines():
    s1 = s1.strip().split()
    s1 = [" ".join(s1[:-1]), int(s1[-1])]
    cnt += s1[1]
    dS[s1[0]] = s1[1]
    d1[i] = s1[0]
    i += 1
d2 = []
su = 0
k = cnt / 450
for t in dS:
    d2.append([-(dS[t] / k - int(dS[t] / k)), t, int(dS[t] / k)])
    su += d2[-1][2]
if su < 450:
    for t in sorted(d2):
        if su == 450:
            break
        t[2] += 1
        su += 1
for t in d2:
    dS[t[1]] = t[2]
for t in sorted(d1):
    print(d1[t], dS[d1[t]])
	