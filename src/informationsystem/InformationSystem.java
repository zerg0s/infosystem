/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package informationsystem;

import com.taskadapter.redmineapi.bean.Issue;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import redmineManagement.ConnectionWithRedmine;
import redmineManagement.IssuesChecker;

import java.io.IOException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * @author user
 */
public class InformationSystem extends Application {

    private RedmineJournalsReader redmineJournalsReader;

    @Override
    public void start(Stage stage) {
        try {
            Parent root = FXMLLoader.load(getClass().getResource("FXMLDocument.fxml"));
            Scene scene = new Scene(root);
            stage.setTitle("Проверка задач в системе Redmine");
            stage.setScene(scene);
            stage.show();
        } catch (IOException ex) {
            Logger.getLogger(InformationSystem.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    public static void main(String[] args) {

        if (args.length != 0) {

            RedmineConnectionProperties connectionOptions = new RedmineConnectionProperties();
            connectionOptions.projectKey = args[1];
            connectionOptions.url = args[0];
            connectionOptions.apiAccessKey = args[2];
            connectionOptions.issueNumbers = args[3];
            IssuesChecker issues = new IssuesChecker(connectionOptions);
            issues.checkSingleIssue();

        } else {
            // загрузка конфигов
            // открытие сцены
            launch(args);
        }
    }

}
