# Мария Евсеева
# Ход короля

startСellX = int(input("Введите номер первой ячейки по вертикали: "))
startСellY = int(input("Введите номер первой ячейки по горизонтали: "))

endСellX = int(input("Введите номер второй ячейки по вертикали: "))
endСellY = int(input("Введите номер второй ячейки по горизонтали: "))

if (abs(endСellX - startСellX) <= 1) and (abs(endСellY - startСellY) <= 1):
    print("YES")
else:
    print("NO")