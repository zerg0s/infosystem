# Created by Olesya Bandurina
# Date 20.10.2018
# Task Description: Сколько школьников сможет одновременно покататься

import bisect

str1 = sorted([int(i) for i in input().split()])
str2 = sorted([int(i) for i in input().split()])
w = 0
n = -1
for i in str2:
    n = bisect.bisect_left(str1, i, n + 1)
    if n < len(str1):
        w += 1
    else:
        break
print(w)
