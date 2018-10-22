#Created by Grebneva Kseniya
#reversal_of_the_sequence
#15.10.2018

def turn():
    seqRev = int(input())
    if seqRev != 0:
        turn()
        print(seqRev)
    else:
        print(0)

print("Введите числа, отделяя строки нажатием Enter, "
      "в последней строке введите 0")
turn()
