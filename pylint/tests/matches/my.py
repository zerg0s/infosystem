l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
n1, n2, n3 = 1, 2, 3
if l1 > l2:
    l1, r1, l2, r2 = l2, r2, l1, r1
    n1, n2 = n2, n1
if l2 > l3:
    l2, r2, l3, r3 = l3, r3, l2, r2
    n2, n3 = n3, n2
if l1 > l2:
    l1, r1, l2, r2 = l2, r2, l1, r1
    n1, n2 = n2, n1

if r1 >= l2 and (r1 >= l3 or r2 >= l3):
    print(0)
else:
    ans = 4
    if r1 - l1 >= l3 - r2 and ans > n1:
        ans = n1
    if r2 - l2 >= l3 - r1 and ans > n2:
        ans = n2
    if r3 - l3 >= l2 - r1 and ans > n3:
        ans = n3
    if ans == 4:
        print(-1)
    else:
        print(ans)
