@echo off
cd %~dp0
cd ..
python ".\pylint\pyTestRunner.py" %1% %2%
