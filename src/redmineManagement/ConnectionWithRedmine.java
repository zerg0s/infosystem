/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package redmineManagement;

import com.taskadapter.redmineapi.AttachmentManager;
import com.taskadapter.redmineapi.Include;
import com.taskadapter.redmineapi.IssueManager;
import com.taskadapter.redmineapi.MembershipManager;
import com.taskadapter.redmineapi.ProjectManager;
import com.taskadapter.redmineapi.RedmineException;
import com.taskadapter.redmineapi.RedmineManager;
import com.taskadapter.redmineapi.RedmineManagerFactory;
import com.taskadapter.redmineapi.UserManager;
import com.taskadapter.redmineapi.bean.*;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.nio.file.StandardOpenOption;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.regex.Pattern;

import data.ConfiguredTask;
import informationsystem.*;
import lintsForLangs.MyCheckStyle;
import lintsForLangs.MyCppLint;
import lintsForLangs.MyPylint;
import lintsForLangs.PhrasesGenerator;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import org.apache.commons.codec.Charsets;
import org.apache.http.entity.ContentType;
import taskCheckers.JavaTaskChecker;
import taskCheckers.PyTaskChecker;
import tools.Translit;
//Status_id HELP 
// 0 - new
// 1 - assigned
// 2 - in progress
// 3 - resolved 
// 4 - approved
// 5 - closed

/**
 * @author user
 */
public class ConnectionWithRedmine {
    static final String myFilesDir = ".\\myFiles\\";

    boolean returnBackIfAllOk = true;
    boolean lint = true;
    private String url;
    private String apiAccessKey;
    private String projectKey;
    private Integer queryId = null;
    private Integer neededJavaErrorAmount;
    private float neededPythonRating = (float) 10.0;
    private String proverka = "";
    private Integer issueStatus;
    private String studentName = "";
    private String professorName = "";
    private String assigneeName = "";

    private RedmineManager mgr;
    private IssueManager issueManager;
    private AttachmentManager attachmentManager;
    private List<Issue> issues;
    private ProjectManager projectManager;
    private List<Project> projects;
    private UserManager userManager;
    private List<User> users;
    private List<Membership> projectsUsers;
    private List<Version> versions;

    public ConnectionWithRedmine(String apikey, String projectkey2, String url) {
        this.apiAccessKey = apikey;
        this.projectKey = projectkey2;
        this.url = url;
        this.mgr = RedmineManagerFactory.createWithApiKey(url, apiAccessKey);
        this.issueManager = mgr.getIssueManager();
        this.attachmentManager = mgr.getAttachmentManager();
        this.projectManager = mgr.getProjectManager();
        this.userManager = mgr.getUserManager();

        try {
            projectsUsers = mgr.getMembershipManager().getMemberships(this.projectKey);
        } catch (RedmineException ex) {
            Logger.getLogger(ConnectionWithRedmine.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public void setRating(float value) {
        this.neededPythonRating = value;
    }

    public void setJavaErrorsAmount(Integer value) {
        this.neededJavaErrorAmount = value;
    }

    public void setReturnBackIfAllOk(Boolean value) {
        this.returnBackIfAllOk = value;
    }

    public void setIssueStatus(Integer value) {
        this.issueStatus = value;
    }

    public void setAssigneeName(String value) {
        this.assigneeName = value;
    }

    public Issue setIssueAssigneeNameForIssue(Issue issue, String value) {
        int id = 0;
        for (Membership user : projectsUsers) {
            if (user.getUserName().equalsIgnoreCase(value)) {
                id = user.getUserId();
                break;
            }
        }
        if (id != 0) {
            issue.setAssigneeId(id);
            issue.setAssigneeName(value);
        } else {
            Logger.getLogger(this.getClass().getName()).warning("Can't find user" + value);
        }
        return issue;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String value) {
        this.studentName = value;
    }

    public String getProfessorName() {
        return professorName;
    }

    public void setProfessorName(String value) {
        this.professorName = value;
    }

    public void checkAttachments(Issue issue) throws IOException {
        checkAttachments(issue, false);
    }

    public void checkAttachmentsForced(Issue issue) throws IOException {
        checkAttachments(issue, true);
    }

    /**
     * @param issue                     - RedmineItem для проверки
     * @param needToCheckAlreadyChecked TRUE - всегда перепроверять, игнорируя
     *                                  уже проверенные, FALSE - учитывать ранее проверенные аттачи
     * @throws IOException
     */
    // deprecated. only for review purpose
    public void checkAttachments(Issue issue, boolean needToCheckAlreadyChecked) throws IOException {
        Collection<Attachment> issueAttachment = issue.getAttachments();
        ArrayList<Attachment> issueAttachments = new ArrayList<>(issueAttachment);
        File dir = new File(myFilesDir);
        dir.mkdirs();
        //Check only latest attach, the rest are already history
        Attachment attach = getLatestCheckableAttach(issueAttachments).get();
        //for (Attachment attach : issueAttachments)
        {
            if (attach.getFileName().endsWith(".py") || attach.getFileName().endsWith(".java")
                    || attach.getFileName().endsWith(".cpp")) {
                int wasChecked = -1;
                //Если не надо перепроверять ранее проверенные, смотрим, не нашлось ли ранее проверенных
                if (!needToCheckAlreadyChecked) {
                    wasChecked = isAttachmentIdWasEarlierChecked(attach.getId());
                }
                //Проверяем, если не проверяли ранее или надо обязательно проверять
                if (needToCheckAlreadyChecked || (wasChecked == 0)) {
                    //if (!(new PyTaskChecker(issue.getSubject())).getNameForKnownTest(issue.getSubject()).equals("")) {

                    String fileToManage = ".\\myFiles\\" + makeUsableFileName(
                            attach.getFileName(),
                            attach.getAuthor().getFullName(),
                            issue.getSubject());
                    downloadAttachments(attach.getContentURL(), apiAccessKey, fileToManage);

                    if (attach.getFileName().endsWith(".py")) {
                        int checkRes = -1;
                        if (doPyLint(issue, fileToManage)) {
                            PyTaskChecker checker = new PyTaskChecker(issue.getSubject(), fileToManage);
                            if (!checker.getNameForKnownTest(issue.getSubject()).equals("")) {
                                checkRes = doPyTaskCheck(checker, issue);
                            }
                        }
                        if (checkRes != -1) {
                            String studentsName = getStudentsName(issue.getId(), this.professorName);
                            System.out.println(checkRes + "(after tests - back to Student) - " + studentsName);
                            this.setIssueAssigneeNameForIssue(issue, studentsName);
                            if (checkRes == 1) {
                                issue.setStatusId(5);
                            }
                            this.updateIssue(issue);
                        }
                    }

                    if (attach.getFileName().endsWith(".java")) {
                        doJavaLint(attach.getFileName());
                    }

                    if (attach.getFileName().endsWith(".cpp")) {
                        doCppLint(attach, issue);
                    }
                    // cleanDirectory(new File(".\\myFiles\\"));
                }
            }
        }
    }

    public void checkIssueAttachments(ConfiguredTask task) {
        Issue issue = task.getIssue();
        Collection<Attachment> issueAttachment = issue.getAttachments();
        List<Attachment> issueAttachments = new ArrayList<Attachment>(issueAttachment);
        new File(myFilesDir).mkdirs();

        //Check only latest attach, the rest are already history
        Optional<Attachment> nullableAttach =  getLatestCheckableAttach(issueAttachments);
        Attachment attach;

        if (!nullableAttach.isPresent()){
            Logger.getAnonymousLogger().info("Can't find suitable attaches for " + task);
            return;
        }
        attach = nullableAttach.get();
        //for (Attachment attach : issueAttachments)
        {
            String attachFileName = attach.getFileName();
            if (isKnownAttachExtention(attachFileName)) {
                int wasCheckedEarlier = -1;
                //Если не надо перепроверять ранее проверенные, смотрим, не нашлось ли ранее проверенных
                if (!task.isNeededForceCheck()) {
                    try {
                        wasCheckedEarlier = isAttachmentIdWasEarlierChecked(attach.getId());
                    } catch (IOException ex) {
                        Logger.getLogger(ConnectionWithRedmine.class.getName()).warning(ex.toString());
                    }
                }
                //Проверяем файл аттача: 1)если не проверяли ранее 0) надо обязательно проверять
                if (task.isNeededForceCheck() || wasCheckedEarlier == 0) {
                    String fileToManage = myFilesDir + makeUsableFileName(
                            attachFileName,
                            attach.getAuthor().getFullName(),
                            issue.getSubject());
                    try {
                        downloadAttachments(attach.getContentURL(), apiAccessKey, fileToManage);
                    } catch (IOException ex) {
                        Logger.getLogger(ConnectionWithRedmine.class.getName()).warning(ex.toString());
                    }

                    if (attachFileName.endsWith(".py")) {
                        processPythonFile(task, issue, fileToManage);
                    }
                    if (attachFileName.endsWith(".zip") || attachFileName.endsWith(".java")) {
                        processJavaFile(task, issue, fileToManage);
                    }
                    //for cpp we can do lint only now :(
                    if (attachFileName.endsWith(".cpp")) {
                        doCppLint(fileToManage, issue);
                    }
                }
                // cleanDirectory(new File(".\\myFiles\\"));
            }
        }
    }

    private Optional<Attachment> getLatestCheckableAttach(List<Attachment> issueAttachments) {
        if (issueAttachments == null && issueAttachments.size() == 0) {
            return Optional.empty();
        }
        int idMax = 0;
        int maxIndex = 0;
        for (int i = 0; i < issueAttachments.size(); i++) {
            if (isKnownAttachExtention(issueAttachments.get(i).getFileName()) &&
                    issueAttachments.get(i).getId() > idMax)
            idMax = issueAttachments.get(i).getId();
            maxIndex = i;
        }
        if (idMax == 0) {
            return Optional.empty();
        }
        return  Optional.of(issueAttachments.get(maxIndex));
    }

    private void processJavaFile(ConfiguredTask task, Issue issue, String fileToManage) {
        int processResult = -1;
        boolean javaLintResult = true;
        if (task.isLintRequired()) {
            javaLintResult = doJavaLint(task, fileToManage);
        }
        //if javaLint was OK or not required
        if (javaLintResult) {
            JavaTaskChecker javaChecker = new JavaTaskChecker(issue.getSubject(), fileToManage);
            String testFolder = javaChecker.getNameForKnownTest();
            if (!testFolder.equals("")) {
                processResult = doJavaTaskCheck(javaChecker, issue);
            }
        } else {
            String student = task.getTaskCompleter();
            this.setIssueAssigneeNameForIssue(issue, student);
        }

        processResult(task, issue, processResult);
    }

    private void processResult(ConfiguredTask task, Issue issue, int processResult) {
        if (processResult != -1) {
            System.out.println(processResult + "(after tests - back to Student) - " + task.getTaskCompleter());
            this.setIssueAssigneeNameForIssue(issue, task.getTaskCompleter());
            if (processResult == 1 && this.returnBackIfAllOk) {
                issue.setStatusId(5);
            }
            if (processResult == 1 && !this.returnBackIfAllOk) {
                issue.setStatusId(4);
            }
        }
        this.updateIssue(issue);
    }

    private void processPythonFile(ConfiguredTask task, Issue issue, String fileToManage) {
        int processResult = -1;
        boolean pyLintResult = true;
        if (task.isLintRequired()) {
            pyLintResult = doPyLint(task, fileToManage);
        }
        if (pyLintResult) {
            PyTaskChecker pyChecker = new PyTaskChecker(issue.getSubject(), fileToManage);
            String testFolder = pyChecker.getNameForKnownTest();
            if (!testFolder.equals("")) {
                processResult = doPyTaskCheck(pyChecker, issue);
            }
        }

        processResult(task, issue, processResult);
    }

    private boolean isKnownAttachExtention(String attachName) {
        return attachName.endsWith(".py") || attachName.endsWith(".java") || attachName.endsWith(".zip") || attachName.endsWith(".cpp");
    }

    private void doCppLint(Attachment attach, Issue issue) {
        String fileToManage = myFilesDir + makeUsableFileName(
                attach.getFileName(),
                attach.getAuthor().getFullName(),
                issue.getSubject());
        doCppLint(fileToManage, issue);
    }

    private void doCppLint(String attachFileName, Issue issue) {
        new MyCppLint().startCpplint(attachFileName);
        this.uploadAttachment(issue, myFilesDir + attachFileName + "_errorReport.txt");
        String lastLine = readLastLineInFile(myFilesDir + attachFileName + "_errorReport.txt");
        int studentCppErrorAmount = this.cppErrorAmountDetectionInFile(lastLine);
        System.out.println("we have " + studentCppErrorAmount);
        System.out.println("we have line " + lastLine);
        issue.setNotes(lastLine);
        this.updateIssue(issue);
    }

    private void doJavaLint(String fullFileName) {
        doJavaLint(null, fullFileName);
    }

    private boolean doJavaLint(ConfiguredTask task, String fullFileName) {
        new MyCheckStyle().startCheckStyle(fullFileName);
        String lastLine = readLastLineInFile(fullFileName + "_errorReport.txt");
        int studentJavaErrorAmount = this.javaErrorAmountDetectionInFile(lastLine);

        if (studentJavaErrorAmount > task.getMaxJavaLintErrors()) {
            if (task != null) {
                this.uploadAttachment(task.getIssue(), fullFileName + "_errorReport.txt");
                task.getIssue().setNotes("Some corrections are required. See the attached file");
            }
            return false;
        } else {
            task.getIssue().setNotes(generateSuccessMsg());
            return true;
        }
    }

    private boolean doPyLint(Issue issue, String fileToManage) {
        return doPyLint(issue, fileToManage, 10.0);
    }

    //см новую реализацию с Configured task ниже
    private boolean doPyLint(Issue issue, String fileToManage, double rating) {
        new MyPylint().startPylint(fileToManage);
        String attachName = fileToManage + "_errorReport.txt";
        String lastLineInReport = readLastLineInFile(attachName);
        float studentPythonRating = 0;
        try {
            studentPythonRating = this.pythonRatingCheck(lastLineInReport);
        } catch (Exception ex) {
            studentPythonRating = -20f;
        }
        //Todo: Пересмотреть условия в IF
        boolean successfullPyLint = false;

        if (neededPythonRating > studentPythonRating) {
            String studentsName = getStudentsName(issue.getId(), this.professorName);
            System.out.println("(assigning back to Student) - " + studentsName + " " + lastLineInReport);
            this.setIssueAssigneeNameForIssue(issue, studentsName);
            lastLineInReport += "\n Some corrections are required! Keep trying!";
            this.uploadAttachment(issue, attachName);
        } else {
            lastLineInReport += "\n " + generateSuccessMsg();
            successfullPyLint = true;
        }
        issue.setNotes(lastLineInReport);
        this.updateIssue(issue);
        return successfullPyLint;
    }

    private boolean doPyLint(ConfiguredTask task, String fileToManage) {
        new MyPylint().startPylint(fileToManage);
        String attachName = fileToManage + "_errorReport.txt";
        String lastLineInReport = readLastLineInFile(attachName);
        double studentPythonRating = 0;
        try {
            studentPythonRating = this.pythonRatingCheck(lastLineInReport);
        } catch (Exception ex) {
            studentPythonRating = -200;
        }
        boolean isPLintSuccessful = false;

        if (task.getRequiredPythonRating() > studentPythonRating) {
            String studentsName = getStudentsName(task.getIssue().getId(), this.professorName);
            System.out.println("(PyLint - assigning back to Student) - " + studentsName + " " + lastLineInReport);
            this.setIssueAssigneeNameForIssue(task.getIssue(), studentsName);
            lastLineInReport += "\n Some corrections are required! Check the report and keep trying!";
            this.uploadAttachment(task.getIssue(), attachName);
        } else {
            lastLineInReport += "\n" + generateSuccessMsg();
            isPLintSuccessful = true;
        }
        task.getIssue().setNotes(lastLineInReport);
        this.updateIssue(task.getIssue());
        return isPLintSuccessful;
    }

    private void downloadAttachments(String url, String apikey, String fileName) throws IOException {

        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder()
                .url(url)
                .get()
                .addHeader("x-redmine-api-key", apikey)
                .addHeader("cache-control", "no-cache") //не обязательно
                .build();

        Response response = client.newCall(request).execute();

        try (InputStream in = response.body().byteStream()) {
            Path to = Paths.get(fileName); //convert from String to Path
            Files.copy(in, to, StandardCopyOption.REPLACE_EXISTING);
        }

    }

    public List<Issue> getIssues() throws RedmineException {
        issues = issueManager.getIssues(projectKey, queryId, Include.journals, Include.attachments, Include.changesets);
        return issues;
    }

    public List<Issue> getIssues(String iterationName) throws RedmineException {
        //15306
        String iterationid = getIterationIdByName(iterationName);

        final Map<String, String> params = new HashMap<String, String>();
        params.put("project_id", projectKey);
        params.put("fixed_version_id", iterationid);
        params.put("limit", "100");
        params.put("include", "attachments, journals");
        issues = issueManager.getIssues(params).getResults();
        return issues;
    }

    public List<Issue> getClosedIssues(String iterationName) {
        String iterationid = getIterationIdByName(iterationName);

        final Map<String, String> params = new HashMap<String, String>();
        params.put("project_id", projectKey);
        params.put("fixed_version_id", iterationid);
        params.put("limit", "100");
        params.put("status_id", "5"); // 5 = closed
        try {
            issues = issueManager.getIssues(params).getResults();
        } catch (RedmineException e) {
            e.printStackTrace();
        }
        // dirtyhack. get another 100.
        final Map<String, String> params2 = new HashMap<String, String>();
        params2.put("project_id", projectKey);
        params2.put("fixed_version_id", iterationid);
        params2.put("limit", "100");
        params2.put("offset", "100");
        params2.put("status_id", "5"); // 5 = closed
        try {
            issues.addAll(issueManager.getIssues(params2).getResults());
        } catch (RedmineException e) {
            e.printStackTrace();
        }
        return issues;
    }

    public List<Issue> getMyIssues(String iterationName) throws RedmineException {

        String iterationid = getIterationIdByName(iterationName);

        final Map<String, String> params = new HashMap<>();
        params.put("project_id", projectKey);
        params.put("fixed_version_id", iterationid);
        params.put("limit", "100");
        params.put("assigned_to_id", "me");
        params.put("include", "attachments, journals");
        issues = issueManager.getIssues(params).getResults();
        return issues;
    }

    private String getIterationIdByName(String iterationName) {
        String retVal = "";
        int projectKeyInt = 0;
        List<Version> allVersions = null;
        try {
            projectKeyInt = mgr.getProjectManager().getProjectByKey(projectKey).getId();
            allVersions = this.mgr.getProjectManager().getVersions(projectKeyInt);
            for (Version version : allVersions) {
                if (version.getName().equals(iterationName)) {
                    retVal = version.getId().toString();
                    break;
                }
            }
        } catch (RedmineException ex) {
            Logger.getLogger(ConnectionWithRedmine.class.getName()).log(Level.SEVERE, null, ex);
        }
        return retVal;
    }

    public Collection<Version> getVersions(String projectKey) throws RedmineException {
        Project project = projectManager.getProjectByKey(projectKey);
        int projectID = project.getId();
        versions = projectManager.getVersions(projectID);
        return versions;
    }

    public Issue getIssueByID(Integer issueID) throws RedmineException {
        return issueManager.getIssueById(issueID, Include.journals, Include.attachments);
    }

    public void uploadAttachment(Issue issue, String path) {

        try {
            File file = new File(path);
            attachmentManager.addAttachmentToIssue(issue.getId(), file, ContentType.TEXT_PLAIN.getMimeType());
        } catch (RedmineException | IOException ex) {
            Logger.getLogger(ConnectionWithRedmine.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public int isAttachmentIdWasEarlierChecked(Integer id) throws IOException {
        List<String> attachmentIDs = new ArrayList<String>();
        attachmentIDs = Files.readAllLines(Paths.get("AttachmentID.txt"), Charsets.UTF_8);
        int response = 0;
        int attachWasCheckedBefore = 1;
        int attachIsNew = 0;

        for (String attach : attachmentIDs) {
            if (attach.trim().equals("")) {
                continue;
            }
            long idFromFile = Long.parseLong(attach);
            if (idFromFile == id) {
                response = attachWasCheckedBefore;
                break;
            } else {
                response = attachIsNew;
            }
        }
        if (response == attachIsNew) {
            String fromIntToString = id + "\r\n";
            Files.write(Paths.get("AttachmentID.txt"), fromIntToString.getBytes(), StandardOpenOption.APPEND);
        }
        return response;
    }

    private void removeDirectory(File dir) {
        if (dir.isDirectory()) {
            File[] files = dir.listFiles();
            if (files != null && files.length > 0) {
                for (File aFile : files) {
                    removeDirectory(aFile);
                }
            }
            dir.delete();
        } else {
            dir.delete();
        }
    }

    private void cleanDirectory(File dir) {
        if (dir.isDirectory()) {
            File[] files = dir.listFiles();
            if (files != null && files.length > 0) {
                for (File aFile : files) {
                    removeDirectory(aFile);
                }
            }
        }
    }

    private String readLastLineInFile(String fileDir) {
        List<String> lines = new ArrayList<>();
        try {
            lines = Files.readAllLines(Paths.get(fileDir), Charsets.UTF_8);
        } catch (IOException ex) {
            Logger.getLogger(ConnectionWithRedmine.class.getName()).log(Level.SEVERE, null, ex);
        }
        String result = "";
        for (int i = lines.size() - 1; i >= 0; i--) {
            if (!lines.get(i).isEmpty()) {
                result = lines.get(i);
                break;
            }
        }
        if (result.indexOf('(') != -1) {
            result = result.substring(0, result.indexOf('('));
        }

        return result;
    }

    public Integer javaErrorAmountDetectionInFile(String string) {
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
        }
        else {
            return 0;
        }
    }

    public Integer cppErrorAmountDetectionInFile(String string) {

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

    public Float pythonRatingCheck(String lastStringInReport) {
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
        System.out.println(rateValue);
        return rateValue;
    }

    public void updateIssue(Issue issue) {
        try {
            mgr.getIssueManager().update(issue);
        } catch (RedmineException ex) {
            Logger.getLogger(ConnectionWithRedmine.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public void setVersionForCheck(String inputTargetVersion, Issue issue) {
        Version version = issue.getTargetVersion();
        Collection<Attachment> attach = issue.getAttachments();

        if (inputTargetVersion.equals("All")) {
            try {
                this.checkAttachments(issue);
            } catch (IOException ex) {
                Logger.getLogger(ConnectionWithRedmine.class.getName()).log(Level.SEVERE, null, ex);
            }
        } else if (version == null) {
            System.out.println("Issue without target version");
        } else if (version.getName().equals(inputTargetVersion)) {
            try {
                this.checkAttachments(issue);
            } catch (IOException ex) {
                Logger.getLogger(ConnectionWithRedmine.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }

    public ArrayList<String> getProjectUsers() {
        MembershipManager membershipManager = mgr.getMembershipManager();

        List<Role> roles;
        List<Membership> memberships = new ArrayList<>();
        try {
            memberships = membershipManager.getMemberships(projectKey);
        } catch (RedmineException ex) {
            Logger.getLogger(ConnectionWithRedmine.class.getName()).log(Level.SEVERE, null, ex);
        }
        ArrayList<String> retArray = new ArrayList<>();
        for (Membership m : memberships) {
            retArray.add(m.getUserName());
        }
        return retArray;
    }

    public ArrayList<String> getIterationTasks(String iteration) {
        List<Issue> issues = new ArrayList<>();
        try {
            issues = getIssues(iteration);
        } catch (RedmineException ex) {
            Logger.getLogger(ConnectionWithRedmine.class.getName()).log(Level.SEVERE, null, ex);
        }
        ArrayList<String> retVal = new ArrayList<>();
        for (Issue issue : issues) {
            retVal.add(issue.getId() + ": " + issue.getSubject());
        }
        return retVal;
    }

    public void copyAndAssignIssue(int issueId, String nameTo) {
        Issue currIssue = new Issue();
        try {
            currIssue = getIssueByID(issueId);
        } catch (RedmineException ex) {
            Logger.getLogger(FXMLDocumentController.class.getName()).log(Level.SEVERE, null, ex);
        }
        Issue newIssue = new Issue();
        newIssue.setSubject(currIssue.getSubject());
        newIssue.setTargetVersion(currIssue.getTargetVersion());
        newIssue.setCategory(currIssue.getCategory());
        newIssue.setProjectId(currIssue.getProjectId());
        newIssue.setPrivateIssue(true);
        newIssue.setAssigneeName(nameTo);
        newIssue.setDescription(currIssue.getDescription());
        newIssue = setIssueAssigneeNameForIssue(newIssue, nameTo);
        try {
            mgr.getIssueManager().createIssue(newIssue);
        } catch (RedmineException ex) {
            Logger.getLogger(ConnectionWithRedmine.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    private String getStudentsName(int id, String managerName) {
        String st = new RedmineJournalsReader(url, this.apiAccessKey).getStudentsName(id, managerName);
        return st;
    }

    private String getStudentsName(int id) {
        return getStudentsName(id, professorName);
    }

    private String generateSuccessMsg() {
        String succ = new PhrasesGenerator().getSuccessRandomPhrase();
        return succ + " Waiting for further checks.";
    }

    //тут надо что-то сделать с этим файлом: убить кириллицу и пробелы,
    // оставив только латиницу
    private String makeUsableFileName(String fileName, String author, String taskTitle) {
        fileName = (Translit.toTranslit(author.toLowerCase())
                + "_" + Translit.toTranslit(taskTitle.toLowerCase())
                + "_" + fileName.toLowerCase())
                .replaceAll(" ", "");
        StringBuilder retStr = new StringBuilder();

        for (int i = 0; i < fileName.length(); i++) {
            if (fileName.charAt(i) >= 'a' && fileName.charAt(i) <= 'z'
                    || fileName.charAt(i) == '.'
                    || fileName.charAt(i) == '_') {
                retStr.append(fileName.charAt(i));
            }
        }

        //Защита от совсем левака
        if (retStr.toString().equalsIgnoreCase(".py")) {
            retStr = new StringBuilder("task.py");
        }
        return retStr.toString();
    }

    private int doPyTaskCheck(PyTaskChecker checker, Issue issue) {
        String result = "";
        try {
            result = checker.startPyCheck();
        } catch (UnsupportedOperationException ex) {
            return -1;
        }
        int success = 0;
        String[] splittedResult = result.split("\n");
        if (splittedResult[splittedResult.length - 1].toLowerCase().equals("passed")) {
            issue.setNotes("All tests passed");
            success = 1;
        } else {
            issue.setNotes(result);
        }
        return success;
    }

    private int doJavaTaskCheck(JavaTaskChecker checker, Issue issue) {
        String result = "";
        try {
            result = checker.startJavaCheck();
        } catch (UnsupportedOperationException ex) {
            return -1;
        }
        int success = 0;
        String[] splittedResult = result.split("\n");
        if (splittedResult[splittedResult.length - 1].toLowerCase().equals("passed")) {
            issue.setNotes("All tests passed");
            success = 1;
        } else {
            issue.setNotes(result);
        }
        return success;
    }

    public void downloadResults() {

    }

    public void setLint(boolean lintStatus) {
        lint = lintStatus;
    }

    public boolean getLint() {
        return lint;
    }
}
