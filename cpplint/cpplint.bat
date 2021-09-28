cd %~dp0
cd ..
python .\cpplint\cpplint.py %1% >_errorReport.txt
