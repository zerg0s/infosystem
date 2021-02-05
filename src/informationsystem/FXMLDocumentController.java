/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package informationsystem;

import com.taskadapter.redmineapi.RedmineException;
import com.taskadapter.redmineapi.bean.Issue;
import com.taskadapter.redmineapi.bean.Version;

import java.io.IOException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;

import data.*;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.ComboBox;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextField;
import javafx.scene.control.ToggleGroup;
import org.apache.commons.codec.Charsets;
import javafx.scene.control.ListView;
import redmineManagement.ConnectionWithRedmine;
import redmineManagement.RedmineJournalsReader;

/**
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
    private CheckBox easyModechk;

    @FXML
    private CheckBox checkAllIterations;

    @FXML
    private CheckBox checkBoxPythonRateScan;

    @FXML
    private Button fileChoose;

    @FXML
    private ListView Students;

    @FXML
    private ListView Tasks;

    @FXML
    private CheckBox checkboxNeedLint;

    private ConnectionWithRedmine connectionToRedmine;
    private RedmineJournalsReader journalReader;
    private boolean needLog = false;
    private RedmineConnectionProperties props = new RedmineConnectionProperties();

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
                    props.apiAccessKey = o.getApiKey();
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

        boolean easyMode = easyModechk.isSelected();
        boolean checkAll = checkAllIterations.isSelected();
        String iterationName = !checkAll ? comboxVersion.getValue().toString() : "";

        if (!comboxUserName.getValue().toString().isEmpty()
                && !comboxProject.getValue().toString().isEmpty()) {
            List<Issue> issues = null;
            ArrayList<String> journals = null;
            try {
                issues = connectionToRedmine.getMyIssues(iterationName);
            } catch (RedmineException ex) {
                Logger.getLogger(FXMLDocumentController.class.getName()).log(Level.SEVERE, null, ex);
            }

            for (Issue issue : issues) {
                processIssue(issue, easyMode);
            }

        }
        Logger.getLogger(FXMLDocumentController.class.getName()).log(Level.INFO, "======Finished========\n");
    }

    private void processIssue(Issue issue, boolean easyMode) {
        processIssue(issue, false, false, easyMode);
    }

    private void processIssueForced(Issue issue) {
        processIssueForced(issue, false);
    }

    private void processIssueForced(Issue issue, boolean needLog) {
        processIssue(issue, false, true, false);
    }

    private void processConfiguredIssue(ConfiguredTask task) {
        processIssue(task);
    }

    private void processIssue(Issue issue, boolean needLog, boolean needForced, boolean easyMode) {
        ArrayList<String> journals;
        if (!issue.getStatusName().equals("Closed") && !issue.getStatusName().equals("Approved")) {
            Logger.getAnonymousLogger().info(issue.toString());
            Double pyRating = 10.0;
            int javaErrorLimit = 5;
            if (comboBoxPythonRating.getValue() != null) {
                pyRating = Double.parseDouble(comboBoxPythonRating.getValue().toString());
            }

            if (textFieldJavaErrorAmount.getText() != null) {
                javaErrorLimit = Integer.parseInt(textFieldJavaErrorAmount.getText());
            }

            //connectionToRedmine.setVersionForCheck(comboxVersion.getValue().toString(), issue);
            String student = getStudentName(journalReader.getJournals(issue.getId().toString()), connectionToRedmine.getProfessorName());
            Logger.getAnonymousLogger().info("Student is " + student);
            ConfiguredTask confTask = new ConfiguredTask(issue, student,
                    needForced,
                    connectionToRedmine.getLint(), pyRating, javaErrorLimit, easyMode);
            connectionToRedmine.checkIssueAttachments(confTask);
            //connectionToRedmine.checkAttachments(issue, needForced);

            journals = journalReader.getJournals(issue.getId().toString());
            connectionToRedmine.setStudentName(getStudentName(journals, comboxUserName.getValue().toString()));
        } else if (needLog) {
            Logger.getAnonymousLogger().info("Already Closed:" + issue.toString());
        }
    }

    private void processIssue(ConfiguredTask task) {
        Issue issue = task.getIssue();
        if (!isIssueInDeadStatus(issue)) {
            System.out.println(issue.toString());
            connectionToRedmine.setStudentName(task.getTaskCompleter());
            connectionToRedmine.checkIssueAttachments(task);
        } else if (needLog) {
            System.out.println("Already Closed:" + issue.toString());
        }
    }

    private boolean isIssueInDeadStatus(Issue issue) {
        String status = issue.getStatusName();
        return status.equals("Closed") || status.equals("Approved")
                || status.equals("Blocked");
    }

    String getStudentName(ArrayList<String> journals, String professorName) {
        String retVal = "";
        for (String journal : journals) {
            if (!journal.equals(professorName)) {
                retVal = journal;
                break;
            }
        }
        return retVal;
    }

    @FXML
    private void handleProjectChoice() {
        if (textFieldURL.getText().isEmpty()) {
            props.url = "https://www.hostedredmine.com";
        } else {
            props.url = textFieldURL.getText();
        }

        if (!comboxProject.getValue().toString().isEmpty()) {
            for (Project p : projects) {
                if (p.getProjectName().equals(comboxProject.getValue().toString())) {
                    props.projectKey = p.getId();
                    break;
                }
            }
        }

        Collection<Version> versions = new ArrayList();

        connectionToRedmine = new ConnectionWithRedmine(props.apiAccessKey, props.projectKey, props.url);
        journalReader = new RedmineJournalsReader(props.url, props.apiAccessKey);
        try {
            versions = connectionToRedmine.getVersions(props.projectKey);
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
        int errorAmmount = Integer.parseInt(textFieldJavaErrorAmount.getText());
        connectionToRedmine.setJavaErrorsAmount(errorAmmount);
    }

    @FXML
    private void handlePyhtonRatingScanCheck() {
        if (checkBoxPythonRateScan.isSelected()) {
            //null here
            float pythonRating = Float.parseFloat(comboBoxPythonRating.getValue().toString());
            connectionToRedmine.setRating(pythonRating);
        }
    }

    @FXML
    private void handlePerevodCheck() {
        if (checkBoxPerevod.isSelected()) {
            connectionToRedmine.setReturnBackIfAllOk(true);
        } else {
            connectionToRedmine.setReturnBackIfAllOk(false);
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
    private void handleCheckboxNeedLint() {
        if (!checkboxNeedLint.isSelected()) {
            connectionToRedmine.setLint(false);
            checkBoxJavaErrScan.setSelected(false);
            checkBoxPythonRateScan.setSelected(false);
        } else {
            connectionToRedmine.setLint(true);
            checkBoxJavaErrScan.setSelected(true);
            checkBoxPythonRateScan.setSelected(true);
        }
    }

    @FXML
    //Загружает закрытые задачи для составления списка сдавших
    private void downloadResults() {
        String currentVersion = comboxVersion.getValue().toString();
        List<Issue> tasks = connectionToRedmine.getClosedIssues(currentVersion);
        ArrayList<StudentsIssue> StudentsIssues = new ArrayList<>();
        for (Issue task : tasks) {
            String taskStatusName = task.getStatusName();
            if (taskStatusName.equals("Closed")) {
                StudentsIssue studentsIssue = new StudentsIssue();
                studentsIssue.setStudentsName(task.getAssigneeName());
                studentsIssue.setIssueName(task.getSubject());
                StudentsIssues.add(studentsIssue);
            }
        }
        HashMap<String, ArrayList<String>> issuesOfTheStudent = new HashMap<String, ArrayList<String>>();
        for (StudentsIssue issue : StudentsIssues) {
            if (!issuesOfTheStudent.containsKey(issue.getStudentsName())) {
                issuesOfTheStudent.put(issue.getStudentsName(), new ArrayList<String>());
            }
            issuesOfTheStudent.get(issue.getStudentsName()).add(issue.getIssueName());
        }
        new FileOperator(currentVersion + ".txt").saveDataToFile(issuesOfTheStudent);
    }

    @FXML
    private void toChooseLocalFile() {
    }

    @FXML
    private void handleButtonSingleIssueCheckAction(ActionEvent event) {
        String issueNum = IssueToTestNumber.getText();
        Integer issueNumLong = 0;
        boolean easyMode = easyModechk.isSelected();
        connectionToRedmine.setProfessorName(comboxUserName.getValue().toString());
        try {
            issueNumLong = Integer.parseInt(issueNum);
            Issue currentIssue = connectionToRedmine.getIssueByID(issueNumLong);
            Boolean isLintNeeded = checkboxNeedLint.isSelected();
            Boolean isForceCheck = true;
            Double pyRating = 10.0;
            int javaErrorLimit = 5;
            if (comboBoxPythonRating.getValue() != null) {
                pyRating = Double.parseDouble(comboBoxPythonRating.getValue().toString());
            }

            if (textFieldJavaErrorAmount.getText() != null) {
                javaErrorLimit = Integer.parseInt(textFieldJavaErrorAmount.getText());
            }

            String student = getStudentName(journalReader.getJournals(currentIssue.getId().toString()), connectionToRedmine.getProfessorName());

            ConfiguredTask task = new ConfiguredTask(currentIssue, student, isForceCheck, isLintNeeded, pyRating, javaErrorLimit, easyMode);
            Logger.getAnonymousLogger().info(task.toString());

            this.processConfiguredIssue(task);

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
