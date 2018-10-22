/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package informationsystem;

import com.taskadapter.redmineapi.IssueManager;
import com.taskadapter.redmineapi.RedmineException;
import com.taskadapter.redmineapi.bean.Issue;
import com.taskadapter.redmineapi.bean.Version;
import java.io.IOException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.ResourceBundle;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextField;
import javafx.scene.control.Toggle;
import javafx.scene.control.ToggleGroup;
import org.apache.commons.codec.Charsets;
import org.xml.sax.SAXException;
import com.taskadapter.redmineapi.bean.User;
import java.io.File;
import java.util.Arrays;
import javafx.scene.control.ListView;
import javafx.stage.FileChooser;

/**
 *
 * @author user
 */
public class FXMLDocumentController implements Initializable {

    private final XmlReader reader = new XmlReader();
    private ArrayList<Project> projects = new ArrayList<>();

    @FXML
    private Button buttonDown;

    @FXML
    private ComboBox comboxVersion;

    @FXML
    private ComboBox comboxProject;

    @FXML
    private ComboBox comboxUserName;

    @FXML
    private TextField textFieldURL;

    @FXML
    private TextField IssueToTestNumber;

    @FXML
    private TextField textFieldJavaErrorAmount;

    @FXML
    private CheckBox checkBoxPerevod;

    @FXML
    private ComboBox comboBoxPythonRating;

    @FXML
    private RadioButton radioButtonStatusClosed;

    @FXML
    private RadioButton radioButtonStatusApproved;

    @FXML
    private RadioButton radioButtonAppointForStudent;

    @FXML
    private RadioButton radioButtonAppointForProfessor;

    @FXML
    private CheckBox checkBoxJavaErrScan;

    @FXML
    private CheckBox checkBoxPythonRateScan;

    @FXML
    private Button fileChoose;

    @FXML
    private ListView Students;

    @FXML
    private ListView Tasks;

    private ConnectionWithRedmine connectionToRedmine;
    private RedmineJournalsReader journalReader;

    public void initialize(URL url, ResourceBundle bn) {

        reader.readXML("ProjectKey.xml");

        reader.getOwners().forEach((ProjectOwner p) -> {
            reader.getUsersNameList().add(p.getName());
        });
        ObservableList<String> userNames = FXCollections.observableArrayList(reader.getUsersNameList());
        comboxUserName.setItems(userNames);

        ObservableList<String> projects = FXCollections.observableArrayList(reader.getProjectNameList(userNames.get(0)));
        this.comboxProject.setItems(projects);

        ArrayList<Float> ratingValues = new ArrayList<Float>();
        for (float a = 10; a >= -3.00; a = (float) (a - 0.25)) {
            ratingValues.add(a);
        }

        ObservableList<Float> pythonRatingValues = FXCollections.observableArrayList(ratingValues);
        comboBoxPythonRating.setItems(pythonRatingValues);

        final ToggleGroup groupIssueStatus = new ToggleGroup();
        radioButtonStatusClosed.setToggleGroup(groupIssueStatus);
        radioButtonStatusClosed.setSelected(true);
        radioButtonStatusClosed.requestFocus();
        radioButtonStatusApproved.setToggleGroup(groupIssueStatus);

        final ToggleGroup groupAppointment = new ToggleGroup();
        radioButtonAppointForStudent.setToggleGroup(groupAppointment);
        radioButtonAppointForStudent.setSelected(true);
        radioButtonAppointForStudent.requestFocus();
        radioButtonAppointForProfessor.setToggleGroup(groupAppointment);

    }

    @FXML
    private void handleUserChoice() {

        if (!comboxUserName.getValue().toString().isEmpty()) {
            for (ProjectOwner o : reader.getOwners()) {
                if (comboxUserName.getValue().toString().equals(o.getName())) {
                    projects = o.getHisProjects();
                    Properties.apiAccessKey = o.getApiKey();
                    break;
                }
            }
            for (Project p : projects) {
                reader.getProjectIDsList().add(p.getId());
                reader.getUsersNameList().add(p.getProjectName());
            }
        }
        ObservableList<String> projectNames = FXCollections.observableArrayList(reader.getProjectNameList(comboxUserName.getValue().toString()));

        comboxProject.getItems().removeAll(comboxProject.getItems());
        comboxProject.setValue(null);
        comboxProject.valueProperty().set(null);
        comboxProject.setItems(projectNames);
    }

    @FXML
    private void loadLists(ActionEvent event) {
        ArrayList<String> users = new ArrayList<>();
        ArrayList<String> tasks = new ArrayList<>();
        users = connectionToRedmine.getProjectUsers();
        String tmp = comboxVersion.getValue().toString();
        tasks = connectionToRedmine.getIterationTasks(tmp);
        ObservableList<String> itemsWithNames = Students.getItems();
        itemsWithNames.clear();
        itemsWithNames.addAll(users);

        ObservableList<String> tasksNames = Tasks.getItems();
        tasksNames.clear();
        tasksNames.addAll(tasks);
    }

    @FXML
    private void copyAndAssignIssues(ActionEvent event) {
        int issueId_ = Integer.parseInt(Tasks.getSelectionModel().getSelectedItem().toString().substring(0, 6));
        String nameTo = "";
        //Integer[] issueIds = Arrays.stream().forEach((x) -> {Integer.parseInt(x.toString().substring(0, 6))).toAttay();
        ArrayList<Integer> issueIds = new ArrayList<>();
        for (Object task : Tasks.getItems().toArray()) {
            issueIds.add(Integer.parseInt(task.toString().substring(0, 6)));
        }
        for (Integer issueId : issueIds) {
            for (int i = 0; i < Students.getItems().size(); i++) {
                nameTo = Students.getItems().get(i).toString();
                connectionToRedmine.copyAndAssignIssue(issueId, nameTo);
            }
        }
    }

    @FXML
    private void handleButtonAction(ActionEvent event) {
        Logger.getLogger(FXMLDocumentController.class.getName()).log(Level.INFO, "======Started========\n");
        connectionToRedmine.setProfessorName(comboxUserName.getValue().toString());

        if (!comboxUserName.getValue().toString().isEmpty()
                && !comboxProject.getValue().toString().isEmpty()
                && !comboxVersion.getValue().toString().isEmpty()) {

            List<Issue> issues = null;
            ArrayList<String> journals = null;
            try {
                issues = connectionToRedmine.getMyIssues(comboxVersion.getValue().toString());
            } catch (RedmineException ex) {
                Logger.getLogger(FXMLDocumentController.class.getName()).log(Level.SEVERE, null, ex);
            }

            for (Issue issue : issues) {
                processIssue(issue);
            }

        }
        Logger.getLogger(FXMLDocumentController.class.getName()).log(Level.INFO, "======Finished========\n");
    }

    private void processIssue(Issue issue) {
        processIssue(issue, false);
    }

    private void processIssue(Issue issue, boolean needLog) {
        ArrayList<String> journals;
        if (!issue.getStatusName().equals("Closed") && !issue.getStatusName().equals("Approved")) {
            System.out.println(issue.toString());
            
            try {
                //connectionToRedmine.setVersionForCheck(comboxVersion.getValue().toString(), issue);
                connectionToRedmine.checkAttachments(issue);
            } catch (IOException ex) {
                Logger.getLogger(FXMLDocumentController.class.getName()).log(Level.SEVERE, null, ex);
            }
            
            journals = journalReader.getJournals(issue.getId().toString());
            connectionToRedmine.setStudentName(getStudentName(journals, comboxUserName.getValue().toString()));
        } else if (needLog) {
            System.out.println("Already Closed:" + issue.toString());
        }
    }

    String getStudentName(ArrayList<String> journals, String professorName) {
        String retVal = "";
        for (String journal : journals) {
            if (!journal.equals(comboxUserName.getValue().toString())) {
                retVal = comboxUserName.getValue().toString();
                break;
            }
        }
        return retVal;
    }

    @FXML
    private void handleProjectChoice() {

        if (textFieldURL.getText().isEmpty()) {
            Properties.url = "http://www.hostedredmine.com";
        } else {
            Properties.url = textFieldURL.getText();
        }

        if (!comboxProject.getValue().toString().isEmpty()) {
            for (Project p : projects) {
                if (p.getProjectName().equals(comboxProject.getValue().toString())) {
                    Properties.projectKey = p.getId();
                    break;
                }
            }
        }

        Collection<Version> versions = new ArrayList();

        connectionToRedmine = new ConnectionWithRedmine(Properties.apiAccessKey, Properties.projectKey, Properties.url);
        journalReader = new RedmineJournalsReader(Properties.url, Properties.apiAccessKey);
        try {
            versions = connectionToRedmine.getVersions(Properties.projectKey);
        } catch (RedmineException ex) {
            Logger.getLogger(FXMLDocumentController.class.getName()).log(Level.SEVERE, null, ex);
        }
        Collection<String> versii = new ArrayList<>();
        if (versii != null || !versii.isEmpty()) {
            for (Version ver : versions) {
                versii.add(ver.getName());
            }
        }
        ObservableList<String> targetVersionLost = FXCollections.observableArrayList(versii);
        comboxVersion.setItems(targetVersionLost);

    }

    @FXML
    private void handleJavaErrorScanCheck() {
        if (checkBoxJavaErrScan.isSelected()) {
            connectionToRedmine.setProverka(textFieldJavaErrorAmount.getText());
        }
        //connectionToRedmine.setJavaErrorsAmount(Integer.parseInt(textFieldJavaErrorAmount.getText()));

    }

    @FXML
    private void handlePyhtonRatingScanCheck() {
        if (checkBoxPythonRateScan.isSelected()) {
            //null here
            connectionToRedmine.setRating(Float.parseFloat(comboBoxPythonRating.getValue().toString()));
        }
    }

    @FXML
    private void handlePerevodCheck() {
        if (checkBoxPerevod.isSelected()) {
            connectionToRedmine.setPerevod(true);
        } else {
            connectionToRedmine.setPerevod(false);
        }
    }

    @FXML
    private void handleIssueStatusRadioButton() {

        if (radioButtonStatusApproved.isSelected()) {
            connectionToRedmine.setIssueStatus(4);
        } else if (radioButtonStatusClosed.isSelected()) {
            connectionToRedmine.setIssueStatus(5);
        }
    }

    @FXML
    private void handeRadioButtonAppointments() {

        if (radioButtonAppointForStudent.isSelected()) {
            connectionToRedmine.setAssigneeName(connectionToRedmine.getStudentName());
        } else if (radioButtonAppointForProfessor.isSelected()) {
            connectionToRedmine.setAssigneeName(connectionToRedmine.getProfessorName());
        }
    }

    @FXML
    private void startTests() {
        PyTaskChecker pyChecker = new PyTaskChecker("Принадлежит ли точка области?");
        pyChecker.getTestName3("Принадлежит ли точка области?");
    }

    @FXML
    private void toChooseLocalFile() {

    }

    @FXML
    private void handleButtonSignleIssueCheckAction(ActionEvent event) {
        //Logger.getAnonymousLogger().log(Level.INFO, IssueToTestNumber.getText());
        String issueNum = IssueToTestNumber.getText();
        Integer issueNumLong = 0;
        connectionToRedmine.setProfessorName(comboxUserName.getValue().toString());

        try {
            issueNumLong = Integer.parseInt(issueNum);
            connectionToRedmine.checkSingleIssue(issueNumLong);
            this.processIssue(connectionToRedmine.getIssueByID(issueNumLong), true);
        } catch (Exception ex) {
            Logger.getAnonymousLogger().log(Level.INFO, ex.toString());
        }

    }

    public Collection<String> readFile(String fileDir) {
        Collection<String> lines = new ArrayList<>();
        try {
            lines = Files.readAllLines(Paths.get(fileDir), Charsets.UTF_8);
        } catch (IOException ex) {
            Logger.getLogger(ConnectionWithRedmine.class.getName()).log(Level.SEVERE, null, ex);
        }
        return lines;
    }

}
