/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package informationsystem;

/**
 *
 * @author Zerg0s
 */
public class RedmineConnectionProperties {
    public String url = "";
    public String apiAccessKey = "";
    public String projectKey = "";
    public String issueNumbers = "";
    public String iterationName = "";

    public void setNewApiAccessKey(String apiKey) {
        this.apiAccessKey = apiKey;
        this.iterationName = "";
        this.projectKey = "";
    }
}
