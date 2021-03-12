package informationsystem.TasksManager;

import javafx.fxml.FXML;
import javafx.scene.control.Button;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.OpenOption;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.logging.Logger;

public class TaskInfo {
    private String taskId;
    private String taskName;
    private String taskBody;
    private String taskPath;
    private List<String> allAvailableTests = new ArrayList<String>();

    public String getTaskId() {
        return taskId;
    }

    public void setTaskId(String taskId) {
        this.taskId = taskId;
    }

    public String getTaskName() {
        return taskName;
    }

    public void setTaskName(String taskName) {
        this.taskName = taskName;
    }

    public String getTaskBody() {
        return taskBody;
    }

    public void setTaskBody(String taskBody) {
        this.taskBody = taskBody;
    }

    public String getTaskPath() {
        return taskPath;
    }

    public void setTaskPath(String taskPath) {
        this.taskPath = taskPath;
    }

    public void addTest(String testName) {
        allAvailableTests.add(testName);
    }

    @Override
    public boolean equals(Object other) {
        if (other == null) return false;
        if (other instanceof TaskInfo) {
            return taskId.equals(((TaskInfo) other).getTaskId());
        } else {
            return false;
        }
    }

    @Override
    public int hashCode() {
        return taskId.hashCode();
    }

    public String getTestContent(String value, Boolean needAnswer) {
        String testFileName = allAvailableTests.stream().filter(item -> item.equals(value)).findFirst().get();
        if (needAnswer) {
            testFileName = testFileName.replace(".t", ".a");
        }

        try {
            return Files.readString(Path.of(TasksKeeper.PathToTests, taskPath, testFileName));
        } catch (IOException e) {
            logger.info(e.toString());
        }

        return ((needAnswer) ? "answer" : "test") + " not found";
    }

    public void setTests(List<String> tests) {
        allAvailableTests.clear();
        for (String testName : tests) {
            allAvailableTests.add(testName);
        }
    }

    public void setTestInput(String testFileName, String newValue) {
        try {
            Files.writeString(Path.of(TasksKeeper.PathToTests, taskPath, testFileName), newValue);
        } catch (IOException e) {
            logger.info(e.toString());
        }
    }

    public void setTestOutput(String testFileName, String newValue) {
        try {
            Files.writeString(
                    Path.of(TasksKeeper.PathToTests, taskPath, testFileName.replace(".t", ".a")),
                    newValue);
        } catch (IOException e) {
            logger.info(e.toString());
        }
    }
    public void saveAllData() {

    }

    private static Logger logger = Logger.getLogger(TaskInfo.class.getSimpleName());
}
