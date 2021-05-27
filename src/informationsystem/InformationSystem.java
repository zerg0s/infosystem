package informationsystem;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import javafx.util.Pair;
import org.xml.sax.SAXException;
import redmineManagement.IssuesChecker;

import javax.xml.parsers.ParserConfigurationException;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * @author Zerg0s
 */
public class InformationSystem extends Application {

    private final String[] updatersList = new String[]{
            "https://textanalysis.ru/pvkrobot/",
            "http://boberpul2.asuscomm.com:8585/"};
    private String onlineResource = "https://textanalysis.ru/pvkrobot/";
    private String onlineXml;

    @Override
    public void start(Stage stage) {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("FXMLDocument.fxml"));
            Parent root = loader.load();
            FXMLDocumentController controller = loader.getController();
            loader.setRoot(this);
            loader.setClassLoader(getClass().getClassLoader());

            Scene scene = new Scene(root);
            stage.setTitle("Проверка задач в системе Redmine");
            stage.setScene(scene);
            stage.setOnHidden(e -> controller.shutdown());
            stage.show();
            String oldVersion = ((Text) root.lookup("#versionName"))
                    .getText().replaceAll("[^\\d.]", "");
            checkNewVersion(oldVersion);
        } catch (IOException ex) {
            Logger.getLogger(InformationSystem.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    private void checkNewVersion(String oldVersion) {
        float onlineVersion = Float.parseFloat(oldVersion);

        // Find the highest online version in all available sources
        for (String path : updateUpdatersList(updatersList)) {
            String onlineXmlTemp = readOnlineXml(path);
            if (Float.parseFloat(checkNewOnlineVersion(onlineXmlTemp)) > onlineVersion) {
                onlineVersion = Float.parseFloat(checkNewOnlineVersion(onlineXmlTemp));
                onlineResource = path;
                onlineXml = onlineXmlTemp;
            }
        }

        ButtonType myOK = new ButtonType("Обновить", ButtonBar.ButtonData.OK_DONE);

        if (Float.parseFloat(oldVersion) < onlineVersion) {
            String newVersionAvailable = "Доступна новая версия!";
            String oldVersionData = "Текущая версия: " + oldVersion + ".\nВсе несохраненные данные будут утеряны.";
            String newVersionData = "Новая версия: " + onlineVersion;
            newVersionData += getNewVersionDescription(onlineXml);
            Alert alert = new Alert(Alert.AlertType.CONFIRMATION, newVersionAvailable, myOK, ButtonType.CANCEL);
            alert.setHeaderText(newVersionData);
            alert.setContentText(oldVersionData);
            alert.setTitle(newVersionAvailable);

            Optional<ButtonType> result = alert.showAndWait();
            //download main distributive - mandatory file for a new version
            //should be named InformationSystem.jar_new.jar
            if (!result.isPresent() || result.get() == myOK) {
                // if (updateFile(XmlReader.getFilePath(onlineXml, "main"))) {
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
                //System.exit(0);
//                            }
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
                // }
                ArrayList<Pair<String, String>> files = XmlReader.getAllAdditionalFiles(onlineXml);
                for (Pair<String, String> fileFromTo : files) {
                    updateFile(fileFromTo);
                }
                System.exit(0);
            }
        }
    }

    private Iterable<String> updateUpdatersList(String[] updatersList) {
        try {
            List<String> updateSources = Stream.concat(Arrays.stream(updatersList).sequential(),
                    Files.readAllLines(Path.of("updater.dat")).stream()).collect(Collectors.toList());
            return Stream.concat(updateSources.stream(),
                                 updateSources.stream().map((s -> s.endsWith("/") ? s.concat("version.xml")
                                                                                  : s.concat("/version.xml"))))
                    .distinct()
                    .collect(Collectors.toList());
        } catch (IOException e) {
            e.printStackTrace();
        }
        return Arrays.asList(updatersList);
    }

    private String readOnlineXml(String path) {
        try (InputStream in = new URL(path).openStream()) {
            byte[] bytes = in.readAllBytes();
            return new String(bytes, Charset.forName("utf8"));
        } catch (IOException e) {
            //e.printStackTrace();
            return "";
        }
    }

    private String getNewVersionDescription(String readXml) {
        try {
            List<String> descriptions = XmlReader.getDescription(readXml, "description", "point");
            return String.join("", descriptions);
        } catch (IOException | ParserConfigurationException | SAXException e) {
            e.printStackTrace();
            return "";
        }
    }

    private String checkNewOnlineVersion(String readXml) {
        try {
            String version = XmlReader.getTextTagValue("version", XmlReader.loadXMLFromString(readXml));
            return !version.equals("") ? version : "0";
        } catch (IOException | ParserConfigurationException | SAXException e) {
            //e.printStackTrace();
            return "0";
        }
    }

    private boolean updateFile(Pair<String, String> pathFromPathTo) {
        StringBuilder resultingPath = new StringBuilder(onlineResource);
        if (pathFromPathTo == null || pathFromPathTo.getKey().isBlank()) {
            return false;
        }

        resultingPath.append(pathFromPathTo.getKey());
        try (InputStream in = new URL(resultingPath.toString()).openStream()) {
            Files.copy(in, Paths.get(pathFromPathTo.getValue()), StandardCopyOption.REPLACE_EXISTING);
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
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
