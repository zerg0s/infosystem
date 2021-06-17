package tools;

import com.taskadapter.redmineapi.RedmineException;
import com.taskadapter.redmineapi.bean.Issue;
import informationsystem.RedmineConnectionProperties;
import redmineManagement.ConnectionWithRedmine;

import java.util.ArrayList;
import java.util.List;

public class IssueCrawler {
    private ConnectionWithRedmine connection;
    private RedmineConnectionProperties properties;
    private final List<Issue> issues;

    public List<Issue> getIssues() {
        return issues;
    }

    public IssueCrawler(RedmineConnectionProperties props) {
        properties = props;
        connection = new ConnectionWithRedmine(props.apiAccessKey, props.projectKey, props.url);
        issues = new ArrayList<>();
    }

    public List<Issue> getAllProjectIssues(String iteration) {
        if (iteration == null) {
            List<Issue> allIssues = new ArrayList<>();
            for (String version : connection.getVersions()) {
                allIssues.addAll(connection.getUniqueIssues(version));
            }

            issues.addAll(allIssues);
        } else {
            issues.addAll(connection.getUniqueIssues(iteration));
        }

        return issues;
    }

    public List<Issue> getAllProjectIssues() {
        issues.addAll(getAllProjectIssues(null));
        return issues;
    }

    public void substractKnownIssues(List<String> allTaskNames) {
        issues.removeIf(issues -> allTaskNames.contains(issues.getSubject()));
    }

    public List<Issue> getIssuesWithAttachments() {
        List<Issue> issuesWithAttachments = new ArrayList<>();
        for (Issue issue : issues) {
            try {
                issuesWithAttachments.add(connection.getIssueByID(issue.getId()));
            } catch (RedmineException e) {
                e.printStackTrace();
            }
        }

        return issuesWithAttachments;
    }
}
