# Ильдар Галиуллин.
# Разворот последовательности.
# 26.09.2018.


def reverse():
    sequence = int(input("Введите числа: "))
    if sequence != 0:
        reverse()
    print(sequence)
    return 0


reverse()
