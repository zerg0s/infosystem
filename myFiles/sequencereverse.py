# Created by Anita Kuzmina
# sequence_reverse
# 30.09.2018


def reverse_sequence():
    num = int(input("Enter number (0 for stop): "))
    if num != 0:
        reverse_sequence()
    print(num)


reverse_sequence()
