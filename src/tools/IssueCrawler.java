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

    public IssueCrawler(RedmineConnectionProperties props) {
        properties = props;
        connection = new ConnectionWithRedmine(props.apiAccessKey,props.projectKey, props.url);
    }

    public List<Issue> getAllProjectIssues(String iteration) {
        if (iteration == null) {
            List<Issue> allIssues = new ArrayList<>();
            for (String version : connection.getVersions()) {
                allIssues.addAll(connection.getUniqueIssues(version));
            }

            //connection.getIssues();
            return allIssues;
        } else {
            return connection.getUniqueIssues(iteration);
        }
    }

    public List<Issue> getAllProjectIssues() {
       return getAllProjectIssues(null);
    }
}
