@echo off
cd %~dp0
cd ..
SET par1="%1% "
SET par2=%~dp0config.file
SET cfgPlint=%par1%%par2% 
python ".\pylint\pylintRunner.py" %cfgPlint%
