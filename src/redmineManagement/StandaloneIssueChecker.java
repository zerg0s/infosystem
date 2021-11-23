package redmineManagement;

import com.taskadapter.redmineapi.RedmineException;
import com.taskadapter.redmineapi.bean.Issue;
import informationsystem.FXMLDocumentController;
import informationsystem.RedmineConnectionProperties;

import java.io.IOException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

public class StandaloneIssueChecker {
    private ConnectionWithRedmine connectionToRedmine;
    private RedmineAlternativeReader redmineAlternativeReader;
    private RedmineConnectionProperties props;
    private String professorName = "Sergey Politsyn";

    public StandaloneIssueChecker(RedmineConnectionProperties props) {
        this.props = props;
        connectionToRedmine = new ConnectionWithRedmine(props.apiAccessKey, props.projectKey, props.url);
        redmineAlternativeReader = new RedmineAlternativeReader(props.url, props.apiAccessKey);
    }

    private static Logger logger = Logger.getLogger(FXMLDocumentController.class.getSimpleName());
}
