# код проверяльщика задач, версия 2019.25

import os
import subprocess
import sys

from shutil import copy2
from pep9 import funcCheck
from localization import Locale


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


def processAndTrimAnswer(answer):
    return answer.strip().replace(" \n", "\n")


def checkConfigurationAndRestrictions(testConfiguration):
    if "functional" in testConfiguration:
        sourceFileWithoutHeader = ""
        for line in open(fileToCheck, "r", encoding="utf-8").readlines():
            if line.strip().startswith("#"): continue
            sourceFileWithoutHeader += line + "\n"
        if not funcCheck(sourceFileWithoutHeader):
            print(f"{Locale.NotInFunctional}\n{Locale.Failed}")
            exit()

    if "deny" in testConfiguration:
        denyValues = list(map(lambda x: x.strip(), str(testConfiguration["deny"]).split(',')))
        sourceCode = open(fileToCheck, "r", encoding="utf-8").readlines()
        cleanSourceCode = map(lambda line:
                              line[:len(line) + 1 + line.find("#")], sourceCode)
        for value in denyValues:
            if value in cleanSourceCode:
                print(f"{Locale.HaveRestricted}\n{Locale.Failed}")
                exit()

    if "must" in testConfiguration:
        mustValues = set(map(lambda x: x.strip(), str(testConfiguration["must"]).split(',')))
        foundValues = set()
        sourceCode = open(fileToCheck, "r", encoding="utf-8").readlines()
        cleanSourceCode = map(lambda line:
                              line[:len(line) + 1 + line.find("#")], sourceCode)
        for value in mustValues:
            if value in cleanSourceCode:
                foundValues.add(value)
        if len(foundValues) != len(mustValues):
            print(Locale.DoesntHaveMandatory)
            print(Locale.Failed)
            exit()


################
# Manual Config Section

easyMode = True  # в этом режиме показываются входные данные для упавших тестов.
debugMode = False  # ONLY for local test
maxExecutionTimeDelay = 1  # max timeout for a task
################

if __name__ == "__main__":
    fileToCheck = "my.py"
    dirToCheck = "regLastWord"
    # dirToCheck = "regFindReplaceRepeated"
    retArray = list()

    extraDataForEasyMode = ""

    if len(sys.argv) > 2 or debugMode == 1:
        if not debugMode:
            fileToCheck = sys.argv[1]
            dirToCheck = sys.argv[2]
        dirWithTests = ".\\tests\\" + dirToCheck + "\\"
        testConfiguration = readConfing(dirWithTests + "config.conf")

        # для функционального программирования еще ограничение: одна инструкция языка.
        checkConfigurationAndRestrictions(testConfiguration)

        for file in sorted(filter(lambda x: x.endswith(".t"), os.listdir(dirWithTests)), key=lambda x: int(x[4:-2])):
            # для всех файлов .t с входными данными
            if os.path.isfile(dirWithTests + file) and file.endswith(".t"):
                # tmp = "<" + myDir + file
                # os.system("python -u " + fileToCheck + " " + tmp + " >output")
                copy2(dirWithTests + file, "input.txt")
                proc = subprocess.Popen(["python", "-u", fileToCheck],
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
                    retArray.append(Locale.Timeout)
                    break
                finally:
                    if "input" in testConfiguration and os.path.exists(str(testConfiguration["input"])):
                        os.remove(str(testConfiguration["input"]))

                # надо проверить .a файлы с ответом
                correctAnswer = readAnswerFile(dirWithTests + file[:file.rfind(".")] + ".a")
                # вдруг будут тесты с 2 правильными ответами
                # correctAnswer2 = readAnswerFile(myDir + file[:file.rfind(".")] + ".a1")

                # функция проверки правильного ответа - пока единственный обязательный параметр конфига
                funcToCheckAnswer = testConfiguration.get("func", None)
                if funcToCheckAnswer is None: break

                # кодировочный костыль, иногда приходит в кодировке анси
                try:
                    userAnswer = open("output", "r", encoding="utf-8").read().replace("\r\n", "\n")
                except UnicodeDecodeError:
                    userAnswer = open("output", "r", encoding="cp1251").read().replace("\r\n", "\n")

                if not checkCrashExists(userAnswer):
                    userAnswer = processAndTrimAnswer(userAnswer)
                    correctAnswer = processAndTrimAnswer(correctAnswer)
                    # tricky check for random tasks - if answer could be divided into 23
                    isAnswerCorrect = False
                    if "answer_code" in testConfiguration:
                        if testConfiguration["answer_code"] == "mod23":
                            isAnswerCorrect = (int(userAnswer) % 23 == 0)
                    else:
                        isAnswerCorrect = funcToCheckAnswer(correctAnswer, userAnswer)
                    retArray.append(isAnswerCorrect)

                    if not isAnswerCorrect:
                        extraDataForEasyMode = open(dirWithTests + file, encoding="utf-8").read()
                        # print(correctAnswer)
                        if debugMode:
                            print(userAnswer)
                        if "ContinueIfTestFailed" not in testConfiguration:  # для толстых программ
                            break  # программа пользователя выдала неверный результат, дальше не надо.
                else:
                    retArray.append(userAnswer)
                    break  # программа пользователя упала, дальше не надо.
    if len(retArray) == 0:
        print(Locale.GeneralError)
    else:
        print(*list(
            map(lambda x: ["test" + str(x[0]),
                           Locale.Passed if str(x[1]) is "True" else Locale.Failed if not x[1] else x[1]],
                enumerate(retArray, 1))), sep="\n")
    # print(retArrray)
    if len(set(retArray)) == 1 and str(retArray[0]) == "True":
        print(Locale.Passed)
    else:
        if easyMode and extraDataForEasyMode:
            print(Locale.EasyModeHelp % extraDataForEasyMode)
        print(Locale.Failed)
