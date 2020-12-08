/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package taskCheckers;

import informationsystem.XmlReader;
import lintsForLangs.MyPylint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.io.File;
import java.nio.file.StandardCopyOption;

/**
 *
 * @author sergeyp
 */
public class PyTaskChecker extends TaskChecker {

    public PyTaskChecker(String subject, String fileToManage, boolean isEasyMode) {
        this.setSubject(subject);
        this.setFileToManage(fileToManage);
        workingDir = ".\\Pylint\\";
        this.isEasyMode = isEasyMode;
    }

    public PyTaskChecker(String subject) {
        this(subject, "file.py", false);
    }

    public String startPyCheck() {
        return startPyCheck(this.getSubject(), this.getFileToManage(), this.isInEasyMode());
    }


    public String startPyCheck(String subject, String fileToManage, boolean isInEasyMode) throws UnsupportedOperationException {

        StringBuilder sb = new StringBuilder();
        FileAndItsTest data = copyFileToTempFolder(fileToManage);
        data.testName = getTestName3(subject);

        if (data.testName.equals("")) {
            throw new UnsupportedOperationException("Not supported");
        }

        try {
            ProcessBuilder builder = new ProcessBuilder("python.exe",
                    "pyTestRunner.py", data.fileName, data.testName, isEasyMode ? "True" : "");
            builder.redirectErrorStream(true);
            builder.directory(new File(workingDir));
            Process p = builder.start();

            BufferedReader r = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line;
            while ((line = r.readLine()) != null) {
                sb.append(line + "\n");
            }
        } catch (IOException ex) {
            Logger.getLogger(MyPylint.class.getName()).log(Level.SEVERE, null, ex);
        }
        removeTempFiles(data);
        //Logger.getLogger(MyPylint.class.getName()).log(Level.INFO, sb.toString());
        return sb.toString();
    }

    private String getTestNameOld(String subject) {
        String testFolderName = "";
        if (subject.toLowerCase().equals("Принадлежит ли точка области?".toLowerCase())) {
            testFolderName = "isPointInArea";
        }
        if (subject.toLowerCase().equals("Принадлежит ли точка квадрату?".toLowerCase())) {
            testFolderName = "isPointInSquare";
        }
        if (subject.toLowerCase().equals("Разворот последовательности".toLowerCase())) {
            testFolderName = "reverseInput";
        }
        if (subject.toLowerCase().equals("Алгоритм Евклида".toLowerCase())) {
            testFolderName = "gcdEvklid";
        }
        if (subject.toLowerCase().equals("Сложение без сложения".toLowerCase())) {
            testFolderName = "sumNoAdd";
        }
        if (subject.toLowerCase().equals("Обращение фрагмента".toLowerCase())) {
            testFolderName = "fragmentReverse";
        }
        if (subject.toLowerCase().equals("Сумма десятичных цифр".toLowerCase())) {
            testFolderName = "sumOfDecNumbers";
        }
        if (subject.toLowerCase().equals("Расписание звонков".toLowerCase())) {
            testFolderName = "alarmsTimeTable";
        }
        if (subject.toLowerCase().equals("Парты".toLowerCase())) {
            testFolderName = "buyingNewDesks";
        }
        if (subject.toLowerCase().equals("Коньки".toLowerCase())) {
            testFolderName = "puttingOnSkates";
        }
        return testFolderName;
    }

    public String getTestName2(String subject) {
        String testFolderName = "";
        XmlReader reader = new XmlReader(".\\pylint\\TestsInfo.xml");
        testFolderName = reader.getTestFolderBySubject(subject);
        return testFolderName;
    }
}
