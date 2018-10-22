#Created by Grebneva Kseniya
#the_number_of_matching_pairs
#19.10.2018

a = input().split()
k = 0

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            k = k + 1
print(k)
