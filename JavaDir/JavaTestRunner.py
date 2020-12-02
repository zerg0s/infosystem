#код проверяльщика задач, версия 2019.23

import os
import subprocess
import sys

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
    return "exception" in userAnswer.lower()


def processAndTrimAnswer(answer):
    return answer.strip().replace(" \n", "\n")


################
# Manual Config Section

easyMode = True  # в этом режиме показываются входные данные для упавших тестов.
debug = 0  # ONLY for local test
maxExecutionTimeDelay = 1  # max timeout for a task

################


if __name__ == "__main__":

    fileToCheck = "Main.class"

    dirToCheck = "reverseInput"
    # dirToCheck = "regFindRepeated"
    # dirToCheck = "regLastWord"
    # dirToCheck = "regDomains"
    # dirToCheck = "regPhoneNumbers"
    # dirToCheck = "regFindReplaceRepeated"
    retArrray = list()

    extraDataForEasyMode = ""

    if len(sys.argv) > 2 or debug == 1:
        if not debug:
            fileToCheck = sys.argv[1]
            dirToCheck = sys.argv[2]
        dirWithTests = ".\\tests\\" + dirToCheck + "\\"
        if not os.path.exists(dirWithTests):
            dirWithTests = "..\\pylint\\tests\\" + dirToCheck + "\\"
        testConfiguration = readConfing(dirWithTests + "config.conf")
        # print(os.path.abspath(dirWithTests))
        for file in filter(lambda x: x.endswith(".t"), os.listdir(dirWithTests)):
            # для всех файлов .t с входными данными
            if os.path.isfile(dirWithTests + file) and file.endswith(".t"):

                # tmp = "<" + myDir + file
                # os.system("python -u " + fileToCheck + " " + tmp + " >output")
                copy2(dirWithTests + file, "input.txt")
                proc = subprocess.Popen(["java", fileToCheck.replace(".class", "")],
                                        stdout=open("output", "w+", encoding="utf-8"),
                                        stderr=subprocess.STDOUT,
                                        stdin=open(dirWithTests + file, encoding="utf-8"),
                                        )
                # вычитываем исходный .t файл и помещаем всё содержимое во входящий поток к тестируемой программе
                # if "input" in testConfiguration:
                #     copy2(myDir + file, str(testConfiguration["input"]))
                #     inputDataForUsersProgram = open(str(testConfiguration["input"]), "rb").read()
                # else:
                #     inputDataForUsersProgram = open(myDir + file, "rb").read()
                #     proc.stdin.write(inputDataForUsersProgram)

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
                correctAnswer = readAnswerFile(dirWithTests + file[:file.rfind(".")] + ".a")
                # вдруг будут тесты с 2 правильными ответами
                # correctAnswer2 = readAnswerFile(myDir + file[:file.rfind(".")] + ".a1")
                # функция проверки правильного ответа - пока единственный обязательный параметр конфига
                funcToCheckAnswer = testConfiguration.setdefault("func", lambda x, y: x.lower() in y.lower());

                # кодировочный костыль, иногда приходит в кодировке анси
                try:
                    userAnswer = open("output", "r", encoding="utf-8").read().replace("\r\n", "\n")
                except UnicodeDecodeError:
                    userAnswer = open("output", "r", encoding="cp1251").read().replace("\r\n", "\n")

                if not checkCrashExists(userAnswer):

                    userAnswer = processAndTrimAnswer(userAnswer)
                    correctAnswer = processAndTrimAnswer(correctAnswer)
                    #tricky check for random tasks - if answer could be divided into 23
                    if "answer_code" in testConfiguration:
                        if testConfiguration["answer_code"] == "mod23":
                            isAnswerCorrect = (int(userAnswer) % 23 == 0)
                    else:
                        isAnswerCorrect = funcToCheckAnswer(correctAnswer, userAnswer)
                    retArrray.append(isAnswerCorrect)

                    if not isAnswerCorrect:
                        extraDataForEasyMode = open(dirWithTests + file, encoding="utf-8").read()
                        # print(correctAnswer)
                        if debug:
                            print(userAnswer)
                        if "ContinueIfTestFailed" not in testConfiguration: # для толстых программ
                            break  # программа пользователя выдала неверный результат, дальше не надо.
                else:
                    retArrray.append(userAnswer)
                    break  # программа пользователя упала, дальше не надо.
    if len(retArrray) == 0:
        print("Tests not found or something else happened plz debug")
    else:
        print(*list(
            map(lambda x: ["test" + str(x[0]), "Passed" if str(x[1]) == "True" else "Failed" if not x[1] else x[1]],
                enumerate(retArrray, 1))), sep="\n")
    # print(retArrray)
    if len(set(retArrray)) == 1 and str(retArrray[0]) == "True":
        print("passed")
    else:
        if easyMode and extraDataForEasyMode:
            print("Wrong answer was received for input:\n%s" % extraDataForEasyMode)
        print("failed")
