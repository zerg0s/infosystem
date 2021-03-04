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
import java.util.regex.Matcher;
import java.util.regex.Pattern;

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
import javafx.scene.control.cell.CheckBoxListCell;
import javafx.util.StringConverter;
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

    @FXML
    private ComboBox lintErrorsNotificationsType;

    private ConnectionWithRedmine connectionToRedmine;
    private RedmineJournalsReader journalReader;
    private boolean needLog = false;
    private RedmineConnectionProperties props = new RedmineConnectionProperties();
    private String projectKeyXml = "ProjectKey.xml";

    public void initialize(URL url, ResourceBundle bn) {

        reader.readXML(projectKeyXml);

        reader.getOwners().forEach((ProjectOwner p) -> {
            reader.getUsersNameList().add(p.getName());
        });

        String selectedSupervisor = reader.getSelectedSupervisor();
        if (!selectedSupervisor.isEmpty()) {
            comboxUserName.setValue(selectedSupervisor);
        }

        if (reader.getSelectedProject() != null) {
            comboxProject.setValue(reader.getSelectedProject().getProjectName());
            props.projectKey = reader.getSelectedProject().getId();
        }
        if (reader.getSelectedVersion() != null) {
            comboxVersion.setValue(reader.getSelectedVersion());
            props.iterationName = comboxVersion.getValue().toString();
        }

        ObservableList<String> userNames = FXCollections.observableArrayList(reader.getUsersNameList());
        comboxUserName.setItems(userNames);

        //this.comboxProject.setItems(projects);

        ArrayList<Float> ratingValues = new ArrayList<Float>();
        for (float a = 10; a >= -3.00; a = (float) (a - 0.25)) {
            ratingValues.add(a);
        }
        comboBoxPythonRating.setItems(FXCollections.observableArrayList(ratingValues));

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

        easyModechk.setSelected(reader.isEasyMode());
        checkAllIterations.setSelected(reader.needCheckAllIterations());

        initializeSelectedProject();
        setSelectedLintMode();
    }

    private void setSelectedLintMode() {
        if (reader.getSelectedLintMode() == null) {
            return;
        }
        lintErrorsNotificationsType.setItems(FXCollections.observableArrayList(getData()));
        ObservableList<LintReportMode> items = lintErrorsNotificationsType.getItems();
        int itemToSelect = items.get(0).getModeNumber();
        for (int i = 0; i < items.size(); i++) {
            if (items.get(i).getModeNumber() == reader.getSelectedLintMode().getModeNumber()) {
                itemToSelect = i;
                break;
            }
        }
        lintErrorsNotificationsType.getSelectionModel().select(itemToSelect);
    }

    private List<LintReportMode> getData() {
        List<LintReportMode> retList = new ArrayList<LintReportMode>();
        retList.add(LintReportMode.valueOf("Default - По умолчанию(показывать, где ошибки)"));
        retList.add(LintReportMode.valueOf("Hard - Только количество ошибок"));
        retList.add(LintReportMode.valueOf("Nightmare - Только наличие ошибок"));
        return retList;
    }

    private void initializeSelectedProject() {
        if (comboxUserName.getValue() != null) {
            if (!comboxUserName.getValue().toString().isEmpty()) {
                for (ProjectOwner owner : reader.getOwners()) {
                    if (comboxUserName.getValue().toString().equals(owner.getName())) {
                        projects = owner.getHisProjects();
                        props.apiAccessKey = owner.getApiKey();
                        comboxProject.setItems(FXCollections.observableArrayList(projects.stream().map((pr) ->
                                pr.getProjectName()
                        ).toArray()));
                        break;
                    }
                }
            }
        }

        String selectedProject = (String) comboxProject.getValue();
        if (selectedProject != null) {
            if (!selectedProject.isEmpty()) {
                for (Project pr : projects) {
                    if (pr.getProjectName().equals(selectedProject)) {
                        props.projectKey = pr.getId();
                        break;
                    }
                }
            }
        }
        props.url = fillUrlProps(textFieldURL);

        if (!props.projectKey.isEmpty() && !props.apiAccessKey.isEmpty()
                && !props.url.isEmpty() && !props.iterationName.isEmpty()) {
            Logger.getAnonymousLogger().info("Тест русских букв!\n");
            Logger.getAnonymousLogger().info("Selected values: " + props.url + "\n"
                    + props.apiAccessKey.substring(props.apiAccessKey.length() - 3) + "\n" + props.projectKey
                    + "\n" + props.iterationName);
            new Thread(() -> {
                connectionToRedmine = new ConnectionWithRedmine(props.apiAccessKey, props.projectKey, props.url);
                journalReader = new RedmineJournalsReader(props.url, props.apiAccessKey);
            }).run();
        }
    }

    private String fillUrlProps(TextField textFieldURL) {
        String url = "";

        if (textFieldURL != null || textFieldURL.getText() != null || textFieldURL.getText().isEmpty()) {
            url = "https://www.hostedredmine.com";
        } else {
            url = textFieldURL.getText();
        }

        return url;
    }

    @FXML
    private void handleUserChoice() {
        if (!comboxUserName.getValue().toString().isEmpty()) {
            for (ProjectOwner owner : reader.getOwners()) {
                if (comboxUserName.getValue().toString().equals(owner.getName())) {
                    projects = owner.getHisProjects();
                    props.setNewApiAccessKey(owner.getApiKey());
                    break;
                }
            }
        }

        reFillDataForCombobox(comboxProject, reader.getProjectNameList(comboxUserName.getValue().toString()));
        reFillDataForCombobox(comboxVersion, new ArrayList<String>());
    }

    private void reFillDataForCombobox(ComboBox toCbxToBeRefilled, ArrayList<String> data) {
        ObservableList<String> projectNames = FXCollections.observableArrayList(data);

        toCbxToBeRefilled.getItems().removeAll(toCbxToBeRefilled.getItems());
        toCbxToBeRefilled.setValue(null);
        toCbxToBeRefilled.valueProperty().set(null);
        toCbxToBeRefilled.setItems(projectNames);
    }

    @FXML
    private void loadLists(ActionEvent event) {

        ArrayList<CellWithCheckBox> users = new ArrayList<>();
        ArrayList<CellWithCheckBox> tasks = new ArrayList<>();
        for (String user : connectionToRedmine.getProjectUsers()) {
            users.add(new CellWithCheckBox(user, false));
        }

        for (String task : connectionToRedmine.getIterationFreeTasks(comboxVersion.getValue().toString())) {
            tasks.add(new CellWithCheckBox(task, false));
        }

//        users.add(new CellWithCheckBox("TestUser", false));
//        tasks.add(new CellWithCheckBox("123456 - test task",false));

        StringConverter<CellWithCheckBox> converter = new StringConverter<CellWithCheckBox>() {
            @Override
            public String toString(CellWithCheckBox cell) {
                return cell.getTitle();
            }

            // not actually used by CheckBoxListCell
            @Override
            public CellWithCheckBox fromString(String string) {
                return null;
            }
        };

        Students.setCellFactory(CheckBoxListCell.forListView(CellWithCheckBox::completedProperty, converter));
        Tasks.setCellFactory(CheckBoxListCell.forListView(CellWithCheckBox::completedProperty, converter));

        ObservableList<CellWithCheckBox> itemsWithNames = Students.getItems();
        itemsWithNames.clear();
        itemsWithNames.addAll(users);

        ObservableList<CellWithCheckBox> tasksNames = Tasks.getItems();
        tasksNames.clear();
        tasksNames.addAll(tasks);
    }

    @FXML
    private void copyAndAssignIssues(ActionEvent event) {
        Pattern pattern = Pattern.compile("\\d{6,7}", Pattern.CASE_INSENSITIVE);

        Tasks.getItems().stream().forEach(item -> ((CellWithCheckBox) item).setCompleted(true));
        Students.getItems().stream().forEach(item -> ((CellWithCheckBox) item).setCompleted(true));
        String nameTo = "";

        ArrayList<Integer> issueIds = new ArrayList<>();
        for (Object task : Tasks.getItems().toArray()) {
            Matcher m = pattern.matcher(((CellWithCheckBox) task).getTitle());
            m.find();
            issueIds.add(Integer.parseInt(m.group()));
        }

        for (Integer issueId : issueIds) {
            for (int i = 0; i < Students.getItems().size(); i++) {
                nameTo = ((CellWithCheckBox) Students.getItems().get(i)).getTitle();
                connectionToRedmine.copyAndAssignIssue(issueId, nameTo);
            }
        }
    }

    @FXML
    private void copyAndAssignSelectedIssues(ActionEvent event) {
        Pattern pattern = Pattern.compile("\\d{6,7}", Pattern.CASE_INSENSITIVE);

        String nameTo = "";

        ArrayList<Integer> issueIds = new ArrayList<>();
        for (Object task : Tasks.getItems().toArray()) {
            CellWithCheckBox cell = (CellWithCheckBox) task;
            if (cell.isCompleted()) {
                Matcher m = pattern.matcher(cell.getTitle());
                m.find();
                issueIds.add(Integer.parseInt(m.group()));
            }
        }

        for (Integer issueId : issueIds) {
            for (Object student : Students.getItems()) {
                CellWithCheckBox cell = (CellWithCheckBox) student;
                if (cell.isCompleted()) {
                    nameTo = cell.getTitle();
                    connectionToRedmine.copyAndAssignIssue(issueId, nameTo);
                }
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
                    connectionToRedmine.getLint(), pyRating, javaErrorLimit,
                    easyMode, (LintReportMode) lintErrorsNotificationsType.getValue());
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

    private String getStudentName(ArrayList<String> journals, String professorName) {
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
        props.url = fillUrlProps(textFieldURL);
        for (Project p : projects) {
            if (comboxProject.getValue() != null && p.getProjectName().equals(comboxProject.getValue().toString())) {
                props.projectKey = p.getId();
                break;
            }
        }

        if (!props.projectKey.isEmpty()) {
            connectionToRedmine = new ConnectionWithRedmine(props.apiAccessKey, props.projectKey, props.url);
            journalReader = new RedmineJournalsReader(props.url, props.apiAccessKey);

            Collection<Version> versions = new ArrayList();
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

            ConfiguredTask task = new ConfiguredTask(currentIssue, student, isForceCheck,
                    isLintNeeded, pyRating, javaErrorLimit, easyMode,
                    (LintReportMode) lintErrorsNotificationsType.getValue());
            if (task.getLintReportMode() == null) {
                task.setLintReportMode(new LintReportMode(0, "Default"));
            }
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

    public void shutdown() {
        HashMap<String, String> map = new HashMap<String, String>();
        putToSettings(map, "isEasyMode", easyModechk.isSelected());
        putToSettings(map, "checkAllIterations", checkAllIterations.isSelected());
        putToSettings(map, "SelectedSupervisor", comboxUserName.getValue());
        putToSettings(map, "SelectedIteration", comboxVersion.getValue());

        if (comboxProject.getValue() != null) {
            putToSettings(map, "SelectedProjectName", comboxProject.getValue());
            putToSettings(map, "SelectedProjectId", props.projectKey);
        }

        if (lintErrorsNotificationsType.getValue() != null) {
            LintReportMode lintReportMode = (LintReportMode) lintErrorsNotificationsType.getValue();
            putToSettings(map, "SelectedLintMode", lintReportMode.toStringForXml());
        }

        reader.saveSettings(projectKeyXml, map);
    }

    private void putToSettings(Map<String, String> map, Object key, Object value) {
        if (map == null || key == null || value == null) return;
        map.put(String.valueOf(key), String.valueOf(value));
    }
}
