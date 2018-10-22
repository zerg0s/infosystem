# Author: Danilova Irina
# Task: Fragment

inputString = input("Введите строку, в которой больше двух h в тексте: ")
outputString = inputString[:inputString.find('h') + 1]
outputString += inputString[inputString.rfind('h') - 1:inputString.find('h'):-1]
outputString += inputString[inputString.rfind('h'):]

print("Получилось: ", outputString)
