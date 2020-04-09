package data;

import org.jetbrains.annotations.NotNull;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

public class FileOperator {
    private String outputFile = "контрольная_работа_2.txt";

    public FileOperator(String outputFile) {
        this.outputFile = outputFile;
    }

    public void saveDataToFile(@NotNull HashMap<String, ArrayList<String>> issuesOfTheStudent) {
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile));

            for (String key : issuesOfTheStudent.keySet()) {
                ArrayList<String> stIssues = issuesOfTheStudent.get(key);
                writer.write(key + "(Total " + stIssues.size()+"): \n");
                for (String issue : stIssues) {
                    writer.write("\t" + issue + "\n");
                }
            }
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void setOutputFile(String outputFile) {
        this.outputFile = outputFile;
    }

    public String getOutputFile() {
        return outputFile;
    }
}
