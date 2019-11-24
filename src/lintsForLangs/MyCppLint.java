/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lintsForLangs;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.logging.Level;
import java.util.logging.Logger;
/**
 *
 * @author user
 */
public class MyCppLint {
    public MyCppLint() {
    }

    public void startCpplint(String attachmentName) {
        try {
            ProcessBuilder builder = new ProcessBuilder(
                    ".\\cpplint\\cpplint.bat" , attachmentName);
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
            Logger.getLogger(MyCppLint.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
