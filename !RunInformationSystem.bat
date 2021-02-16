cd %~dp0
chcp 1251
IF EXIST "InformationSystem.jar_new.jar" (
  del /f InformationSystem.jar
  rename InformationSystem.jar_new.jar InformationSystem.jar
)

java.exe --module-path "%cd%\lib" --add-modules javafx.controls,javafx.fxml  -Dfile.encoding=Cp1251 -classpath "InformationSystem.jar;.\lib\javafx-swt.jar;.\lib\javafx.web.jar;.\lib\javafx.base.jar;.\lib\javafx.fxml.jar;.\lib\javafx.media.jar;.\lib\javafx.swing.jar;.\lib\javafx.controls.jar;.\lib\javafx.graphics.jar" informationsystem.InformationSystem