package textUtils;

import data.ConfiguredTask;
import data.LintReportMode;
import org.apache.commons.codec.Charsets;
import redmineManagement.ConnectionWithRedmine;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.regex.Pattern;

public class TextUtils {
    /**
     *     * @param reportLines
     * @return
     */
    public static String getPrettyErrorsJava(String[] reportLines) {
        int i = 0;
        String result = "";
        while (i < reportLines.length - 2) {
            i++;
            result += reportLines[i].replaceAll("^\\[ERROR\\](.*)(\\.java:)(.*)$",
                    "[ERROR]Line $3") + "\n";
        }
        return result;
    }

    /**
     *     * @param reportLines
     * @return
     */
    public static String getPrettyErrorsPython(String[] reportLines) {
        int i = 0;
        String result = "";
        while (i < reportLines.length - 2) {
            i++;
            result += reportLines[i].replaceAll("^(.*)(\\.py:)(.*)$",
                    "[ERROR]Line $3") + "\n";
        }
        return result;
    }

    public static String generateErrorMsg(ConfiguredTask task, String lastLineInReport) {
        String msg = "\n PEP8 mismatch found. Some corrections are required!";
        String error = "";
        if (task.getLintReportMode().getModeNumber() != LintReportMode.NIGHTMARE_MODE)
            error = lastLineInReport + msg;
        else {
            error = msg;
        }
        return error;
    }

    public static String[] readReportFile(String fileDir) {
        List<String> lines = new ArrayList<>();
        try {
            lines = Files.readAllLines(Paths.get(fileDir), Charsets.UTF_8);
        } catch (IOException ex) {
            logger.log(Level.SEVERE, ex.toString());
        }

        if (lines.isEmpty()) {
            try {
                lines = Files.readAllLines(Paths.get(fileDir), Charset.forName("windows-1251"));
            } catch (IOException ex) {
                logger.log(Level.SEVERE, ex.toString());
            }
        }

        String result = "";
        int i = lines.size() - 1;
        while (lines.size() > 0) {
            result = lines.get(i);
            lines.remove(i);
            if (!result.isBlank()) {
                break;
            }
            i--;
        }
        if (result.indexOf('(') != -1) {
            result = result.substring(0, result.indexOf('('));
        }
        lines.add(result);
        return lines.toArray(new String[0]);
    }

    public static Integer javaErrorAmountDetectionInFile(String string) {
        if (!string.toLowerCase().contains("audit done.")) {
            ArrayList<String> words = new ArrayList<>();
            if (!string.isEmpty()) {
                for (String retval : string.split(" ")) {
                    words.add(retval);
                }
            }

            String neededNumber = words.get((words.size()) - 2);
            int errorAmount = Integer.parseInt(neededNumber);

            return errorAmount;
        } else {
            return 0;
        }
    }

    public static Integer cppErrorAmountDetectionInFile(String string) {

        ArrayList<String> words = new ArrayList<>();
        if (!string.isEmpty()) {
            for (String retval : string.split(" ")) {
                words.add(retval);
            }
            words.addAll(Arrays.asList(string.split(" ")));
        }

        String neededNumber = words.get((words.size()) - 1);
        int errorAmount = Integer.parseInt(neededNumber);

        return errorAmount;
    }

    public static Float pythonRatingCheck(String lastStringInReport) {
        ArrayList<String> splittedWords = new ArrayList<>();
        //String result = "";
        if (!lastStringInReport.isEmpty()) {
            for (String word : lastStringInReport.split(" ")) {
                splittedWords.add(word);
            }
        }
        String matchedConstruction = "";
        for (String word : splittedWords) {
            if (Pattern.compile(".?\\d+(\\.)?(\\d+)?").matcher(word).find()) {
                System.out.println(word);
                matchedConstruction = word;
                break;
            }

        }
        for (String rateValue : matchedConstruction.split("/")) {
            matchedConstruction = rateValue;
            break;
        }

        float rateValue = Float.parseFloat(matchedConstruction);
        logger.info(Float.toString(rateValue));
        return rateValue;
    }

    public static List<String> readFile(String fileDir) {
        List<String> lines = new ArrayList<>();
        try {
            lines = Files.readAllLines(Paths.get(fileDir), Charsets.UTF_8);
        } catch (IOException ex) {
            logger.log(Level.SEVERE, null, ex);
        }
        return lines;
    }

    static Logger logger = Logger.getLogger(TextUtils.class.getSimpleName());
}
