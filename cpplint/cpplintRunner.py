import sys
import os
from shutil import copyfile
import subprocess

i = 0
# print ("\n".join(sys.path))
while not os.path.isfile(os.path.dirname(sys.path[i]) + r"\python.exe"):
    # print("--- " + os.path.dirname(sys.path[i]) + r"\python.exe")
    i = i + 1
scriptsFolder = os.path.dirname(sys.path[i]) + r"\Scripts"
print(scriptsFolder)
if not os.path.isfile(scriptsFolder + r"\cpplint.exe"):
    copyfile("cpplint.exe", scriptsFolder + r"\cpplint.exe")

if (len(sys.argv) > 1):
    # stream = os.popen(scriptsFolder + r"\cpplint.exe " + sys.argv[1])  # + " >" + sys.argv[1] + "_errorReport.txt")
    proc = subprocess.Popen(scriptsFolder + r"\cpplint.exe " + sys.argv[1], stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    str1 = proc.stdout.read().decode('utf8').replace("\r\n","\n")
    # print (str1)
    with open(sys.argv[1] + "_errorReport.txt", "w+", encoding="utf-8") as outFile:
        outFile.write(str1)
