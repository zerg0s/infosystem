# Created by Anita Kuzmina
# Palindromes
# 16.09.2018

k = int(input("Enter k: "))
count = 0

for i in range(1, k + 1):
    if str(i) == str(i)[::-1]:
        count = count + 1

print(count)