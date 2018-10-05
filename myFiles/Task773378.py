start = []
end = []
length = []
i = 0
while i < 3:
    start.append(int(input("Введите начало спички: ")))
    end.append(int(input("Введите конец спички: ")))
    length.append(end[i] - start[i])
    i += 1
if end[0] >= start[1] and end[1] >= start[2]:
    print(0)
else:
    if (start[2] - end[1]) <= length[0]:
        print(1)
    else:
        if start[1] - end [0] <= length[2]:
            print(3)
        else:
            print(1)

