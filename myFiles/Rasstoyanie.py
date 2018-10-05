x = 1
arr = []
while x:
 x = int(input())
 arr += [x]
max_arr = max(arr)
f_index = arr.index(max_arr)
l_index = arr[::-1].index(max_arr)
print(l_index - f_index + 1)
