import re


def check(inputStr):
    stack = []
    lst = re.sub(r"[\w|\s|\[|\]]*", ' ', inputStr.strip()).split()
    for i in lst:
        if i in ('(', '{'):
            stack.append(i)
        else:
            if stack:
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return 1
            else:
                if i == "}" and stack[:-1] == "{" or i == ")" and stack[:-1] == "(":
                    stack.remove(stack[:-1])
                if not stack:
                    return 1
    return 0 if not stack else 1


str1 = input()
print(check(str1))
