package informationsystem.loggerWindow;

import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.TextArea;
import tools.PvkLogger;

import java.net.URL;
import java.util.ResourceBundle;

public class LoggerWindowController implements Initializable {
    @FXML
    private TextArea txtBox;

    private PvkLogger logger;

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
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

    }
}
