package data;

import com.taskadapter.redmineapi.bean.Issue;

public class ConfiguredTask {
    private Issue issue;
    private String taskCompleter;
    private boolean isNeededForceCheck;
    private boolean isLintRequired;
    private double requiredPythonRating;
    private int maxJavaLintErrors;
    private boolean isInEasyMode;

    public ConfiguredTask(Issue issue,
                          String taskCompleter,
                          boolean isNeededForceCheck,
                          boolean isLintRequired,
                          double requiredPythonRating,
                          int javaErrors,
                          boolean easyMode) {
        this.isLintRequired = isLintRequired;
        this.isNeededForceCheck = isNeededForceCheck;
        this.issue = issue;
        this.requiredPythonRating = requiredPythonRating;
        this.taskCompleter = taskCompleter;
        this.maxJavaLintErrors = javaErrors;
        this.isInEasyMode = easyMode;
    }

    @Override
    public String toString() {
        return issue.toString() + " " + "Need Force: " + isNeededForceCheck +
                " Need Lint: " + isLintRequired + " PyLint Rating: " + requiredPythonRating +
                " Java Error Limit: " + maxJavaLintErrors +
                " Student:" + taskCompleter;
    }

    public Issue getIssue() {
        return issue;
    }

    public void setIssue(Issue issue) {
        this.issue = issue;
    }

    public String getTaskCompleter() {
        return taskCompleter;
    }

    public void setTaskCompleter(String taskCompleter) {
        this.taskCompleter = taskCompleter;
    }

    public boolean isNeededForceCheck() {
        return isNeededForceCheck;
    }

    public void setNeededForceCheck(boolean neededForceCheck) {
        isNeededForceCheck = neededForceCheck;
    }

    public boolean isLintRequired() {
        return isLintRequired;
    }

    public void setLintRequired(boolean lintRequired) {
        isLintRequired = lintRequired;
    }

    public double getRequiredPythonRating() {
        return requiredPythonRating;
    }

    public void setRequiredPythonRating(double requiredPythonRating) {
        this.requiredPythonRating = requiredPythonRating;
    }

    public int getMaxJavaLintErrors() {
        return maxJavaLintErrors;
    }

    public void setMaxJavaLintErrors(int maxJavaLintErrors) {
        this.maxJavaLintErrors = maxJavaLintErrors;
    }

    public boolean isEasyMode() {
        return isInEasyMode;
    }
}
