def sum(a, b):
    if b != 0:
        return sum (a+1, b-1)

    else:
        return a

a = int(input())
b = int(input())

if a < 0 or b < 0:
        print("Вы ввели отрицательное/отрицательные числа, попробуйте снова.")
else:
        print("a + b =", sum(a, b))