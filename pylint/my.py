# В некоторых системах текст, обрамленный в "*", должен отображаться полужирным.
# Требуется функция, которая для входной строки заменить её участки, обрамленные в "*" на их html-предстваление.
# Например,
# This is important! -> This is <b>important</b>
import re


def find(string):
    pattern = re.compile(r'\*((?!\\\*)|.*)?\*')
    return re.sub(pattern, r'<b>\1</b>', string).replace(r"\*", "*")


print(find(input()))
