import sys
import subprocess
import os
from shutil import copy2


# read the correct answer for test## from .a file
def readAnswerFile(pathToFile):
    if os.path.isfile(pathToFile):
        retVal = open(pathToFile, "r", encoding="utf-8").read()
    else:
        retVal = ""
    return retVal


def readConfing(pathTocfg):
    dictOfConfigs = dict()
    if os.path.isfile(pathTocfg):
        fileContent = open(pathTocfg, "r", encoding="utf-8").read()
        keypairs = fileContent.split("\t")
        dictOfConfigs = {k: v for k, v in map(lambda x: x.split("="), keypairs)}
    # В словарь записан полный конфиг. В поле func функция проверки
    if "func" in dictOfConfigs:
        if dictOfConfigs["func"] == "contains":
            dictOfConfigs["func"] = lambda x, y: x.lower() in y.lower()
        else:
            dictOfConfigs["func"] = lambda x, y: (x.strip() == y.strip())
    return dictOfConfigs


def checkCrashExists(userAnswer):
    return "traceback (most recent call last):" in userAnswer.lower()


################
# Manual Config Section

easyMode = True  # в этом режиме показываются входные данные для упавших тестов.
debug = 0  # ONLY for local test
maxExecutionTimeDelay = 1  # max timeout for a task

################

if __name__ == "__main__":

    fileToCheck = "file.py"
    dirToCheck = "countSort"
    retArrray = list()
    extraDataForEasyMode = ""

    if len(sys.argv) > 2 or debug == 1:
        if not debug:
            fileToCheck = sys.argv[1]
            dirToCheck = sys.argv[2]
        myDir = ".\\tests\\" + dirToCheck + "\\"
        for file in os.listdir(myDir):

            # для всех файлов .t с входными данными
            if os.path.isfile(myDir + file) and file.endswith(".t"):

                testConfiguration = readConfing(myDir + "config.conf")

                proc = subprocess.Popen(["python", "-u", fileToCheck],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT,
                                        stdin=subprocess.PIPE,
                                        )
                # вычитываем исходный .t файл и помещаем всё содержимое во входящий поток к тестируемой программе
                if "input" in testConfiguration:
                    copy2(myDir + file, str(testConfiguration["input"]))
                    inputDataForUsersProgram = open(str(testConfiguration["input"]), "rb").read()
                else:
                    inputDataForUsersProgram = open(myDir + file, "rb").read()
                    proc.stdin.write(inputDataForUsersProgram)

                # ждем отклика в течение таймаута, в outs - результат работы программы
                try:
                    outs, errs = proc.communicate(timeout=maxExecutionTimeDelay)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    outs, errs = proc.communicate()
                    retArrray.append("Timeout")
                    break
                finally:
                    if "input" in testConfiguration and os.path.exists(str(testConfiguration["input"])):
                        os.remove(str(testConfiguration["input"]))

                # надо проверить .a файлы с ответом
                correctAnswer = readAnswerFile(myDir + file[:file.rfind(".")] + ".a")
                # функция проверки правильного ответа - единственный обязательный параметр конфига
                funcToCheckAnswer = testConfiguration["func"]

                userAnswer = outs.decode(sys.stdout.encoding).replace("\r\n", "\n")
                # print(userAnswer)
                if not checkCrashExists(userAnswer):
                    isAnswerCorrect = funcToCheckAnswer(correctAnswer, userAnswer)
                    retArrray.append(isAnswerCorrect)
                    if not isAnswerCorrect:
                        extraDataForEasyMode = inputDataForUsersProgram
                        break  # программа пользователя выдала неверный результат, дальше не надо.
                else:
                    retArrray.append(userAnswer)
                    break  # программа пользователя упала, дальше не надо.
    if len(retArrray) == 0:
        print("Tests not found or something else happened plz debug")
    else:
        print(*list(
            map(lambda x: ["test" + str(x[0]), "Passed" if str(x[1]) is "True" else "Failed" if not x[1] else x[1]],
                enumerate(retArrray, 1))), sep="\n")
    # print(retArrray)
    if len(set(retArrray)) == 1 and str(retArrray[0]) == "True":
        print("passed")
    else:
        if easyMode and extraDataForEasyMode:
            print("Wrong answer was received for input:\n%s" % extraDataForEasyMode.decode('utf-8'))
        print("failed")
