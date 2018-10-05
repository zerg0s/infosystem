/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package informationsystem;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author sergeyp
 */
public class PyTaskChecker {

    private String subject;
    private String fileToManage;

    public PyTaskChecker(String subject, String fileToManage) {
        this.subject = subject;
        this.fileToManage = fileToManage;
    }

    private String selectTests(String subject) {
        //тут надо будет добавить работу с sqlite, пока просто читаем списки тестов из файла формата  "имя_задачи имя_файла_с_тестом
        String retVal = "runer_test.py";
        return retVal;
    }

    public String startPyCheck(String fileUnderCheck, String testFileName) {

        try {
            ProcessBuilder builder = new ProcessBuilder(
                    ".\\pylint\\py_task_checker.bat", fileUnderCheck, fileUnderCheck);
            builder.redirectErrorStream(true);
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
        return "";
    }

    public static void main(String Args[]) {
        PyTaskChecker pyChecker = new PyTaskChecker("Пробежка по утрам", "runner.py");

    }

}
