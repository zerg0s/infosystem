package taskCheckers;

import informationsystem.XmlReader;

import java.util.HashMap;

public class TaskChecker {
    protected String subject;
    protected String fileToManage;
    protected static HashMap<String, String> knownTests;

    static {
        fillData();
    }

    private static void fillData() {
        XmlReader reader = new XmlReader(".\\TestsInfo_v2.xml");
        knownTests = reader.getAlltests();
    }

    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public String getNameForKnownTest(String subject) {
        return getTestName3(subject);
    }
    public String getNameForKnownTest() {
        return getTestName3(getSubject());
    }

    String getFileToManage() {
        return fileToManage;
    }

    void setFileToManage(String fileToManage) {
        this.fileToManage = fileToManage;
    }

    String getTestName3(String subjectFromIssue) {
        String testFolderName;
        testFolderName = knownTests.getOrDefault(subjectFromIssue, "");
        //еще одна попытка найти по неполному совпадению
        if (testFolderName.equals("")){
            for(String test : knownTests.keySet()){
                if (subjectFromIssue.toLowerCase().contains(test.toLowerCase()))
                {
                    testFolderName = knownTests.getOrDefault(test, "");
                }
            }
        }
        return testFolderName;
    }

    class FileAndItsTest {
        String fileName = "file.py";
        String testName = "test";
    }

}
