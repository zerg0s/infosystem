package data;

public class StudentsIssue {
    private int id;
    private String studentsName;
    private String issueTitle;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getIssueName() {
        return issueTitle;
    }

    public void setIssueName(String issueName) {
        issueTitle = issueName;
    }

    public String getStudentsName() {
        return studentsName;
    }

    public void setStudentsName(String name) {
        studentsName = name;
    }

    @Override
    public String toString() {
        return "StudentsIssue{" +
                "id=" + id +
                ", studentsName='" + studentsName + '\'' +
                ", issueTitle='" + issueTitle + '\'' +
                '}';
    }
}
