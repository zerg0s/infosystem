package informationsystem.loggerWindow;

import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.text.TextFlow;
import javafx.stage.Stage;
import tools.PvkLogger;

import java.net.URL;
import java.util.ResourceBundle;

public class LoggerWindowController implements Initializable {
    @FXML
    private TextArea txtBox;
    @FXML
    private TextFlow txtRich;
    @FXML
    private Button btnClose;

    private PvkLogger logger;
    private Stage stage;

    @FXML
    public void appendLogs(String text) {
        Platform.runLater(() -> {
            txtBox.appendText("\n" + text);
        });
    }

    public void setLogger(PvkLogger logger) {
        this.logger = logger;
    }

    @FXML
    public void shutdown() {
        // get a handle to the stage
        Stage stage = (Stage) btnClose.getScene().getWindow();
        // do what you have to do
        stage.close();
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

    }

    public Stage getStage() {
        return stage;
    }

    public void setStage(Stage stage) {
        this.stage = stage;
    }
}
