#Created by Grebneva Kseniya
#perfect_performer
#21.09.2018

while True:
    
    A = int(input("Введите число А: "))
    B = int(input("Введите число В<A: "))
    
    if(A > B):
        while(A != B):
            C = A
            if(A % 2 == 0):
                A = C // 2
                if(A >= B):
                    print(':2')
                else:
                    A = C - 1
                    print('-1')
            else:
                A = C - 1
                print('-1')
        break
    else:
        print("B не меньше A.")
