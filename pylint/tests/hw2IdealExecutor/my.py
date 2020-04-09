
first_value = int(input())
second_value = int(input())

while first_value != second_value:
    if(first_value % 2 == 0) and (first_value/2 - second_value > 0):
        first_value = first_value/2
        print(":2")
    if (first_value/2 - second_value < 0) or (first_value % 2 != 0) or \
       (first_value - second_value == 1):
        first_value = first_value - 1
        print("-1")
