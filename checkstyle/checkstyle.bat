@echo off
cd %~dp0
cd ..
set JAVA_FILE=%1%
java -jar checkstyle\checkstyle-8.41-all.jar -c checkstyle\sun_checks.xml %JAVA_FILE% 1> %JAVA_FILE%_errorReport.txt 2>&1
rem java -jar checkstyle-8.8-all.jar -c /sun_checks.xml %JAVA_FILE%
