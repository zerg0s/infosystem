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

