/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package informationsystem.TasksManager;

import informationsystem.xml.TasksXmlReader;
import informationsystem.xml.XmlReader;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;

import java.net.URL;
import java.util.*;
import java.util.logging.Logger;

/**
 * @author user
 */
public class FxmlTasksController implements Initializable {

    private final XmlReader reader = new XmlReader();
    private TaskInfo taskInfo;

    @FXML
    private Accordion tasksWindow;

    @FXML
    private SplitPane tasksDescriptionPane;

    @FXML
    private TextField txtTaskTitle;

    @FXML
    private TextArea txtTaskDescription;

    @FXML
    private TitledPane paneTaskDescription;

    public FxmlTasksController() {

    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        tasksWindow.setExpandedPane(tasksWindow.getPanes().get(0));
        tasksDescriptionPane.setDividerPosition(0, 0.14);
        tasksWindow.expandedPaneProperty().addListener(
                (observable, oldValue, newValue) -> {
                    if (newValue != null) {
                        tasksDescriptionPane.setDividerPosition(0, 0.14);
                    }
                });

        txtTaskTitle.textProperty().addListener((observable, oldValue, newValue) -> {
            if (newValue.isBlank() || newValue.equals(oldValue)) {
                return;
            }
            taskInfo.setTaskName(newValue);
        });

        txtTaskDescription.textProperty().addListener((observable, oldValue, newValue) -> {
            if (newValue.isBlank() || newValue.equals(oldValue)) {
                return;
            }
            taskInfo.setTaskBody(newValue);
        });
    }

    public void shutdown() {
        saveTask(taskInfo);
        Logger.getAnonymousLogger().info("Shutting down");
    }

    public void setTask(TaskInfo taskInfo) {
        if (taskInfo != null) {
            this.taskInfo = taskInfo;
        }

        if (taskInfo.getTaskName() != null) {
            txtTaskTitle.setText(taskInfo.getTaskName());
        }

        if (taskInfo.getTaskBody() != null) {
            txtTaskDescription.setText(taskInfo.getTaskBody());
        }
    }

    public TaskInfo getTaskInfo() {
        return taskInfo;
    }

    private void saveTask(TaskInfo selectedTask) {
        String xmlWithTests = "TestsInfo_v2.xml";
        TasksXmlReader reader = new TasksXmlReader(xmlWithTests);
        reader.saveTask(selectedTask);
    }
}
