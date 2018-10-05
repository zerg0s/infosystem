#Created by Grebneva Kseniya
#number_of_palindromes
#22.09.2018

K = str(input("Введите целое число от 1 до 100000: "))
K = int(K)
numP = 0
if (K > 1 and K < 100000):
    P = 1
    while P in range(K):
        invP = str(P)
        if(invP[::-1] == invP):
            numP = numP + 1
        P = P + 1
    print(numP)
else:
    print("Условие: 1 < K < 100000")
