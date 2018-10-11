/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package informationsystem;

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
public class PyTaskChecker {

    private String subject;
    private String fileToManage;

    private void removeTempFiles(FileAndItsTest data) {
        try {
            Files.delete(new File(".\\Pylint\\" + data.fileName).toPath());
            Files.delete(new File(".\\Pylint\\" + data.fileTestName).toPath());
        } catch (IOException ex) {
            Logger.getLogger(PyTaskChecker.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    private class FileAndItsTest {

        public String fileName = "file.py";
        public String fileTestName = "test_file.py";
    }

    public PyTaskChecker(String subject, String fileToManage) {
        this.subject = subject;
        this.fileToManage = fileToManage;
    }

    public String startPyCheck() {
        return startPyCheck(this.subject, this.fileToManage);
    }

    public String startPyCheck(String subject, String fileToManage) {

        String testFileName = getTestName(subject);
        FileAndItsTest data = copyTestAndFileToTempFolder(fileToManage, testFileName);
        try {
            ProcessBuilder builder = new ProcessBuilder("python.exe",
                    "pyTestRunner.py", data.fileName, data.fileTestName);
            builder.redirectErrorStream(true);
            builder.directory(new File(".\\pylint"));
            Process p = builder.start();
            BufferedReader r = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line;
            while (true) {
                line = r.readLine();
                if (line == null) {
                    break;
                }
                System.out.println(line);

            }
        } catch (IOException ex) {
            Logger.getLogger(MyPylint.class.getName()).log(Level.SEVERE, null, ex);
        }
        //removeTempFiles(data);
        return "";
    }
    //Все ужасно, метод писать некогда :(

    private String getTestName(String subject) {
        return "test_pointInArea.py";
    }

    public static void main(String[] args) {

    }

    private FileAndItsTest copyTestAndFileToTempFolder(String fileToManage, String testFileName) {
        FileAndItsTest retVal = new FileAndItsTest();
        try {
            Files.copy(new File(".\\myFiles\\" + fileToManage).toPath(), new File(".\\Pylint\\" + retVal.fileName).toPath(), StandardCopyOption.REPLACE_EXISTING);
            Files.copy(new File(".\\Pylint\\tests\\" + testFileName).toPath(), new File(".\\Pylint\\" + retVal.fileTestName).toPath(), StandardCopyOption.REPLACE_EXISTING);
        } catch (IOException ex) {
            Logger.getLogger(PyTaskChecker.class.getName()).log(Level.SEVERE, null, ex);
        }
        return retVal;
    }

}
