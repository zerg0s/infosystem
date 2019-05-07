# checks functional style


def funcCheck(line):
    stack = []
    flagIsFirstOpenBrace = True
    retValue = True

    for ch in line:
        if ch != "(" and ch != ")":
            continue
        if ch == "(":
            if flagIsFirstOpenBrace:
                stack.append("(")
                flagIsFirstOpenBrace = False
            elif len(stack):
                stack.append("(")
            else:
                retValue = False
                break
        elif ch == ")":
            stack.pop(-1)
    return retValue


def noIfCheck(file):
    pass


def noRecursionCheck(file):
    pass


if __name__ == "__main__":
    test = "\n\n\na\n(a(\n\ta)a)aa"
    print(funcCheck(test))
