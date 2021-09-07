package redmineManagement;

import com.taskadapter.redmineapi.RedmineException;
import com.taskadapter.redmineapi.bean.Issue;
import informationsystem.FXMLDocumentController;
import informationsystem.RedmineConnectionProperties;

import java.io.IOException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

public class IssuesChecker {
    private ConnectionWithRedmine connectionToRedmine;
    private RedmineAlternativeReader redmineAlternativeReader;
    private RedmineConnectionProperties props;
    private String professorName = "Sergey Politsyn";

    public IssuesChecker(RedmineConnectionProperties props) {
        this.props = props;
        connectionToRedmine = new ConnectionWithRedmine(props.apiAccessKey, props.projectKey, props.url);
        redmineAlternativeReader = new RedmineAlternativeReader(props.url, props.apiAccessKey);
    }

    public void checkSingleIssue() {
        checkSingleIssue(props.issueNumbers);
    }

    public void checkSingleIssue(String issueNumber) {

        int issueNumLong;

        try {
            issueNumLong = Integer.parseInt(issueNumber);
            processIssue(issueNumLong);
        } catch (Exception ex) {
            Logger.getAnonymousLogger().log(Level.INFO, ex.toString());
        }
    }

    private void processIssue(int issueNumLong) {
        ArrayList<String> journals;
        try {
            Issue issue = connectionToRedmine.getIssueByID(issueNumLong);
            if (!issue.getStatusName().equals("Closed") && !issue.getStatusName().equals("Approved")) {
                logger.log(Level.INFO, issue.toString());
                //connectionToRedmine.setVersionForCheck(comboxVersion.getValue().toString(), issue);
                connectionToRedmine.checkAttachmentsForced(issue);
                journals = redmineAlternativeReader.getJournals(issue.getId().toString());
                connectionToRedmine.setStudentName(getStudentName(journals, professorName));
            }

        } catch (IOException | RedmineException ex) {
            logger.log(Level.SEVERE, null, ex);
        }
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

    private static Logger logger = Logger.getLogger(FXMLDocumentController.class.getSimpleName());
}
