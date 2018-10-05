def check_input():
    in_data = input()
    if in_data.lstrip("-").isdigit():
        data = int(in_data)
        return data
    else:
        print("Недопустимый ввод! " + "'" + in_data +
              "'" + " не является целым числом!")
        return exit(0)


print("Решение уравнения: (ax+b)/(cx+d) = 0")
print("Введите коэффициент а:")
A = check_input()
print("Введите коэффициент b:")
B = check_input()
print("Введите коэффициент c:")
C = check_input()
print("Введите коэффициент d:")
D = check_input()
if (C == 0) and (D == 0):
    print("NO")
    exit(0)
elif (A == 0) and (B == 0):
    print('INF')
    exit(0)
elif A == 0:
    print('NO')
    exit(0)
elif C == 0:
    print(str(-B/A))
    exit(0)
elif B/A == D/C:
    print('NO')
    exit(0)
else:
    print(str(-B/A))
    exit(0)
