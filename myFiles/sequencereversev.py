# Created by Anita Kuzmina
# sequence_reverse
# 28.09.2018


def reverseSequence():
    num = int(input("Enter number (0 for stop): "))
    if num != 0:
        reverseSequence()
    print(num)


reverseSequence()
