# Created by Olesya Bandurina
# Date 23.10.2018
# Task Description: Сколько чисел содержится одновременно

print(list(set((int(j) for j in input().split())) & set((int(j) for j in input().split()))))
