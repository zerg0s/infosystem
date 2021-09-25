'''Определите, можно ли вычеркнуть из данного массива одно число так, чтобы оставшиеся числа оказались упорядоченными по возрастанию.
+Пример1:+
Ввод:
1 2 5 3 4
Вывод:
Yes

+Пример2:+
Ввод:
1 2 3 4
Вывод:
Yes  (Вычеркиваем любой элемент и массив остается упорядоченным)

+Пример3:+
Ввод:
4 3 2 1
Вывод:
No
'''

def checkSorted(list1):
    i = 1
    if len(list1) <= 1:
        return True

    prev = list1[0]
    while i < len(list1):
        if list1[i] >= prev:
            prev = list1[i]
            i += 1
        else:
            return False

    return True


def checkAlmostSorted(list1):
    if len(list1) <= 1:
        return True

    i = 0
    while i < len(list1) - 1:
        if checkSorted(list1[0:i] + list1[i + 1:]):
            return True
        else:
            i += 1
    return False

