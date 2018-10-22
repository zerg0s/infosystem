# Мальцев Алексей
# Контрольная работа 20.10.18
# Обращение фрагмента

stroka1 = input()
First = int(stroka1.find("h"))
End = int(stroka1.rfind("h"))
Middle = stroka1[End - 1:First:-1]
print(stroka1[0:First + 1] + Middle + stroka1[End:])
