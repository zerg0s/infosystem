# код проверяльщика задач, версия 2021.27

import os
import subprocess
import sys

from shutil import copy2
from typing import List

from pep9 import funcCheck
from localization import Locale
from testReport import TestReport


# read the correct answer for test## from .a file
def readAnswerFile(pathToFile):
    if os.path.isfile(pathToFile):
        return open(pathToFile, "r", encoding="utf-8").read()


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
    else:
        dictOfConfigs["func"] = lambda x, y: x.lower() in y.lower()        
    
    return dictOfConfigs


def checkCrashExists(userAnswer):
    return "traceback (most recent call last):" in userAnswer.lower()


def processAndTrimAnswer(answer):
    return answer.strip().replace(" \n", "\n") if answer else None


def cleanMainFromFileToCheck():
    isMainFound = False
    sourceFileWithoutMain = ""
    for line in open(fileToCheck, "r", encoding="utf-8").readlines():
        if line.strip().startswith("if __name__"):
            isMainFound = True
            break
        sourceFileWithoutMain += line
    if isMainFound:
        text_file = open(fileToCheck, "w+", encoding="utf-8")
        text_file.write(sourceFileWithoutMain)
        text_file.close()


def addExecStdIntoTheEndOfFile():
    text_file = open(fileToCheck, "a+", encoding="utf-8")
    text_file.write("\n\nfrom sys import stdin\n\nif __name__ == \"__main__\": exec(stdin.read())")
    text_file.close()


def prettyPrintRetArray(retArray: List[TestReport]):
    i = 0
    for reportLine in retArray:
        if reportLine[0] == TestReport.TEST:
            print(f"test{i + 1} - ", end="")
            if str(reportLine[1]) == "True":
                print(Locale.Passed)
            else:
                print(Locale.Failed)
            i += 1
        else:
            print(reportLine[1])


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


def getCorrectAnswers(dirWithTests, fileWithTests):
    correctAnswers = list()
    # как минимум 1 правильный ответ должен быть, иначе считаем любой ответ правильным
    readAnswer = readAnswerFile(dirWithTests + fileWithTests[:fileWithTests.rfind(".")] + ".a")
    if readAnswer is None:
        readAnswer = ' '
    correctAnswers.append(readAnswer)

    # вдруг будут тесты с более чем 1 правильными ответами
    i = 1
    otherAnswerExists = os.path.isfile(dirWithTests + fileWithTests[:fileWithTests.rfind(".")] + ".a" + str(i))

    while otherAnswerExists:
        correctAnswer2 = readAnswerFile(dirWithTests + fileWithTests[:fileWithTests.rfind(".")] + ".a" + str(i))
        if correctAnswer2 is None:
            break
        correctAnswers.append(correctAnswer2)
        i += 1
    return correctAnswers


################
# Manual Config Section

easyMode = False  # в этом режиме показываются входные данные для упавших тестов.
maxExecutionTimeDelay = 2  # max timeout for a task
################

if __name__ == "__main__":
    fileToCheck = "myFile.py"
    dirToCheck = "reverseInput"
    # dirToCheck = "regFindReplaceRepeated"
    retArray = list()

    extraDataForEasyMode = ""

    if len(sys.argv) > 2:
        fileToCheck = sys.argv[1]
        dirToCheck = sys.argv[2]
        if len(sys.argv) > 3:
            easyMode = True if sys.argv[3] else easyMode

    dirWithTests = ".\\tests\\" + dirToCheck + "\\"
    testConfiguration = readConfing(dirWithTests + "config.conf")

    # для функционального программирования еще ограничение: одна инструкция языка.
    checkConfigurationAndRestrictions(testConfiguration)

    # для всех файлов .t с входными данными
    testFiles = sorted(filter(lambda x: x.endswith(".t"), os.listdir(dirWithTests)), key=lambda x: int(x[4:-2]))

    for file in testFiles:
        if os.path.isfile(dirWithTests + file) and file.endswith(".t"):
            needToCompileTestData = testConfiguration.get("needToCompileTestData", None)
            inputDataFile = testConfiguration.get("input", "input.txt")

            copy2(dirWithTests + file, inputDataFile)
            if needToCompileTestData:
                cleanMainFromFileToCheck()
                addExecStdIntoTheEndOfFile()

            proc = subprocess.Popen(["python", "-u", fileToCheck],
                                    stdout=open("output", "w+", encoding="utf-8"),
                                    stderr=subprocess.STDOUT,
                                    stdin=open(inputDataFile, encoding="utf-8"),
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
                retArray.append(TestReport(TestReport.OTHER, Locale.Timeout))
                break
            finally:
                if "input" in testConfiguration and os.path.exists(str(testConfiguration["input"])):
                    os.remove(str(testConfiguration["input"]))

            # надо проверить .a файлы с ответами
            correctAnswers = getCorrectAnswers(dirWithTests, file)

            # функция проверки правильного ответа - пока единственный обязательный параметр конфига
            funcToCheckAnswer = testConfiguration.get("func", None)
            if funcToCheckAnswer is None:
                break

            # кодировочный костыль, иногда приходит в кодировке анси
            try:
                userAnswer = open("output", "r", encoding="utf-8").read().replace("\r\n", "\n")
            except UnicodeDecodeError:
                userAnswer = open("output", "r", encoding="cp1251").read().replace("\r\n", "\n")

            if checkCrashExists(userAnswer):
                extraDataForEasyMode = open(dirWithTests + file, encoding="utf-8").read()
                if easyMode and extraDataForEasyMode:
                    retArray.append(TestReport(TestReport.OTHER, Locale.EasyModeHelp % extraDataForEasyMode))

                retArray.append(TestReport(TestReport.OTHER, Locale.CrashFound))
                retArray.append(TestReport(TestReport.OTHER, userAnswer))
                break  # программа пользователя упала, дальше не надо.

            userAnswer = processAndTrimAnswer(userAnswer)
            correctAnswers = list(map(processAndTrimAnswer, correctAnswers))

            # Костыль для случаев, когда любой ответ - не падение верный
            if len(correctAnswers) > 0 and \
                    (correctAnswers[0] is None or
                     correctAnswers[0].strip() == ""):
                retArray.append(TestReport(TestReport.TEST, "True"))
                continue

            # tricky check for random tasks - if answer could be divided into 23
            isAnswerCorrect = False
            if "answer_code" in testConfiguration:
                if testConfiguration["answer_code"] == "mod23":
                    isAnswerCorrect = (int(userAnswer) % 23 == 0)
            elif userAnswer is not None and correctAnswers[0] is not None:
                for aCorrectAnswer in correctAnswers:
                    isAnswerCorrect |= funcToCheckAnswer(aCorrectAnswer, userAnswer)

            retArray.append(TestReport(TestReport.TEST, isAnswerCorrect))

            if not isAnswerCorrect:
                extraDataForEasyMode = open(dirWithTests + file, encoding="utf-8").read()
                if easyMode:
                    retArray.append(TestReport(TestReport.OTHER, Locale.ReceivedAnswer))
                    retArray.append(TestReport(TestReport.OTHER, userAnswer))
                    retArray.append(TestReport(TestReport.OTHER, Locale.EasyModeHelp % extraDataForEasyMode))
                if "ContinueIfTestFailed" not in testConfiguration:  # для толстых программ
                    break  # программа пользователя выдала неверный результат, дальше не надо.

    if len(retArray) == 0:
        print(Locale.GeneralError)
    else:
        prettyPrintRetArray(retArray)

    # костыль для Java-стороны Locale.Passed в последней строке вывода значит, что задача принята.
    if retArray and all(map(lambda x: str(x[1]) == "True", retArray)):
        print(Locale.Passed)
    else:
        print(Locale.Total, Locale.Failed, sep="\n")
