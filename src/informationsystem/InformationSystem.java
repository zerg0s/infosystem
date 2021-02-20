package informationsystem;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import redmineManagement.IssuesChecker;
import redmineManagement.RedmineJournalsReader;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.Optional;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * @author Zerg0s
 */
public class InformationSystem extends Application {

    private RedmineJournalsReader redmineJournalsReader;
    private final String onlineResource = "http://textanalysis.ru/pvkrobot/version.txt";
    private final String onlineResourceDistr = "http://textanalysis.ru/pvkrobot/InformationSystem.jar";

    @Override
    public void start(Stage stage) {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("FXMLDocument.fxml"));
            Parent root = loader.load();
            FXMLDocumentController controller = loader.getController();
            //Parent root = FXMLLoader.load(getClass().getResource("/informarionsystem/FXMLDocument.fxml"));
            Scene scene = new Scene(root);
            stage.setTitle("Проверка задач в системе Redmine");
            stage.setScene(scene);
            stage.setOnHidden(e -> controller.shutdown());
            stage.show();
            String oldVersion = ((Text) root.lookup("#versionName")).getText().replaceAll("[^\\d.]", "");
            checkNewVersion(oldVersion);
        } catch (IOException ex) {
            Logger.getLogger(InformationSystem.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    private void checkNewVersion(String oldVersion) {
        String onlineVersion = checkNewOnlineVersion();
        ButtonType myOK = new ButtonType("Обновить", ButtonBar.ButtonData.OK_DONE);

        if (Float.parseFloat(oldVersion) < Float.parseFloat(onlineVersion)) {
            Alert alert = new Alert(Alert.AlertType.CONFIRMATION, "Доступна новая версия!", myOK, ButtonType.CANCEL);
            alert.setHeaderText("Новая версия: " + onlineVersion);
            alert.setContentText("Текущая версия: " + oldVersion + ". Все несохраненные данные будут утеряны.");
            alert.setTitle("Доступна новая версия!");

            Optional<ButtonType> result = alert.showAndWait();
            if (!result.isPresent() || result.get() == myOK) {
                if (downloadDistr()) {
//                    // Run a java app in a separate system process
//                        for (String file : listFiles(".")) {
//                            // if there is a 'standard' bat to run our program
//                            if (file.contains("Run") && file.contains(".bat") && file.contains("InformationSystem")) {
//                                new Thread(() -> {
//                                    try {
//                                        Process proc = Runtime.getRuntime().exec(file);
//                                    } catch (IOException e) {
//                                        e.printStackTrace();
//                                    }
//                                }).start();
                                System.exit(0);
//                            }
                    System.exit(0);
//                    String runCmdLine ="rename InformationSystem.jar_new.jar InformationSystem.jar";
//                    String runCmdLine2 = "java.exe --module-path \".\\lib\" --add-modules javafx.controls,javafx.fxml " +
//                            " -Dfile.encoding=UTF-8 -classpath \"InformationSystem.jar;.\\lib\\javafx-swt.jar;" +
//                            ".\\lib\\javafx.web.jar;.\\lib\\javafx.base.jar;.\\lib\\javafx.fxml.jar;" +
//                            ".\\lib\\javafx.media.jar;.\\lib\\javafx.swing.jar;.\\lib\\javafx.controls.jar;" +
//                            ".\\lib\\javafx.graphics.jar\" informationsystem.InformationSystem";
//                    try {
//                        Process proc = Runtime.getRuntime().exec(runCmdLine);
//                        Process proc2 = Runtime.getRuntime().exec(runCmdLine2);
//                    } catch (IOException e) {
//                        e.printStackTrace();
//                    }
//                    System.exit(0);
                }
            }
        }
    }


    private boolean downloadDistr() {
        try (InputStream in = new URL(onlineResourceDistr).openStream()) {
            Files.copy(in, Paths.get(onlineResourceDistr.substring(onlineResourceDistr.lastIndexOf('/') + 1) + "_new.jar"),
                    StandardCopyOption.REPLACE_EXISTING);
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }

    private String checkNewOnlineVersion() {
        try (InputStream in = new URL(onlineResource).openStream()) {
            byte[] bytes = in.readAllBytes();
            return new String(bytes, Charset.defaultCharset());
        } catch (IOException e) {
            e.printStackTrace();
            return "0";
        }
    }

    private Set<String> listFiles(String dir) {
        return Stream.of(new File(dir).listFiles())
                .filter(file -> !file.isDirectory())
                .map(File::getName)
                .collect(Collectors.toSet());
    }

    public static void main(String[] args) {

        System.setProperty("java.net.useSystemProxies", "true");

        if (args.length != 0) {

            RedmineConnectionProperties connectionOptions = new RedmineConnectionProperties();
            connectionOptions.projectKey = args[1];
            connectionOptions.url = args[0];
            connectionOptions.apiAccessKey = args[2];
            connectionOptions.issueNumbers = args[3];
            IssuesChecker issues = new IssuesChecker(connectionOptions);
            issues.checkSingleIssue();

        } else {
            // открытие сцены
            launch(args);
        }
    }

}
