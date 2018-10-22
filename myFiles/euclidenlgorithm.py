#Created by Grebneva Kseniya
#euclidean_algorithm
#12.10.2018

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print(a + b)

a = int(input('a = '))
b = int(input('b = '))
gcd(a, b)
