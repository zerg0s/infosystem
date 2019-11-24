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
import java.util.HashMap;

/**
 *
 * @author sergeyp
 */
public class PyTaskChecker {

    private String subject;
    private String fileToManage;
    private static HashMap<String, String> knownTests;

    static {
        fillData();
    }

    private void removeTempFiles(FileAndItsTest data) {
        try {
            Files.delete(new File(".\\Pylint\\" + data.fileName).toPath());
            //Files.delete(new File(".\\Pylint\\" + data.fileTestName).toPath());
        } catch (IOException ex) {
            Logger.getLogger(PyTaskChecker.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    private class FileAndItsTest {

        public String fileName = "file.py";
        public String testName = "test";
    }

    public PyTaskChecker(String subject, String fileToManage) {
        this.subject = subject;
        this.fileToManage = fileToManage;
    }

    public PyTaskChecker(String subject) {
        this(subject, "file.py");
    }

    public String startPyCheck() {
        return startPyCheck(this.subject, this.fileToManage);
    }

    public String getNameForKnownTest(String subject) {
        return getTestName3(subject);
    }

    public String startPyCheck(String subject, String fileToManage) throws UnsupportedOperationException {

        StringBuilder sb = new StringBuilder();
        FileAndItsTest data = copyFileToTempFolder(fileToManage);
        data.testName = getTestName3(subject);

        if (data.testName.equals("")) {
            throw new UnsupportedOperationException("Not supported");
        }

        try {
            ProcessBuilder builder = new ProcessBuilder("python.exe",
                    "pyTestRunner.py", data.fileName, data.testName);
            builder.redirectErrorStream(true);
            builder.directory(new File(".\\pylint"));
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

    //Все ужасно, метод писать некогда :(
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

    public String getTestName3(String subjectFromIssue) {
        String testFolderName;
        testFolderName = knownTests.getOrDefault(subjectFromIssue, "");
        //еще одна попытка найти по неполному совпадению
        if (testFolderName.equals("")){
            for(String test : knownTests.keySet()){
                if (subjectFromIssue.toLowerCase().contains(test.toLowerCase()))
                {
                    testFolderName = knownTests.getOrDefault(test, "");
                }
            }
        }
        return testFolderName;
    }

    private static void fillData() {
        XmlReader reader = new XmlReader(".\\pylint\\TestsInfo.xml");
        knownTests = reader.getAlltests();
    }

    private FileAndItsTest copyFileToTempFolder(String fileToManage) {
        FileAndItsTest retVal = new FileAndItsTest();
        try {
            Files.copy(new File(fileToManage).toPath(), new File(".\\Pylint\\" + retVal.fileName).toPath(), StandardCopyOption.REPLACE_EXISTING);
            //Files.copy(new File(".\\Pylint\\tests\\" + testFileName).toPath(), new File(".\\Pylint\\" + retVal.fileTestName).toPath(), StandardCopyOption.REPLACE_EXISTING);
        } catch (IOException ex) {
            Logger.getLogger(PyTaskChecker.class.getName()).log(Level.SEVERE, null, ex);
        }
        return retVal;
    }

}
