package taskCheckers;

public class CppTaskChecker extends TaskChecker{

    public CppTaskChecker(String subject, String fileToManage, boolean easyMode) {
        this.setSubject(subject);
        this.setFileToManage(fileToManage);
        this.isEasyMode = easyMode;
        workingDir = ".\\JavaDir\\";
    }

    public static void main(String[] args) {

    }
}
