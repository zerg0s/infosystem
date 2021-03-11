/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package informationsystem.TasksManager;

import com.taskadapter.redmineapi.RedmineException;
import com.taskadapter.redmineapi.bean.Issue;
import com.taskadapter.redmineapi.bean.Version;
import data.*;
import informationsystem.RedmineConnectionProperties;
import informationsystem.XmlReader;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.CheckBoxListCell;
import javafx.stage.Modality;
import javafx.stage.Stage;
import javafx.util.StringConverter;
import org.apache.commons.codec.Charsets;
import redmineManagement.ConnectionWithRedmine;
import redmineManagement.RedmineJournalsReader;

import java.io.IOException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author user
 */
public class FxmlTasksController implements Initializable {

    private final XmlReader reader = new XmlReader();

    @FXML
    private Accordion tasksWindow;

    @FXML
    private SplitPane tasksDescriptionPane;

    @FXML
    private TextField txtTaskTitle;

    @FXML
    private TextArea txtTaskDescription;


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        tasksWindow.setExpandedPane(tasksWindow.getPanes().get(0));
        tasksDescriptionPane.setDividerPosition(0, 0.14);
    }

    public void shutdown() {
        Logger.getAnonymousLogger().info("Shutting down");
    }

    public void setTask(TaskInfo taskInfo) {
        if (taskInfo.getTaskName() != null) {
            txtTaskTitle.setText(taskInfo.getTaskName());
        }
        if (taskInfo.getTaskBody() != null) {
            txtTaskDescription.setText(taskInfo.getTaskBody());
        }
    }
}
